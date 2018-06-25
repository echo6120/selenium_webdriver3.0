#encoding=utf-8
import MySQLdb
from Sql import *

class DataBaseInit(object):
    # 本类用于完成初始化数据操作
    # 创建数据库，创建数据表，向表中插入测试数据
    def __init__(self, host, port, dbName, username,charset):
        self.host = host
        self.port = port
        self.db = dbName
        self.user = username
        self.charset = charset

    def create(self):
        try:
            # 连接mysql数据库
            conn = MySQLdb.connect(
                host = self.host,
                port = self.port,
                user = self.user,
                charset = self.charset
            )
            # 获取数据库游标
            cur = conn.cursor()
            # 创建数据库
            cur.execute(create_database)
            # 选择创建好的ketest数据库
            conn.select_db("ketest")
            # 创建测试表
            cur.execute(create_table)
        except MySQLdb.Error, e:
            raise e
        else:
            # 关闭游标
            cur.close()
            # 提交操作
            conn.commit()
            # 关闭连接
            conn.close()
            print u"创建数据库及表成功"

    def insertDatas(self):
        try:
            # 连接mysql数据库中具体某个库
            conn = MySQLdb.connect(
                host = self.host,
                port = self.port,
                db = self.db,
                user = self.user,
                charset = self.charset
            )
            cur = conn.cursor()
            # 向测试表中插入测试数据
            sql = "insert into testdata(kename, teacher) values(%s, %s);"
            res = cur.executemany(sql, [('一个暑假提升你的四六级听力', '剑昆'),
                                  ('忘词王是怎样炼成的', '曲根'),
                                  ('四六级', '欧阳萍'),
                                  ('杨老师', 'so cool')])
        except MySQLdb.Error, e:
            raise e
        else:
            conn.commit()
            print u"初始数据插入成功"
            # 确认插入数据成功
            cur.execute("select * from testdata;")
            for i in cur.fetchall():
                print i[1], i[2]
            cur.close()
            conn.close()


if __name__ == '__main__':
    db = DataBaseInit(
        host="localhost",
        port=3306,
        dbName="ketest",
        username="root",
        charset="utf8"
    )
    db.create()
    db.insertDatas()
    print u"数据库初始化结束"
