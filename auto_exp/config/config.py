#!/usr/bin/env python
# -*- coding: utf-8 -*-


class config(object):
	def __init__(self):
		self.path = "/home/ubuntu/Code/Auto-Exp/"
		self.default_console_words = "AEF>"
		self.phone_pattern = r"([133|155|139|151|189|187][1-9]{10})"
		self.email_pattren = r"(\w+@\w+.\w+)"
		self.MySQL_user = 'root'
		self.MySQL_password = 'root'
		self.MySQL_host = '127.0.0.1'
		self.MySQL_port = 3306
		self.MySQL_db = 'auto_exp'
		self.filter = ["'","#",'-','%']
		self.default_domain_table = {
			'id' : 'int(4) not null primary key auto_increment',
			'url' : 'char(100) not null',
			'type' : 'int(2) not null'
		}
		self.default_dns_server = 'auto_exp/dic/dns_servers.txt'
		self.default_web_dir = 'auto_exp/webaddr.dic'
		self.shodan_api = 'iugjvSn7YGEikIrSDzgw3XBkI3RVYxG5'

