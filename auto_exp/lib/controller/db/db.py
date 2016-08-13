#!/usr/bin/env python
# -*- coding: utf-8 -*-
from auto_exp.config.config import config
from auto_exp.lib.core.database.core import D_Mysql
import time
ISOTIMEFORMAT = '%Y%m%d'

Config = config()


class DB(object):
    type_sub = 0
    type_path = 1
    type_file = 2
    db = D_Mysql(Config.MySQL_user, Config.MySQL_password,
                 Config.MySQL_host, Config.MySQL_port, Config.MySQL_db)

    def get_exp(self, where='1=1'):
        result = self.db.db_select('exploit', ['*'], where)
        return result

    def insert_exp(self, name, desc, level, author):
        data = {
            'name': "'" + str(name) + "'",
            'desc': "'" + str(desc) + "'",
            'level': str(level),
            'author': "'" + str(author) + "'"
        }
        if len(self.db.db_select('exploit', ['*'], "name = '" + name + "'")) == 0:
            self.db.db_insert('exploit', data)
        else:
            self.db.db_update('exploit', data, "name = '" + name + "'")

    def add_url(self, url, exp, info=""):
        data = {
            'url': "'" + url + "'",
            'exp': "'" + exp + "'",
            'info': "'" + info + "'"
        }
        if len(self.db.db_select('url', ['*'], "url = '" + url + "'")) == 0:
            self.db.db_insert('url', data)
        else:
            self.db.db_update('url', data, "url ='" + url + "'")

    def get_exp_id(self, exp):
        return int(self.get_exp('name=' + exp)[0][0])

    def del_exp(self, name):
        return self.db.db_delete('exploit', "name = '" + name + "'")

    def add_task(self, exp):
        data = {
            'exp': "'" + exp + "'",
            'starttime': "'" + time.strftime(ISOTIMEFORMAT, time.localtime()) + "'",
        }
        self.db.db_insert("tasks", data)

    def update_task(self, id, status):
        data = {
            'status': int(status)
        }
        self.db.db_update("tasks", data, "id =" + str(id))

    def get_task(self, id):
        return self.db.db_select("tasks", ['id'], "id =" + str(id))[0][0]
    # def show_url(self,exp):

if __name__ == "__main__":
    pass
