#!/usr/bin/env python
# -*- coding: utf-8 -*-

from auto_exp.lib.core.output.output import O_Output
from auto_exp.lib.core.network.netjson import N_json
from auto_exp.lib.core.search.zoomeye.login import Zoo_login

class Zoo_function(object):
	output = O_Output()
	njson = N_json()
	def __init__(self,user,password):
		login = Zoo_login(user,password)
		token = login.get_token()
		try:
			tok = token["access_token"]
			self.token = tok
		except:
			self.output.print_error(token['message'])
	def host_search(self,query,page='1',facets=''):
		headers = {
			"Authorization": "JWT "+self.token
		}
		url = "http://api.zoomeye.org/host/search/?query=\""+query+"\"&page="+str(page)+"&facet="+facets
		res = self.njson.request(url,headers=headers,method="get")
		return  res
	def web_search(self,query,page='1',facets=''):
		headers = {
			"Authorization": "JWT "+self.token
		}
		url = "https://api.zoomeye.org/web/search\?query\=\""+query+"\"&page="+str(page)+"&facet="+facets
		res = self.njson.request(url,headers=headers,method="get")
		return  res

if __name__ == "__main__":
	pass
