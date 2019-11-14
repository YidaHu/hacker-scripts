#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/11/14 15:07
# @Author  : Huyida
# @Site    : 
# @File    : calculate_rpc_server.py
# @Software: PyCharm
# @Description:

from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCRequestHandler


def div(x, y):
    return x - y


class Math:
    def _listMethods(self):
        # this method must be present for system.listMethods
        # to work
        return ['add', 'pow']

    def _methodHelp(self, method):
        # this method must be present for system.methodHelp
        # to work
        if method == 'add':
            return "add(2,3) => 5"
        elif method == 'pow':
            return "pow(x, y[, z]) => number"
        else:
            # By convention, return empty
            # string if no help is available
            return ""

    def _dispatch(self, method, params):
        if method == 'pow':
            return pow(*params)
        elif method == 'add':
            return params[0] + params[1]
        else:
            raise Exception('bad method')


server = SimpleXMLRPCServer(("127.0.0.1", 8000))
server.register_introspection_functions()
server.register_function(div, "div")
server.register_function(lambda x, y: x * y, 'multiply')
server.register_instance(Math())
server.serve_forever()