# -*- coding: utf-8 -*-
"""
Created on Mon Nov  6 19:42:06 2023

@author: USER
"""

import MySQLdb

conn = MySQLdb.connect(host='localhost',user='root',passwd='1234567890',db='stock',port=3306)
cursor = conn.cursor()

