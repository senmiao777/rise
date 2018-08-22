#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import requests
import json
import pymysql
import re
import time
from datetime import datetime
def send(order_no, term, _type):
    head = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'
    }
    ##post发送的数据

    postData = {
        'orderNo': order_no,
        'useage': 3
    }

    _url="http://www.b"
    response = requests.post(url=_url, headers=head, data=postData)
    json_result = json.loads(response.text)
    print("response code =", json_result.get('code'))
    return json_result.get('code')


def read_txt():
    with open(file="E:/test2.txt", mode="r", encoding="utf-8") as f:
        # 为a+模式时，因为为追加模式，指针已经移到文尾，读出来的是一个空字符串。
        #   ftext = f.read()  # 一次性读全部成一个字符串
        ftextlist = f.readlines()  # 也是一次性读全部，但每一行作为一个子句存入一个列表
        lines = len(ftextlist)
        print("lines =", lines)
        for i in range(lines):
            split = ftextlist[i].split(",")
            _id = split[0]
            term = split[1]
            print("split[0] = ", _id)
            print("split[1] = ", term)
            send_result = send(_id.strip(), term.strip(), '123')
            time.sleep(0.1)
    return 0

def send(stock_code):
    head = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'
    }
    ##post发送的数据

    _data = {
        'stockCode': stock_code
    }

    #_url = "http://localhost:8080/t/stock/info2"
    _url = "http://learn.com/t/stock/info2"
    response = requests.get(url=_url, headers=head, params=_data)
    json_result = json.loads(response.text)
    print("response data =", json_result.get('data'))
    return json_result.get('data')

def for_send():
    for i in range(50):
        send('603722')
        time.sleep(0.1)
# print("result = ",send(1,1,1))

##print("result = ", read_txt())
print("result = ", for_send())






