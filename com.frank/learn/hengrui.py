#!/usr/bin/env python
# coding=utf-8
import configparser
import getopt
import random
import sys
import dateutils
import pymysql
import uuid
import math
import decimal
import datetime
import lxml
import pandas
import requests
import bs4
import openpyxl
import xlwt
#import MySQLdb
#import mysqlclient
#from sqlalchemy import create_engine
import tushare as ts
#import backports.functools-lru-cache
import cycler
import matplotlib

import six








def test():
    phone_num = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    str = "".join(random.choice(phone_num) for i in range(3))

    return str;


# def importSql():
#     df = ts.get_stock_basics()
#     engine = create_engine('mysql://root:look@192.168.31.22:3306/mydb?charset=utf8')
#
#     # 存入数据库
#     df.to_sql('benefit', engine)
#     return "SUCC";
#

def res():
    df = ts.get_stock_basics()
    return df;

def excelres():
    df = ts.get_stock_basics()
   # print(df)
    df.to_excel('D:/test2.xlsx')
    return "succ"

def benefit():
    ts.set_token('feca4dcb1241d2564ff37534a9f509705a5154664ff39364849639145ab9f1b3')
    bd = ts.Fundamental()
    df = bd.FdmtIS(ticker='600276', publishDateBegin='20100101',beginDate='20100101',field='ticker,reportType,fiscalPeriod,bizTaxSurchg,finanExp')
    print(df)
    df.to_excel('D:/test.xls')
    return "succ"


#print(test())
#print(ts.__version__)
#print(res())
#print(excelres)
#print(importSql2())

print(benefit())