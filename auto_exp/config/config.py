#!/usr/bin/env python
# -*- coding: utf-8 -*-


class config(object):

    def __init__(self):
        self.path = "E://code//Auto-Exploit-Framework//"
        self.default_console_words = "AEF>"
        self.phone_pattern = r"([133|155|139|151|189|187][1-9]{10})"
        self.email_pattren = r"(\w+@\w+.\w+)"
        self.MySQL_user = 'root'
        self.MySQL_password = ''
        self.MySQL_host = ''
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
        self.shodan_api = ''
        self.zoom_user = ''
        self.zoom_password = ''
        self.host = '127.0.0.1'
        self.api_port = 8090
        self.logo = "    _         _              _____            \n" + \
            "   / \  _   _| |_ ___       | ____|_  ___ __  \n" + \
            "  / _ \| | | | __/ _ \ _____|  _| \ \/ / '_ \ \n" + \
            " / ___ \ |_| | || (_) |_____| |___ >  <| |_) |\n" + \
            "/_/   \_\__,_|\__\___/      |_____/_/\_\ .__/ \n" + \
            "                                       |_|    \n"
