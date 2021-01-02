# -*- coding: utf-8 -*-
import pymysql
db = pymysql.connect("localhost","root","123000","xWash")
# 使用cursor()方法获取操作游标
cursor = db.cursor()
sql = """select location,remainTime,status,belong,message from D19;"""
try:
    # 执行sql语句
    cursor.execute(sql)
    results = cursor.fetchall()
    print(results)
    for item in results:
        print(item)
except Exception :
    print(Exception)
    # 如果发生错误则回滚
    db.rollback()

# 关闭数据库连接
db.close()