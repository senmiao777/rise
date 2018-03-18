#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import requests
import json


url = "https://www.zhihu.com/api/v4/answers/251023939/comments?include=data%5B*%5D.author%2Ccollapsed%2Creply_to_author%2Cdisliked%2Ccontent%2Cvoting%2Cvote_count%2Cis_parent_author%2Cis_author&order=normal&limit=20&offset=0&status=open"
# 直接输入URL访问知乎的链接
# 报{"error": {"message": "ZERR_NO_AUTH_TOKEN", "code": 100, "name": "AuthenticationInvalidRequest"}}
# 很明显，是权限问题
# 在header里加了 'authorization': 'oauth c3cef7c66a1843f8b3a9e6a1e3160e20' 问题解决
# 我怎么知道解决方案是加个authorization呢？猜的
# 从网页登陆后，访问链接，在request header 里发现有这个参数，试了下OK了

def download_page(url):
    print("download_page url=", url)
    head = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36',
        'authorization': 'oauth c3cef7c66a1843f8b3a9e6a1e3160e20'
    }
    response = requests.get(url, headers=head)
    content = response.content.decode()
    # 注意：直接通过response.json 得到的数据，前边会有 <bound method Response.json of <Response [200]>> 这么个字符串，后边还有点特殊，不好处理
    json2 = response.json
    print("content json =",json.loads(content))
    print("json2=",json2)
    return content

def parse_html(response):
    loads = json.loads(response)
    return loads


page = download_page(url)
print("download_page=",page)
# html = parse_html(page)
# print(html)
