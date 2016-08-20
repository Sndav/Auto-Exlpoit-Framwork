#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os


class IO_File(object):

    def __init__(self):
        pass

    def read(self, path):
        if self.check_file(path):
            self.create_file(path)
        file_open = open(path, 'r')
        try:
            text = file_open.readlines()
        finally:
            file_open.close()
        return text

    def write(self, path, text):
        if self.check_file(path):
            self.create_file(path)
        file_open = open(path, "w")
        try:
            if file_open.write(text + '\n'):
                return True
        finally:
            file_open.close()
        return False

    def create_file(path):
        open(path, 'w+')

    def check_file(self, path):
        if os.path.isfile(path):
            return True
        else:
            return False
