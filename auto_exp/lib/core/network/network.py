#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests
import re

class N_Request():
	def get_title(self,url):
		headers={'Accept-Language': 'zh-cn',
            'Content-Type': 'application/x-www-form-urlencoded',
            'User-Agent': 'Mozilla/4.0 (compatible MSIE 6.00 Windows NT 5.1 SV1)',
        }
		try:
			con = requests.get(url,headers=headers).text
			a = re.findall(r"<title>(.*?)</title>",con)
			try:
				return a[0]
			except:
				return ""
		except:
			pass
	def check(self,url):
		try:
			res = requests.get(url,timeout = 2)
			if res.status_code == requests.codes.ok:
				return True
			else:
				return False
		except:
			return False
if __name__ == "__main__":
	pass