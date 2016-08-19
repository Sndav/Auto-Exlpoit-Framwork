#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# A simple and fast sub domains brute tool for pentesters
# my[at]lijiejie.com (http://www.lijiejie.com)

import Queue
import sys
import dns.resolver
import threading
import time
import os
from auto_exp.lib.method.console.consle_width import getTerminalSize
from auto_exp.config.config import config


class DNSBrute:

    def __init__(self, target, names_file, ignore_intranet, threads_num):
        self.config = config()
        self.target = target.strip()
        self.names_file = names_file
        self.ignore_intranet = ignore_intranet
        self.thread_count = self.threads_num = threads_num
        self.scan_count = self.found_count = 0
        self.lock = threading.Lock()
        # Cal terminal width when starts up
        self.console_width = getTerminalSize()[0] - 2
        self.resolvers = [dns.resolver.Resolver() for _ in range(threads_num)]
        self._load_dns_servers()
        self._load_sub_names()
        self._load_next_sub()
        self.ip_dict = {}
        self.sub = []
        self.STOP_ME = False

    def _load_dns_servers(self):
        dns_servers = []
        with open(self.config.default_dns_server) as f:
            for line in f:
                server = line.strip()
                if server.count('.') == 3 and server not in dns_servers:
                    dns_servers.append(server)
        self.dns_servers = dns_servers
        self.dns_count = len(dns_servers)

    def _load_sub_names(self):
        self.queue = Queue.Queue()
        file = 'dict/' + \
            self.names_file if not os.path.exists(
                self.names_file) else self.names_file
        with open(file) as f:
            for line in f:
                sub = line.strip()
                if sub:
                    self.queue.put(sub)

    def _load_next_sub(self):
        next_subs = []
        with open(self.config.default_next_sub) as f:
            for line in f:
                sub = line.strip()
                if sub and sub not in next_subs:
                    next_subs.append(sub)
        self.next_subs = next_subs

    def _update_scan_count(self):
        self.lock.acquire()
        self.scan_count += 1
        self.lock.release()

    def _print_progress(self):
        self.lock.acquire()
        msg = '%s found | %s remaining | %s scanned in %.2f seconds' % (
            self.found_count, self.queue.qsize(), self.scan_count, time.time() - self.start_time)
        sys.stdout.write('\r' + ' ' * (self.console_width - len(msg)) + msg)
        sys.stdout.flush()
        self.lock.release()

    @staticmethod
    def is_intranet(ip):
        ret = ip.split('.')
        if not len(ret) == 4:
            return True
        if ret[0] == '10':
            return True
        if ret[0] == '172' and 16 <= int(ret[1]) <= 32:
            return True
        if ret[0] == '192' and ret[1] == '168':
            return True
        return False

    def _scan(self):
        thread_id = int(threading.currentThread().getName())
        self.resolvers[thread_id].nameservers.insert(
            0, self.dns_servers[thread_id % self.dns_count])
        self.resolvers[thread_id].lifetime = self.resolvers[
            thread_id].timeout = 10.0
        # limit max found records to 40000
        while self.queue.qsize() > 0 and not self.STOP_ME and self.found_count < 40000:
            sub = self.queue.get(timeout=1.0)
            for _ in range(3):
                try:
                    cur_sub_domain = sub + '.' + self.target
                    answers = self.resolvers[thread_id].query(cur_sub_domain)
                    is_wildcard_record = False
                    if answers:
                        for answer in answers:
                            self.lock.acquire()
                            if answer.address not in self.ip_dict:
                                self.ip_dict[answer.address] = 1
                            else:
                                self.ip_dict[answer.address] += 1
                                # a wildcard DNS record
                                if self.ip_dict[answer.address] > 2:
                                    is_wildcard_record = True
                            self.lock.release()
                        if is_wildcard_record:
                            self._update_scan_count()
                            self._print_progress()
                            continue
                        ips = ', '.join([answer.address for answer in answers])
                        if (not self.ignore_intranet) or (not DNSBrute.is_intranet(answers[0].address)):
                            self.lock.acquire()
                            self.found_count += 1
                            msg = cur_sub_domain.ljust(30) + ips
                            a = [cur_sub_domain, [
                                answer.address for answer in answers]]
                            self.sub.append(a)
                            sys.stdout.write(
                                '\r' + msg + ' ' * (self.console_width - len(msg)) + '\n\r')
                            sys.stdout.flush()
                            # self.outfile.write(
                            #    cur_sub_domain.ljust(30) + '\t' + ips + '\n')
                            self.lock.release()
                            try:
                                self.resolvers[thread_id].query(
                                    '*.' + cur_sub_domain)
                            except:
                                for i in self.next_subs:
                                    self.queue.put(i + '.' + sub)
                        break
                except dns.resolver.NoNameservers, e:
                    break
                except Exception, e:
                    pass
            self._update_scan_count()
            self._print_progress()
        self._print_progress()
        self.lock.acquire()
        self.thread_count -= 1
        self.lock.release()

    def run(self):
        self.start_time = time.time()
        for i in range(self.threads_num):
            t = threading.Thread(target=self._scan, name=str(i))
            t.setDaemon(True)
            t.start()
        while self.thread_count > 1:
            try:
                time.sleep(1.0)
            except KeyboardInterrupt, e:
                msg = '[WARNING] User aborted, wait all slave threads to exit...'
                sys.stdout.write('\r' + msg + ' ' *
                                 (self.console_width - len(msg)) + '\n\r')
                sys.stdout.flush()
                self.STOP_ME = True

    def getresult(self):
        return self.sub

if __name__ == '__main__':
    d = DNSBrute(target="wooyun.org",
                 names_file=config.default_subdomainfix,
                 ignore_intranet=False,
                 threads_num=10)

    d.run()
    while threading.activeCount() > 1:
        time.sleep(0.1)
