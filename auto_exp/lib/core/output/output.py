#!/usr/bin/env python
# -*- coding: utf-8 -*-

from auto_exp.lib.method.output.CLIOutput import CLIOutput

class O_Output(object):
	___output  = CLIOutput()
	def print_error(self,content):
		self.___output.printError('[!] ' + content)
	def print_warning(self,content):
		self.___output.printWarning('[*] ' + content)
	def print_default(self,content):
		self.___output.printNewLine('[+] ' + content)
	def print_form(self,name,value):

		max_line = []
		max_len = 0
		all = []
		all.append(name)
		all += value
		for i in name:
			max_len += len(i)
			max_line.append(len(i))
		for j in range(len(value)):
			leng = 0
			for i in range(len(value[j])):
				leng += len(str(value[j][i]))
				if max_line[i] < len(str(value[j][i])):
					max_line[i] = len(str(value[j][i]))
			if leng > max_len:
				max_len = leng
		line = len(value)
		basic = '+'
		for i in range(len(name)):
			basic += '-'*max_line[i]
			basic += '+'
		for i in range(len(all)):
			print basic
			self.___output.printInLine('|')
			all[i] = list(all[i])
			for j in range(len(name)):
				all[i][j] = str(all[i][j]).ljust(max_line[j])
			print '|'.join(all[i])+'|'
		print basic
if __name__ == "__main__":
	pass
