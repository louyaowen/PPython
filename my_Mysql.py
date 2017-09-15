# -*- coding:utf-8 -*-
# 数据库处理

import pymysql
import sys, io
import json

#! 设置输出编码utf-8
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')


mysql_config = {'host':'127.0.0.1',
                'port':3306,
                'user':'root',
                'password':'root',
                'db':'ncist',
                'charset':'utf8'
                #'cursorclass':'pymysql.cursors.DictCursor'
                }
conn = pymysql.connect(**mysql_config)

with conn.cursor(pymysql.cursors.DictCursor) as cursor:
    cursor.execute("select * from tieba")
    
    for row in cursor.fetchall():
        row['images'] = json.loads(row['images'])
        print(row)
