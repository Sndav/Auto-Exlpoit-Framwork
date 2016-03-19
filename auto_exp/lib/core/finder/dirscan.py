#!/usr/bin/env python
# encoding: utf-8

import auto_exp.lib.method.requests as requests
from auto_exp.lib.method.utils.FileUtils import FileUtils
import sys

class S_Dirscan(object):
# 全局配置
	def __init__(self,dic_path,threads=10,timeout=3,allow_redirects=False,proxy=False):
		self.dir_exists = []
		#self.siteurl = siteurl
		self.using_dic = dic_path
		self.threads_count = threads
		self.timeout = timeout
		self.allow_redirects = allow_redirects
		self.headers = {
			'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/535.20 (KHTML, like Gecko) Chrome/19.0.1036.7 Safari/535.20',
			'Referer' : 'http://www.google.com',
			'Cookie': 'whoami=wyscan_dirfuzz',
		}
		if proxy:
			self.proxies = {
				"http": "http://127.0.0.1:8080"
			}
		else:
			self.proxies = {}

	def dir_check(self,url):
		return requests.get(url, stream=True, headers=self.headers, timeout=self.timeout, proxies=self.proxies, allow_redirects=self.allow_redirects)

	def fuzz_start(self,siteurl):
		for line in FileUtils.getLines(self.using_dic):
			line = siteurl.rstrip('/') + line
			try:
				result = self.dir_check(line)
				if result.status_code == requests.codes.ok or result.status_code == requests.codes.forbidden:
					self.dir_exists.append(line)
			except:
				continue
		return self.dir_exists


	



