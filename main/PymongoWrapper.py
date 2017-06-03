#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
from pymongo import MongoClient
from gevent import sleep

import config.config as config

# 单利模式
def singleton(func):
    instances = {}
    def getinstance(*args, **kwargs):
        if func not in instances:
            instances[func] = func(*args, **kwargs)
        return instances[func]
    return getinstance


@singleton
class PymongoWrapper(object):
    kwargs = {}
    connect = True
    host = 'localhost'
    port = 27017
    dbName = ''

    def __init__(self):
        if config.MONGO_HOST is not None:
            self.host = config.MONGO_HOST

        if config.MONGO_PORT is not None:
            self.port = config.MONGO_PORT

        if config.MONGO_CONNECT is not None:
            self.connect = config.MONGO_CONNECT

        if config.MONGO_DBNAME is not None:
            self.dbName = config.MONGO_DBNAME

        if config.MONGO_USERNAME is not None:
            self.kwargs['username'] = config.MONGO_USERNAME

        if config.MONGO_PASSWORD is not None:
            self.kwargs['password'] = config.MONGO_PASSWORD

        if config.MONGO_MAX_POOL_SIZE is not None:
            self.kwargs['maxPoolSize'] = config.MONGO_MAX_POOL_SIZE

        if config.MONGO_MIN_POOL_SIZE is not None:
            self.kwargs['minPoolSize'] = config.MONGO_MIN_POOL_SIZE

        if config.MONGO_MAX_IDLE_TIME_MS is not None:
            self.kwargs['maxIdleTimeMS'] = config.MONGO_MAX_IDLE_TIME_MS

        if config.MONGO_SOCKET_TIMEOUT_MS is not None:
            self.kwargs['socketTimeoutMS'] = config.MONGO_SOCKET_TIMEOUT_MS

        if config.MONGO_CONNECT_TIMEOUT_MS is not None:
            self.kwargs['connectTimeoutMS'] = config.MONGO_CONNECT_TIMEOUT_MS

        if config.MONGO_SOCKET_KEEP_ALIVE is not None:
            self.kwargs['socketKeepAlive'] = config.MONGO_SOCKET_KEEP_ALIVE

        if config.MONGO_REPLICA_SET is not None:
            self.kwargs['replicaSet'] = config.MONGO_REPLICA_SET

    def getConnect(self):
        return MongoClient(host=self.host,port=self.port,document_class=dict,
                           tz_aware=None,connect=self.connect, **self.kwargs)

    def getDatabaseWithDBName(self):
        return self.getConnect()[self.dbName]


# class MyTestCase(unittest.TestCase):
#
#     # def test_something(self):
#         # self.assertEqual(True, False)
#
#     def test_Message(self):
#         db = PymongoWrapper().getDatabaseWithDBName()
#         message = db.data.find_one({})
#         print message
#         self.assertEqual(message is not None, True)

if __name__ == '__main__':
    # unittest.main()

    for i in xrange(100000):
        db = PymongoWrapper().getDatabaseWithDBName()
        message = db.data.find_one({})
        print (" {0} {1}".format(i,message.get('data')))
        sleep(0.01)

    # client = MongoClient('127.0.0.1', 27017, dict, None, True)['test']
    # print client.data.find_one({})
