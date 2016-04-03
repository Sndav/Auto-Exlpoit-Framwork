#!/usr/bin/env python
# -*- coding: utf-8 -*-

import auto_exp.config.config as config
import re

class S_InfoScan(object):
	def __init__(self,content):
		self.content = content
		self.config = config.config()
	def phone_scan(self):
		self.phone_match = re.findall(self.config.phone_pattern,self.content)
		return phone_match
	def email_scan(self):
		self_email_match = re.findall(self.config.email_pattren,self.content)
		return email_match
if __name__ == "__main__":
	pass