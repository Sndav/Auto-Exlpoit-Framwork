#!/usr/bin/env python
# -*- coding: utf-8 -*-

from bottle import *
from auto_exp.lib.core.output.output import O_Output
from auto_exp.lib.controller.db.db import *
from auto_exp.lib.core.network.api.dataprocess import *

debug(True)
db = DB()

@get("/show/exploit")
def show_exp():
	exploit = db.get_exp()
	exploit = list(exploit)
	for i in range(len(exploit)):
		exploit[i] = list(exploit[i])
		exploit[i][3] = get_level(exploit[i][3])
	return  dictojson(exploit)

@get("/show/status/:id")
def show_status(id):
	return "50"

@get("/show/tasks/")
def show_tasks():
	pass

@get("/run/new/:exp")
def run_new(exp):
	try:
		db.add_task(exp)
	except Exception ,e:
		print str(e)
	return "1"

@post("/add/exp")
def add_exp():
	text = request.forms.get("text")
	name = request.forms.get("name")
	pass

@post("/run/command")
def run_command():
	command = request.forms.get("command")
	pass

@get("/del/exp/:id")
def del_exp(id):
	pass

@post("/edit/exp")
def edit_exp():
	text = request.forms.get("text")
	name = request.forms.get("name")
	pass

@get("/test")
def test():
	return "test"



server_output = O_Output()

def create_server(host,port):
	try:
		run(host=host,port=int(port))
	except Exception,e:
		server_output.print_error("Unable to create server: "+str(e))
		return 1

if __name__ == "__main__":
	pass


