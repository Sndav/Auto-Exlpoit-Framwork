#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re

from auto_exp.lib.core.finder.subdomain import S_Subscan
from auto_exp.config.config import config
from auto_exp.lib.core.finder.dirscan import S_Dirscan
from auto_exp.lib.core.finder.search_address import *

class Search(object):
	def __init__(self):
		self.config = config()
	def run_search_sub(self,domain):
		sub_search = S_Subscan(domain,self.config.path+self.config.default_dns_server)
		sub_search.run()
		return sub_search.result
	def run_scan_dir(self,path):
		dir_scan = S_Dirscan(self.config.path+self.config.default_web_dir)
		return dir_scan.fuzz_start(path)
	def run_bing(self,string,page):
		bing_scan = W_Bing()
		url = []
		for i in range(page):
			url += bing_scan.search(string,20,i+1)
		return url
	def run_shodan(self,string,page):
		shodan = W_Shodan(self.config.shodan_api)
		ip = []
		for i in range(page):
			ip += shodan.search(string,i+1)
		return ip
if __name__ == "__main__":
	pass