#!/usr/local/bin/python3
# -*- coding: UTF-8 -*-
import pymysql

db = pymysql.connect("172.20.1.11",
    "root",
    "zstack.mysql.password",
    "zstack" )
cursor = db.cursor()
cursor.execute("SELECT VERSION()")
print(cursor.fetchone())

# Management node
cursor.execute("select hostName from ManagementNodeVO")
print(list(cursor.fetchall())[0])

# Compute node
cursor.execute("select managementIp from HostEO")
print(list(cursor.fetchall())[0])

# Storage type

# Storage node

# Storage pool

db.close()