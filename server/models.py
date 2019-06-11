"""
服务端 模型层

与数据库进行交互
"""

import pymysql

class DBManager:
    """数据库管理对象"""
    def __init__(self):
        self.db = pymysql.connect('localhost', 'root', '123456', 'pytalk', charset='utf8') # 连接数据库
        self.cursor = self.db.cursor() # 创建游标