#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import requests

class Zoo_login(object):
	def __init__(self,user,passd):
		self.dic = {
			"username":user,
			"password":passd
		}
		self.dic = json.dumps(self.dic)
	def get_token(self):
		res = requests.post("http://api.zoomeye.org/user/login",data = self.dic)
		res = res.text
		json_t = json.loads(res)
		return json_t

if __name__ == "__main__":
	pass