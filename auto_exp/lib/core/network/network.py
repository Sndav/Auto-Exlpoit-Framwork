#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests
import re
from auto_exp.lib.core.search.discoverproxyserver import D_Proxy
from random import Random


class N_Request(object):

    use_proxy = False

    def get_title(self, url):
        headers = {'Accept-Language': 'zh-cn',
                   'Content-Type': 'application/x-www-form-urlencoded',
                   'User-Agent': 'Mozilla/4.0 (compatible MSIE 6.00 Windows NT 5.1 SV1)',
                   }
        try:
            con = requests.get(url, headers=headers).text
            a = re.findall(r"<title>(.*?)</title>", con)
            try:
                return a[0]
            except:
                return ""
        except:
            pass

    def request_get(self, url):
        if self.use_proxy:
            ran = Random()
            i = ran.Random()
            proxyser = self._getproxyserver()
            proxy = {
                "http": "http://" + proxyser[i][0] + ":" + proxyser[i][1]
            }
        else:
            proxy = {}
        try:
            return requests.get(url, proxy=proxy)
        except:
            return None

    def check(self, url):
        try:
            res = requests.get(url, timeout=2)
            if res.status_code == requests.codes.ok:
                return True
            else:
                return False
        except:
            return False

    def _getproxyserver(self):
        pro = D_Proxy()
        return pro.get(2)

if __name__ == "__main__":
    pass
