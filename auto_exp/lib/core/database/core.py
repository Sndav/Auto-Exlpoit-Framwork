#!/usr/bin/env python
# -*- coding: utf-8 -*-
import MySQLdb
from auto_exp.lib.core.output.output import O_Output
from auto_exp.config.config import config


class D_Mysql(object):

    def __init__(self, user, password, host, port, db):
        self.__output = O_Output()
        self.__user = user
        self.__password = password
        self.__host = host
        self.__port = port
        self.__db = db
        self.__isconnected = True
        try:
            self.__conn = MySQLdb.connect(
                host=self.__host,
                user=self.__user,
                passwd=self.__password,
                port=self.__port,
                db=self.__db,
            )
            self.__cur = self.__conn.cursor()
        except MySQLdb.Error, e:
            self.__output.print_error(
                "MySQL Error " + e.args[0] + ':' + e.args[1])
            self.__isconnected = False

    def db_stop(self):
        if self.__isconnected:
            self.__cur.close()
            self.__conn.close()
        else:
            self.__output.print_warning(
                "You have not connected to MySQL Database")

    def db_query(self, query):
        if self.__isconnected:
            try:
                self.__cur.execute(query)
            except MySQLdb.Error, e:
                self.__output.print_error(
                    "MySQL Error " + str(e.args[0]) + ":" + str(e.args[1]))
            return self.__cur.fetchall()
        else:
            self.__output.print_warning(
                "You have not connected to MySQL Database")

    def db_execute(self, query):
        if self.__isconnected:
            # self.__rebuild()
            bool = True
            try:
                self.__cur.execute(query)
                self.__conn.commit()
            except MySQLdb.Error, e:
                self.__output.print_error(
                    "MySQL Error " + str(e.args[0]) + ":" + str(e.args[1]))
                bool = False
            return bool
        else:
            self.__output.print_warning(
                "You have not connected to MySQL Database")

    def db_insert(self, table, data):
        if self.__isconnected:
            name = []
            value = []
            for key in data:
                name.append('`' + key + '`')
                value.append(data[key])
            query = 'insert into `' + table + \
                '` (' + ','.join(name) + ') values (' + ','.join(value) + ')'
            return self.db_execute(query)
        else:
            self.__output.print_warning(
                "You have not connected to MySQL Database")

    def db_delete(self, table, where='1=2'):
        if self.__isconnected:
            query = 'delete from `' + table + '` where ' + where
            return self.db_execute(query)
        else:
            self.__output.print_warning(
                "You have not connected to MySQL Database")

    def db_update(self, table, data, where='1=2'):
        if self.__isconnected:
            set = []
            for key in data:
                set.append('`' + key + '`=' + data[key])
            # print ','.join(set)
            query = 'update `' + table + '` set ' + \
                ','.join(set) + ' where ' + where
            return self.db_execute(query)
        else:
            self.__output.print_warning(
                "You have not connected to MySQL Database")

    def db_select(self, table, key, where):
        if self.__isconnected:
            if len(key) == 0:
                value = ['*']
            else:
                value = ','.join(key)
            query = 'select ' + value + ' from `' + table + '` where ' + where
            return self.db_query(query)
        else:
            self.__output.print_warning(
                "You have not connected to MySQL Database")

    def db_create_table(self, table, data):
        string = []
        for key in data:
            string.append('`' + key + '` ' + data[key])
        query = 'create table `' + table + '` (' + ','.join(string) + ')'
        return self.db_execute(query)

    def db_filter(self, string):
        pass
if __name__ == "__main__":
    pass
