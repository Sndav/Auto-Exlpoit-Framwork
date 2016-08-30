#!/usr/bin/python
# -*-coding:utf-8-*-
import requests
import time
import json


class SqlMapApi:

    def __init__(self, server='', target='', options={"threads": 10}):
        super(SqlMapApi, self).__init__()
        self.options = options
        self.server = server
        if self.server[-1] != '/':
            self.server = self.server + '/'
        self.target = target
        self.taskid = ''
        self.engineid = ''
        self.status = ''
        self.start_time = time.time()

    # Start Scan Task

    def task_new(self):
        self.taskid = json.loads(
            requests.get(self.server + 'task/new').text)['taskid']
        # get taskid,according to this taskid , do someting else
        if len(self.taskid) > 0:
            return True
        return False

    # Delete Scan Task

    def task_delete(self):
        if json.loads(requests.get(self.server + 'task/' + self.taskid + '/delete').text)['success']:
            return True
        return False

    # Start Scan Task

    def scan_start(self):
        headers = {'Content-Type': 'application/json'}
        payload = {'url': self.target}
        url = self.server + 'scan/' + self.taskid + '/start'
        # http://127.0.0.1:8557/scan/xxxxxxxxxx/start
        t = json.loads(
            requests.post(url, data=json.dumps(payload), headers=headers).text)
        self.engineid = t['engineid']
        if len(str(self.engineid)) > 0 and t['success']:
            return True
        return False

    # Get Status of Tasks

    def scan_status(self):
        self.status = json.loads(
            requests.get(self.server + 'scan/' + self.taskid + '/status').text)['status']
        if self.status == 'running':
            return 'running'
        elif self.status == 'terminated':
            return 'terminated'
        else:
            return 'error'

    # Get Status of Tasks

    def scan_data(self):
        data = json.loads(
            requests.get(self.server + 'scan/' + self.taskid + '/data').text)['data']
        if len(data) == 0:
            return {
                "Injection": False,
                "Target": "",
            }
        else:
            return {
                "Injection": True,
                "Target": self.target,
            }

    # Main Option Of Ccan

    def option_set(self):
        headers = {'Content-Type': 'application/json'}
        option = {
            "options": self.options
        }
        url = self.server + 'option/' + self.taskid + '/set'
        t = json.loads(
            requests.post(url, data=json.dumps(option), headers=headers).text)
        return t

    # Stop Tasks

    def scan_stop(self):
        json.loads(
            requests.get(self.server + 'scan/' + self.taskid + '/stop').text)['success']

    # Kill Tasks Progress

    def scan_kill(self):
        json.loads(
            requests.get(self.server + 'scan/' + self.taskid + '/kill').text)['success']

    def run(self):
        if not self.task_new():
            return False
        self.option_set()
        if not self.scan_start():
            return False
        while True:
            if self.scan_status() == 'running':
                time.sleep(10)
            elif self.scan_status() == 'terminated':
                break
            else:
                break
            if time.time() - self.start_time > 3000:
                self.scan_stop()
                self.scan_kill()
                break
        self.scan_data()
        self.task_delete()

if __name__ == '__main__':
    t = SqlMapApi('http://127.0.0.1:8774', 'http://192.168.3.171/1.php?id=1')
    t.run()
