#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests
import re


class D_Proxy(object):

    def get(self, page):
        ret = []
        match_ip = []
        match_port = []
        url = "http://www.kuaidaili.com/proxylist/"
        for i in range(page):
            cerrent_url = url + str(i + 1)
            content = requests.get(cerrent_url).content
            match_ip += re.findall(r'IP\">(.*?)<\/td>', content)
            match_port += re.findall(r'PORT\">(.*?)<\/td>', content)
        for i in range(len(match_ip)):
            match = [
                match_ip[i],
                match_port[i],
            ]
            ret.append(match)
        return ret
if __name__ == "__main__":
    a = D_Proxy()
    print a.get(2)
