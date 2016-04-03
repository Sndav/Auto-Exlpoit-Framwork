#!/usr/bin/env python
# -*- coding: utf-8 -*-

class  Search_SearchEngine():
	def __init__(self,site="W_shodan"):
		self.site = site
	def Search(self):
		class_name  =  "auto_exp.lib.core.search.search_address."+self.site
		self.search_class =  eval(class_name)
		return self.search_class
