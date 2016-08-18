#!/usr/bin/env python
# -*- coding: utf-8 -*-
import threading
from time import gmtime, strftime
import Queue


class threads(threading.Thread):
    """docstring for threads"""

    def __init__(self, queue):
        self.queue = queue

    def run(self):
        pass


def run(cla, thread_count):
    try:
        threads = []
        for i in range(int(thread_count)):
            threads.append(cla)

        print threads
        for t in threads:
            t.start()
        for t in threads:
            t.join()
    except:
        pass

if __name__ == "__main__":
    class worker(threading.Thread):

        def __init__(self, queue):
            threading.Thread.__init__(self)
            self.queue = queue

        def run(self):
            while True:
                if self.queue.empty():
                    break
                try:
                    print str(self.queue.get_nowait()) + " " + strftime("%Y %H:%M:%S", gmtime())
                except:
                    break
    q = Queue.Queue()
    for i in range(10):
        q.put(i)
    # print q
    run(worker(q), 5)
