#!/usr/bin/env python
# -*- coding: utf-8 -*-

import shodan
import requests
import re
from auto_exp.lib.core.search.zoomeye.main import Zoo_main


class W_Shodan(object):

    def __init__(self, api):
        self.api = api
        self.shodan = shodan.Shodan(self.api)

    def search(self, keywords, pages=1):
        query = ' ' . join(keywords)
        result = self.shodan.search(query, pages)['matches']
        ip = []
        for addr in result:
            ip.append(addr['ip_str'])
        return ip


class W_Bing(object):

    def search(self, keywords, count, pages=1):
        count = count
        page = int(pages)
        query = keywords.replace(' ', '+')
        url = []

        try:
            res = requests.get('http://www.bing.com/search?q=' + query + '&count=' +
                               str(count) + "&first=" + str((page - 1) * int(count) + 1))
            match = re.findall(
                r'\<li class="b_algo"\>\<h2\>\<a target="_blank" href=\"(.*?)\" ', res.content)
            for val in match:
                url.append(val)
        except Exception, e:
            print e
            pass
        return url


class W_Zoomeye(Zoo_main):
    pass


class W_Baidu(object):

    def search(self, keywords, pages=1):
        page = str(10 * (pages - 1))
        keyword = keywords.replace(' ', '+')
        url = "http://www.baidu.com/s?wd=" + keyword + "&pn=" + page
        res = requests.get(url).text
        url1 = re.findall(
            r'<a target="_blank" href="(.*?)" class="c-showurl" style="text-d', res)
        url2 = []
        for line in url1:
            url2.append(requests.get(line).url)
        return url2

if __name__ == "__main__":
    pass
