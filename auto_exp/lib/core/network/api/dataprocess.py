#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

def get_level(level):
	a = ['low', 'medium', 'high']
	return a[level]

def dictojson(dic):
	return json.dumps(dic)
if __name__ == "__main__":
	pass

