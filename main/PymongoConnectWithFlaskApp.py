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
    """
    # 链接的数据库的地址
    # (host)
    MONGO_HOST = '127.0.0.1'
    # 数据库主机的端口
    # (port)
    MONGO_PORT = 27017
    # 用户名（可以为空）
    # (username)
    MONGO_USERNAME = None
    # 用户的密码
    # (password)
    MONGO_PASSWORD = None
    # 用户要链接的数据库
    # （dbName）
    MONGO_DBNAME = 'test'
    # 是否使用懒加载的方式，当有数据库操作的时候才链接，默认是（true）直接链接（非懒加载形式）
    # (connect)
    MONGO_CONNECT = True
    # 每个连接服务器的并发连接的最大允许数量。
    # 如果有maxPoolSize个与所请求的服务器的连接的未关闭，那么对服务器的请求将会阻塞。默认为100。不能是0。
    # (maxPoolSize)
    MONGO_MAX_POOL_SIZE = 100
    # 最小的数据库链接数,默认是0
    # (minPoolSize)
    MONGO_MIN_POOL_SIZE = 0
    # 在被删除和替换之前，连接可以在池中保持空闲的最大毫秒数。默认设置为None(没有限制)。
    # (maxIdleTimeMS)
    MONGO_MAX_IDLE_TIME_MS = None
    # 驱动程序等待响应的时间(以毫秒为单位)，默认为None(没有超时)。
    # (socketTimeoutMS)
    MONGO_SOCKET_TIMEOUT_MS = None
    # 链接超时时间(以毫秒为单位), 默认为20s
    #(connectTimeoutMS)
    MONGO_CONNECT_TIMEOUT_MS = 20000
    # 是否保持链接 keep-alive , 默认为 FALSE
    # (socketKeepAlive)
    MONGO_SOCKET_KEEP_ALIVE = False
    # (字符串或None)用于连接的复制集的名称。驱动程序将验证它连接的所有服务器是否匹配这个名称。
    # 意味着指定的主机是一个种子列表，驱动程序应该尝试查找集合中的所有成员。默认情况下没有任何一个。
    # （replicaSet）
    MONGO_REPLICA_SET = None
    # readPreference :表示读优先级设置参数可选项：
    # PRIMARY （默认 只读主库），PRIMARY_PREFERRED（主库优先），
    # SECONDARY（只读从库），SECONDARY_PREFERRED（从库优先），NEAREST（就近优先）[注意都用小写]
    # 详情查看 pymongo.read_preferences 
    # (read_preferences)
    MONGO_READ_PREFERENCE
    """
    kwargs = {}
    connect = True
    host = 'localhost'
    port = 27017
    dbName = ''
    username = None
    password = None

    def __init__(self, app):
        if app.config.get('MONGO_HOST') is not None:
            self.host = app.config['MONGO_HOST']

        if app.config.get('MONGO_PORT') is not None:
            self.port = app.config['MONGO_PORT']

        if app.config.get('MONGO_CONNECT') is not None:
            self.connect = app.config['MONGO_CONNECT']

        if app.config.get('MONGO_DBNAME') is not None:
            self.dbName = app.config['MONGO_DBNAME']

        if app.config.get('MONGO_USERNAME') is not None:
            self.username = app.config['MONGO_USERNAME']

        if app.config.get('MONGO_PASSWORD') is not None:
            self.password = app.config['MONGO_PASSWORD']

        if app.config.get('MONGO_MAX_POOL_SIZE') is not None:
            self.kwargs['maxPoolSize'] = app.config['MONGO_MAX_POOL_SIZE']

        if app.config.get('MONGO_MIN_POOL_SIZE') is not None:
            self.kwargs['minPoolSize'] = app.config['MONGO_MIN_POOL_SIZE']

        if app.config.get('MONGO_MAX_IDLE_TIME_MS') is not None:
            self.kwargs['maxIdleTimeMS'] = app.config['MONGO_MAX_IDLE_TIME_MS']

        if app.config.get('MONGO_SOCKET_TIMEOUT_MS') is not None:
            self.kwargs['socketTimeoutMS'] = app.config['MONGO_SOCKET_TIMEOUT_MS']

        if app.config.get('MONGO_CONNECT_TIMEOUT_MS') is not None:
            self.kwargs['connectTimeoutMS'] = app.config['MONGO_CONNECT_TIMEOUT_MS']

        if app.config.get('MONGO_SOCKET_KEEP_ALIVE') is not None:
            self.kwargs['socketKeepAlive'] = app.config['MONGO_SOCKET_KEEP_ALIVE']

        if app.config.get('MONGO_REPLICA_SET') is not None:
            self.kwargs['replicaSet'] = app.config['MONGO_REPLICA_SET']

        if app.config.get('MONGO_READ_PREFERENCE') is not None:
            self.kwargs['read_preference'] = app.config['MONGO_READ_PREFERENCE']

    def getConnect(self):
        return MongoClient(host=self.getHost(),port=self.port,document_class=dict,
                           tz_aware=None,connect=self.connect, **self.kwargs)

    def getDatabaseWithDBName(self):
        return self.getConnect()[self.dbName]

    def getHost(self):
        if self.username is not None and self.password is not None:
            return 'mongodb://%s:%s@%s' % (self.username, self.password, self.host)
        return self.host
