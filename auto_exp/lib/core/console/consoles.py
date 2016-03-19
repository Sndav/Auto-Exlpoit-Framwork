#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
from cmd import Cmd
import readline
from auto_exp.lib.method.switch.switch import switch
from auto_exp.lib.core.exploit.load_exp import exp
from auto_exp.lib.method.output.CLIOutput import CLIOutput
from auto_exp.lib.core.output.output import O_Output
from auto_exp.lib.controller.db.db import DB
from auto_exp.lib.core.file.file import IO_File
from auto_exp.config.config import config

class C_Base(Cmd):
	def __init__(self):
		self.config = config()
		self.db = DB()
		self.output = CLIOutput()
		self.output2 = O_Output()
		self.exp = exp()
		Cmd.__init__(self)
		os.system("clear")
		self.case_insensitive = False
		self.prompt = self.config.default_console_words
		self.isused = False
		self.file =IO_File()
	def do_help(self, arg):
		if not arg :
			self.output.printYellow("[Command]")
			print "    use [exp]                    : use exploit"
			print "    show exploit                 : show the info of exploit"
			print "    del [exp]                    : del exploit"
			self.output.printYellow("[System]")
			print "    exit                         : exit the system"
			self.output.printYellow("[Exploit]")
			print "    run exploit                  : run exploit"
			self.output.printYellow("[Help]")
			print "    help [command]               : show help"
		else:
			self.__do_ls(arg)
	def __do_ls(self,arg):
		if not arg:
			for case in switch(arg):
				if case("use"):
					self.output.printYellow("[Command]")
					print "    use [exp]           : use exploit"
					break
				if case("show"):
					self.output.printYellow("[Command]")
					print "    show exploit        : show the info of exp"
					break
				if case("exit"):
					self.output.printYellow("[System]")
					print "    exit                : exit the system"
					break
				if case("del"):
					self.output.printYellow("[Command]")
					print "    del [exp]           : del exploit"
					break
		#else:
			#self.do_help()
	def do_use(self,arg):
		if arg:
			try:
				exploit = self.exp.load_exp(arg)
				self.exploit = exploit
				self.exploit.print_desc()
				self.isused = True
			except:
				self.output2.print_error('Failed to load exploit')
	def do_show(self,arg):
		if not arg:
			pass
		elif arg == 'exp' or arg == 'exploit':
			self.case_insensitive = True
			exploit = self.db.get_exp()
			name = ['id','name','desc','level','author']
			exploit = list(exploit)
			for i in range(len(exploit)):
				exploit[i] = list(exploit[i])
				exploit[i][3] = self.__get_level(exploit[i][3])
			self.output2.print_form(name,exploit)
	def do_run(self,arg):
		if arg == 'exploit':
			if self.isused:
				self.exploit.run()
			else:
				self.output2.print_warning('Please Use an Exploit')
	def do_load(self,arg):
		if not arg:
			pass
		else:
			if self.file.check_file(self.config.path+'exploit/'+arg+'.py'):
				exp = self.exp.load_exp(arg)
				if arg == exp.info['Name']:
					self.db.insert_exp(exp.info['Name'],exp.info['Desc'],exp.info['Level'],exp.info['Author'])
				else:
					self.output2.print_error("Exploit Name != File Name")
			else :
				self.output2.print_error('Please Move You Exploit To /exploit')
	def do_del(self,arg):
		self.db.del_exp(arg)
	def do_exit(self,arg):
		quit()
	def __get_level(self,level):
		a = ['low','medium','high']
		return a[level]
	def default(self, line):
		pass
	def emptyline(self):
		self.default('')
if __name__ == "__main__":
	pass
