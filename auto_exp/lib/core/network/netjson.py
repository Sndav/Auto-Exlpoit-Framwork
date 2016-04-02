#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import requests

class N_json(object):
	def request(self, url, dic=None, headers=None,method = "post"):
		if method == "post":
			if dic is None:
				dic = {}
			if headers is None:
				headers = {}
			j = json.dumps(dic)
			res = requests.post(url,j,headers=headers)
			print res.text
			res = res.json()
			return res
		else :
			if method == "get":
				res = requests.get(url,headers=headers)
				print res.text
				res = res.json()
				return res


if __name__ == "__main__":
	pass

