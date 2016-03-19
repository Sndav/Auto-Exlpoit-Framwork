#!/usr/bin/env python
# -*- coding: utf-8 -*-
from auto_exp.config.config import config
from auto_exp.lib.core.database.core import D_Mysql

Config = config()
class DB(object):
	type_sub = 0
	type_path = 1
	type_file = 2
	db = D_Mysql(Config.MySQL_user,Config.MySQL_password,Config.MySQL_host,Config.MySQL_port,Config.MySQL_db)
	#def create_web_db(self,domain):
	#	if len(self.db.db_select('domain',['domain'],"domain='"+domain+"'")) == 0 :
	#		self.db.db_create_table(domain,Config.default_domain_table)
	#		self.db.db_insert('domain',{'domain':domain})
	#	else:
	#		pass
	#def insert_url(self,url,domain,type):
	#	if len(self.db.db_select(domain,['*'],"url='"+url+"'")) == 0:
	#		self.db.db_insert(domain,{'url':url,'type':type})
	#	else:
	#		pass
	#def get_url(self,domain,type):
	#	result = self.db.db_select(domain,['url'],"type='"+type+"'")
	#	url = []
	#	for each in result:
	#		url.append(each[0])
	#	return url
	def get_exp(self,where = '1=1'):
		result = self.db.db_select('exploit',['*'],where)
		return result
	def insert_exp(self,name,desc,level,author):
		data = {
			'name':"'"+str(name)+"'",
			'desc':"'"+str(desc)+"'",
			'level':str(level),
			'author':"'"+str(author)+"'"
		}
		if len(self.db.db_select('exploit',['*'],"name = '"+name+"'"))  == 0:
			self.db.db_insert('exploit',data)
		else:
			self.db.db_update('exploit',data,"name = '"+name+"'")
	def add_url(self,url,exp,info = ""):
		data = {
			'url':"'"+url+"'",
			'exp':"'"+exp+"'",
			'info':"'"+info+"'"
		}
		if len(self.db.db_select('url',['*'],"url = '"+url+"'"))  == 0:
			self.db.db_insert('url',data)
		else:
			self.db.db_update('url',data,"url ='"+url+"'")
	def get_exp_id(self,exp):
		return int(self.get_exp('name='+exp)[0][0])
	def del_exp(self,name):
		return self.db.db_delete('exploit',"name = '"+name+"'")
	#def show_url(self,exp):

if __name__ == "__main__":
	pass