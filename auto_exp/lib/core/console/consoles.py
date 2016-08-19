#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from cmd import Cmd
from auto_exp.lib.method.switch.switch import switch
from auto_exp.lib.core.exploit.load_exp import exp
from auto_exp.lib.method.output.CLIOutput import CLIOutput
from auto_exp.lib.core.output.output import O_Output
from auto_exp.lib.controller.db.db import DB
from auto_exp.lib.core.file.file import IO_File
from auto_exp.config.config import config
from auto_exp.lib.core.search.subdomain import DNSBrute
from auto_exp.lib.core.search.discoverproxyserver import D_Proxy
from auto_exp.lib.core.network.network import N_Request
from auto_exp.lib.core.network.api.listener import *


class C_Base(Cmd):

    def __init__(self):
        self.net = N_Request()
        self.config = config()
        self.db = DB()
        self.output = CLIOutput()
        self.output2 = O_Output()
        self.exp = exp()
        Cmd.__init__(self)
        os.system("clear")
        self.output.printYellow(
            "Welcome To Auto-Exploit-Framework\nThe world Will Remember You Forever")
        self.case_insensitive = False
        self.prompt = self.config.default_console_words
        self.isused = False
        self.file = IO_File()

    def do_help(self, arg):
        self.output.printYellow("[Command]")
        print "    use [exp]                    : use exploit"
        print "    show exploit                 : show the info of exploit"
        print "    del [exp]                    : del exploit"
        print "    load exploit                 : load exploit"
        print "    proxysearch [page]           : Search Proxy"
        print "    subdimain [domain]           : Search Subdimain"
        self.output.printYellow("[System]")
        print "    exit                         : exit the system"
        self.output.printYellow("[Web]")
        print "    runserver                    : start server"
        self.output.printYellow("[Exploit]")
        print "    run                          : run exploit"
        self.output.printYellow("[Help]")
        print "    help [command]               : show help"

    def do_proxysearch(self, arg):
        page = int(arg)
        pro = D_Proxy()
        re = pro.get(page)
        name = ['IP', 'PORT']
        self.output2.print_form(name, re)

    def do_use(self, arg):
        if arg:
            try:
                exploit = self.exp.load_exp(arg)
                self.exploit = exploit
                self.exploit.print_desc()
                self.isused = True
            except:
                self.output2.print_error('Failed to load exploit')

    def do_show(self, arg):
        if not arg:
            pass
        elif arg == 'exp' or arg == 'exploit':
            self.case_insensitive = True
            exploit = self.db.get_exp()
            name = ['id', 'name', 'desc', 'level', 'author']
            exploit = list(exploit)
            for i in range(len(exploit)):
                exploit[i] = list(exploit[i])
                exploit[i][3] = self.__get_level(exploit[i][3])
            self.output2.print_form(name, exploit)

    def do_run(self, arg):
        if self.isused:
            self.exploit.run()
        else:
            self.output2.print_warning('Please Use an Exploit')

    def do_load(self, arg):
        if not arg:
            pass
        else:
            # print self.config.path+'exploit/'+arg+'.py'
            if self.file.check_file(self.config.path + 'exploit/' + arg + '.py'):
                exp = self.exp.load_exp(arg)
                if arg == exp.info['Name']:
                    self.db.insert_exp(exp.info['Name'], exp.info['Desc'], exp.info[
                                       'Level'], exp.info['Author'])
                else:
                    self.output2.print_error("Exploit Name != File Name")
            else:
                self.output2.print_error('Please Move You Exploit To /exploit')

    def do_del(self, arg):
        self.db.del_exp(arg)
        pass

    def do_exit(self, arg):
        quit()
        pass

    def __get_level(self, level):
        a = ['low', 'medium', 'high']
        return a[level]

    def default(self, line):
        pass

    def do_subdomain(self, domain):
        d = DNSBrute(target=domain,
                     names_file=self.config.default_subdomainfix,
                     ignore_intranet=False,
                     threads_num=10)
        d.run()

    def do_runserver(self, arg):
        create_server(self.config.host, self.config.api_port)

    def emptyline(self):
        self.default('')
if __name__ == "__main__":
    pass
