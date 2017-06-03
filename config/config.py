#!/usr/bin/env python
# -*- coding: utf-8 -*-

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
