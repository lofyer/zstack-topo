#!/usr/local/bin/python3
# -*- coding: UTF-8 -*-
import pymysql

db = pymysql.connect("172.32.1.11",
    "root",
    "zstack.mysql.password",
    "zstack" )
cursor = db.cursor()
cursor.execute("SELECT VERSION()")
print("MySQLVersion: ", cursor.fetchone())

# Management node
cursor.execute("select uuid,hostName from ManagementNodeVO")
print("Management Nodes:\n", list(cursor.fetchall()))

# Zone
cursor.execute("select uuid,name,type from ZoneEO where deleted is null")
print("Zones:\n", list(cursor.fetchall()))

# Cluster
cursor.execute("select uuid,zoneUuid,name from ClusterEO where deleted is null")
print("Cluster:\n", list(cursor.fetchall()))

# Compute node
cursor.execute("select uuid,managementIp from HostEO where deleted is null")
print("Compute Nodes\n", list(cursor.fetchall()))

# Storage pool
cursor.execute('select uuid,zoneUuid,name,type from PrimaryStorageEO where deleted is null')
print("Storage Pool:\n", list(cursor.fetchall()))


db.close()
