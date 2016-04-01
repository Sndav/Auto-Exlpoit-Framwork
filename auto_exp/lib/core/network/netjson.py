#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import requests

class N_json(object):
	def request(self,url,dic,header = ""):
		j = json.dumps(dic)
		res = requests.post(url,j,header=dic(header))
		res = res.text
		j = json.loads(res)
		return j

if __name__ == "__main__":
	pass