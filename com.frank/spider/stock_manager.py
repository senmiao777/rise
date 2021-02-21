#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import requests
import pymysql
import json

FUND_MANAGER_URL = 'http://fund.eastmoney.com/Data/FundDataPortfolio_Interface.aspx?dt=14&mc=returnjson&ft=all&pn=50&pi=%d&sc=abbname&st=asc'

def download_page(cp):
    url = FUND_MANAGER_URL % cp
    head = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'
    }
    data = requests.get(url, headers=head).content
    return data


def get_json_data(html):
    sub = str(html, encoding="utf-8")
    sub = sub[15:]
    sub = sub.replace("data", "\"data\"")
    sub = sub.replace("record", "\"record\"")
    sub = sub.replace("pages", "\"pages\"")
    sub = sub.replace("curpage", "\"curpage\"")
    json_result = json.loads(sub)
    data = json_result.get('data')
    return data


def deal_json_data(array, db):
    cursor = db.cursor()
    for i in range(len(array)):
        number = array[i][0]
        fund_manager_name = array[i][1]
        fund_company_code = array[i][2]
        fund_company_name = array[i][3]
        index_codes = array[i][4]
        index_names = array[i][5]
        days = array[i][6]
        market_value = array[i][10]
        if ('亿元' in market_value):
            market_value = market_value[0:len(market_value) - 2]
        else:
            market_value = "0.0"
        max_profit = array[i][11]
        if ('%' in max_profit):
            max_profit = max_profit[0:len(max_profit) - 1]
        else:
            max_profit = "0.0"


        sql = "INSERT INTO `fund_manager_info` ( `number`, `fund_manager_name`, `fund_company_code`, `fund_company_name`, `index_codes`, `index_names`, `days`, `market_value`, `max_profit`) " \
              "VALUES('%s','%s','%s','%s','%s','%s','%s','%s','%s');" % (
                  number, fund_manager_name, fund_company_code, fund_company_name, index_codes, index_names, days,
                  market_value, max_profit)
        try:
            # 执行sql语句
            # Exception exception 'latin-1' codec can't encode characters in position 214-218: ordinal not in range(256)
            # 解决方案 .encode("utf8").decode("latin-1")
            # decode = sql.encode("latin-1").decode("utf8")
            cursor.execute(sql)
            # 提交到数据库执行
            db.commit()

        except Exception as e:
            print('Exception exception %s' % e)
            db.rollback()


def main():
    db = pymysql.connect("192.168.31.22", "root", "look", "mydb", use_unicode=True, charset="utf8")
    cp = 1
    while cp <= 50:
        page = download_page(cp)
        json_array = get_json_data(page)
        deal_json_data(json_array, db)
        cp += 1
    db.close()


if __name__ == '__main__':
    main()
