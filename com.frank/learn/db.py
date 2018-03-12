#!/usr/bin/env python3
# coding: utf-8

import pymysql

connect = pymysql.connect('192.168.31.22', 'root', 'look', 'mydb')
cursor = connect.cursor()
cursor.execute("select version()")
fetchone = cursor.fetchone()
print("fetchone=",fetchone)

cursor.execute("select * from user_info where id = 1")
fetchone = cursor.fetchone()
print("user_info one=",fetchone)
