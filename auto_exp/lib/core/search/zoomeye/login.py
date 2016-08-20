#!/usr/bin/env python
# -*- coding: utf-8 -*-

from auto_exp.lib.core.network.netjson import N_json


class Zoo_login():
    net = N_json()

    def __init__(self, user, password):
        self.dic = {
            "username": user,
            "password": password
        }

    def get_token(self):
        response = self.net.request(
            "https://api.zoomeye.org/user/login", self.dic)
        print response
        return response
if __name__ == "__main__":
    pass
