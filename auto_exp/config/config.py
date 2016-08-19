#!/usr/bin/env python
# -*- coding: utf-8 -*-


class config(object):

    def __init__(self):
        self.path = "/home/hackboy/code/Auto-Exp/"
        self.default_console_words = "AEF>"
        self.phone_pattern = r"([133|155|139|151|189|187][1-9]{10})"
        self.email_pattren = r"(\w+@\w+.\w+)"
        self.MySQL_user = 'root'
        self.MySQL_password = 'root'
        self.MySQL_host = '127.0.0.1'
        self.MySQL_port = 3306
        self.MySQL_db = 'auto_exp'
        self.filter = ["'", "#", '-', '%']
        self.default_domain_table = {
            'id': 'int(4) not null primary key auto_increment',
            'url': 'char(100) not null',
            'type': 'int(2) not null'
        }
        self.default_dns_server = 'auto_exp/dic/dns_servers.txt'
        self.default_web_dir = 'auto_exp/dic/webaddr.dic'
        self.default_subdomainfix = 'auto_exp/dic/subnames.txt'
        self.default_next_sub = 'auto_exp/dic/next_sub.txt'
        self.shodan_api = 'iugjvSn7YGEikIrSDzgw3XBkI3RVYxG5'
        self.zoom_user = 'bossstyle@126.com'
        self.zoom_password = 'wzzj123'
        self.host = '127.0.0.1'
        self.api_port = 8090
