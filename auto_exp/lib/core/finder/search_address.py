#!/usr/bin/env python
# -*- coding: utf-8 -*-

import shodan
import requests
import re
from auto_exp.lib.core.finder.zoomeye.main import Zoo_main

# Shodan Search
class W_Shodan(object):
	def __init__(self,api):
		self.api = api
		self.shodan = shodan.Shodan(self.api)
	def search(self,keywords,pages = 1):
		query = ' ' . join(keywords)
		result = self.shodan.search(query,pages)['matches']
		ip = []
		for addr in result:
			ip.append(addr['ip_str'])
		return ip

# Bing Search
class W_Bing(object):
	def search(self,keywords,count,pages = 1):
		count = count
		page = int(pages)
		query=keywords.replace(' ','+')
		url = []

		res = requests.get('http://www.bing.com/search?q='+query+'&count='+str(count)+"&first="+str((page-1)*int(count)+1))
		match = re.findall(r'\<li class="b_algo"\>\<h2\>\<a href=\"(.*?)\" target="_blank"', res.content)
		for val in match:
				url.append(val)
		return url
class W_Zoomeye(Zoo_main):
	pass





