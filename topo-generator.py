#!/usr/local/bin/python3
# -*- coding: UTF-8 -*-
import pymysql

db = pymysql.connect("172.20.0.10",
    "root",
    "zstack.mysql.password",
    "zstack" )
cursor = db.cursor()
cursor.execute("SELECT VERSION()")
print("Mysql Version: ", cursor.fetchone())

# Management node
cursor.execute("select uuid,hostName from ManagementNodeVO")
print("Management Nodes: ", list(cursor.fetchall()))

# Zone
cursor.execute("select uuid,name,type from ZoneEO")
print("Zones: ", list(cursor.fetchall()))

# Cluster
cursor.execute("select uuid,zoneUuid,name from ClusterEO")
print("Compute Nodes: ", list(cursor.fetchall()))

# Compute node
cursor.execute("select uuid,managementIp from HostEO")
print("Compute Nodes: ", list(cursor.fetchall()))

# Storage type

# Storage node

# Storage pool

db.close()