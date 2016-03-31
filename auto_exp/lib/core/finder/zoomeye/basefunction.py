#!/usr/bin/env python
# -*- coding: utf-8 -*-

from auto_exp.lib.core.finder.zoomeye.login import Zoo_login
from auto_exp.lib.core.output.output import O_Output

class Zoo_function(object):
	output = O_Output
	def __init__(self,user,password):
		login = Zoo_login(user,password)
		token = login.get_token()
		try:
			tok = token["access_token"]
			self.token = tok
		except:
			self.output.print_error(token['message'])
	def search(self,quert):
		pass
if __name__ == "__main__":
	pass