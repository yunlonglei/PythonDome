#!/usr/bin/python3

import pymysql

# 打开数据库连接 (数据库地址，用户名，库名)
conn = pymysql.connect(host='39.101.222.149', user='root', password='123mysql456', db='python_test' )

# 使用 cursor() 方法创建一个游标对象 cursor
cursor = conn.cursor()

# 使用 execute()  方法执行 SQL 查询
cursor.execute('SELECT * from userinfo')

# 使用 fetchone() 方法获取单条数据.
data = cursor.fetchone()

print("Database version : %s %s %s" % data)

# 关闭数据库连接
conn.close()
