#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pymongo import MongoClient

# 单利模式
def singleton(func):
    instances = {}
    def getinstance(*args, **kwargs):
        if func not in instances:
            instances[func] = func(*args, **kwargs)
        return instances[func]
    return getinstance


@singleton
class PymongoConnectWithFlaskApp(object):
    kwargs = {}
    connect = True
    host = 'localhost'
    port = 27017
    dbName = ''

    def __init__(self, app):
        if app.config['MONGO_HOST'] is not None:
            self.host = app.config['MONGO_HOST']

        if app.config['MONGO_PORT'] is not None:
            self.port = app.config['MONGO_PORT']

        if app.config['MONGO_CONNECT'] is not None:
            self.connect = app.config['MONGO_CONNECT']

        if app.config['MONGO_DBNAME'] is not None:
            self.dbName = app.config['MONGO_DBNAME']

        if app.config['MONGO_USERNAME'] is not None:
            self.kwargs['username'] = app.config['MONGO_USERNAME']

        if app.config['MONGO_PASSWORD'] is not None:
            self.kwargs['password'] = app.config['MONGO_PASSWORD']

        if app.config['MONGO_MAX_POOL_SIZE'] is not None:
            self.kwargs['maxPoolSize'] = app.config['MONGO_MAX_POOL_SIZE']

        if app.config['MONGO_MIN_POOL_SIZE'] is not None:
            self.kwargs['minPoolSize'] = app.config['MONGO_MIN_POOL_SIZE']

        if app.config['MONGO_MAX_IDLE_TIME_MS'] is not None:
            self.kwargs['maxIdleTimeMS'] = app.config['MONGO_MAX_IDLE_TIME_MS']

        if app.config['MONGO_SOCKET_TIMEOUT_MS'] is not None:
            self.kwargs['socketTimeoutMS'] = app.config['MONGO_SOCKET_TIMEOUT_MS']

        if app.config['MONGO_CONNECT_TIMEOUT_MS'] is not None:
            self.kwargs['connectTimeoutMS'] = app.config['MONGO_CONNECT_TIMEOUT_MS']

        if app.config['MONGO_SOCKET_KEEP_ALIVE'] is not None:
            self.kwargs['socketKeepAlive'] = app.config['MONGO_SOCKET_KEEP_ALIVE']

        if app.config['MONGO_REPLICA_SET'] is not None:
            self.kwargs['replicaSet'] = app.config['MONGO_REPLICA_SET']

    def getConnect(self):
        return MongoClient(host=self.host,port=self.port,document_class=dict,
                           tz_aware=None,connect=self.connect, **self.kwargs)

    def getDatabaseWithDBName(self):
        return self.getConnect()[self.dbName]
