#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import requests
import json
import pymysql
import re

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
    #content = response.content
    # 注意：直接通过response.json 得到的数据，前边会有 <bound method Response.json of <Response [200]>> 这么个字符串，后边还有点特殊，不好处理
    print("content json =", json.loads(content))
    return content


def parse_html(response):
    loads = json.loads(response)
    return loads


def get_comment_detail(list,db):
    print( "--------------------------------------------len(list)",len(list))
    cursor = db.cursor()

    for i in range(len(list)):

        obj = list[i]
        print("第 %d 个元素是%s" % (i + 1,obj))
        content = obj.get('content')
        content = remove_emoji(content)
        # 地区：济南，性别：男，职业：金融民工，学历：本科，年龄：31，对对方的大致要求：有趣最重要，别的都好说。
        info = get_user_base_info(content)
        created_time = obj.get('created_time')
        author = obj.get('author').get('member')
        id = author.get('id')
        url_token = author.get('url_token')
        name = author.get('name')
        avatar_url = author.get('avatar_url')
        headline = author.get('headline')
        gender = author.get('gender')

        print(
            "--------------------------------------------content =%s,info=%s,created_time=%s,id=%s,url_token=%s,name=%s,avatar_url=%s,headline=%s,gender=%s" %
            (content, info, created_time, id, url_token, name, avatar_url, headline, gender))

        sql = "INSERT INTO `blind_date_comment` (`area`,`occupation`,`requirement`,`content`,`user_age`,`user_education`,`user_id`,`user_name`,`url_token`,`head_image`,`gender`,`register_gender`,`register_at`,`headline`) " \
              "VALUES('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s');" % (info[0],info[2],info[5],content,info[4],info[3],id,name,url_token,avatar_url,gender,info[1],created_time,headline)
        print("`````````````````sql =",sql)
        try:
            # 执行sql语句
            # Exception exception 'latin-1' codec can't encode characters in position 214-218: ordinal not in range(256)
            # 解决方案 .encode("utf8").decode("latin-1")
            #decode = sql.encode("latin-1").decode("utf8")
            cursor.execute(sql)
            # 提交到数据库执行
            print("`````````````````execute =")
            db.commit()

        except Exception as e:
            print('Exception exception %s' % e)
            db.rollback()


emoji_pattern = re.compile(u"(\ud83d[\ude00-\ude4f])|"  # emoticons
    u"(\ud83c[\udf00-\uffff])|"  # symbols & pictographs (1 of 2)
    u"(\ud83d[\u0000-\uddff])|"  # symbols & pictographs (2 of 2)
    u"(\ud83d[\ude80-\udeff])|"  # transport & map symbols
    u"(\ud83c[\udde0-\uddff])"  # flags (iOS)
    "+", flags=re.UNICODE)

emoji_pattern2 = re.compile(u'[\U00010000-\U0010ffff]')


def remove_emoji(text):
    return emoji_pattern2.sub(u'', text)

def remove_emoji2(text):
    try:
        # python UCS-4 build的处理方式
        highpoints = re.compile(u'[\U00010000-\U0010ffff]')
    except re.error:
        # python UCS-2 build的处理方式
        highpoints = re.compile(u'[\uD800-\uDBFF][\uDC00-\uDFFF]')

    resovle_value = highpoints.sub(u'??', src_string)
    return resovle_value

def get_user_base_info(content):
    split = content.split("，",5)

    # 用逗号分隔出有效数据
    if len(split) > 5:
        print("len(split) > 5:")
        if (split[0].find("：") != -1):
            print("11111111111 split[0].find(: ) != -1 split=", split)
            area = split[0].find("地区") != -1 and split[0][3:len(split[0])] or "area"
            register_gender = split[1].find("性别") != -1 and split[1][3:len(split[1])] or "register_gender"
            occupation = split[2].find("职业") != -1 and split[2][3:len(split[2])] or "occupation"
            education = split[3].find("学历") != -1 and split[3][3:len(split[3])] or "education"
            age = split[4].find("年龄") != -1 and split[4][3:len(split[4])] or "age"
            requirement = split[5].find("要求") != -1 and split[5][split[5].find("要求：")+3:len(split[5])] or "requirement"
            return area, register_gender, occupation, education, age, requirement
        elif (split[0].find("地区") != -1):
            print("2222222222221 split[0].find(: ) != -1 split=", split)
            area = split[0].find("地区") != -1 and split[0][2:len(split[0])] or "area"
            register_gender = split[1].find("性别") != -1 and split[1][2:len(split[1])] or "register_gender"
            occupation = split[2].find("职业") != -1 and split[2][2:len(split[2])] or "occupation"
            education = split[3].find("学历") != -1 and split[3][2:len(split[3])] or "education"
            age = split[4].find("年龄") != -1 and split[4][2:len(split[4])] or "age"
            requirement = split[5].find("要求") != -1 and split[5][split[5].find("要求")+2:len(split[5])] or "requirement"
            return area, register_gender, occupation, education, age, requirement
        else:
            print("66666666666666666666 split[0].find(: ) != -1 split=", split)
            return "area", "register_gender", "occupation", "education", "age", "requirement"


    content_split = content.split(" ",5)
    if len(content_split) > 5:
        if (content_split[0].find("：") != -1):
            print("333333333333333333333333 content_split[0].find(: ) != -1 content_split=", content_split)
            area = content_split[0].find("地区") != -1 and content_split[0][3:len(content_split[0])] or "area"
            register_gender = content_split[1].find("性别") != -1 and content_split[1][
                                                                    3:len(content_split[1])] or "register_gender"
            occupation = content_split[2].find("职业") != -1 and content_split[2][3:len(content_split[2])] or "occupation"
            education = content_split[3].find("学历") != -1 and content_split[3][3:len(content_split[3])] or "education"
            age = content_split[4].find("年龄") != -1 and content_split[4][3:len(content_split[4])] or "age"
            requirement = split[5].find("要求") != -1 and split[5][split[5].find("要求：")+3:len(split[5])] or "requirement"
            return area, register_gender, occupation, education, age, requirement
        elif (content_split[0].find("地区") != -1):
            print("44444444444444444444 content_split[0].find(: ) != -1 content_split=", content_split)
            area = content_split[0].find("地区") != -1 and content_split[0][2:len(content_split[0])] or "area"
            register_gender = content_split[1].find("性别") != -1 and content_split[1][
                                                                    2:len(content_split[1])] or "register_gender"
            occupation = content_split[2].find("职业") != -1 and content_split[2][2:len(content_split[2])] or "occupation"
            education = content_split[3].find("学历") != -1 and content_split[3][2:len(content_split[3])] or "education"
            age = content_split[4].find("年龄") != -1 and content_split[4][2:len(content_split[4])] or "age"
            requirement = split[5].find("要求") != -1 and split[5][split[5].find("要求")+2:len(split[5])] or "requirement"
            return area, register_gender, occupation, education, age, requirement
        else:
            print("777777777777777777777777 split[0].find(: ) != -1 split=", split)
            return "area", "register_gender", "occupation", "education", "age", "requirement"
    else:
        print("55555555555555555555 split[0].find(: ) != -1 split=", split)
        return "area", "register_gender", "occupation", "education", "age", "requirement"


def insert_sql(data):
    # 打开数据库连接
    db = pymysql.connect("192.168.31.22", "root", "look", "mydb",use_unicode=True, charset="utf8")
    # 使用 cursor() 方法创建一个游标对象 cursor
    #cursor = db.cursor()
    # 使用 execute()  方法执行 SQL 查询
    get_comment_detail(data,db)

    # 关闭数据库连接
    db.close()

page = download_page(url)
print("download_page=", page)
html = parse_html(page)
print(html)
data = html.get('data')
print('get data=', data)

# comment_detail = get_comment_detail(get)
# print('###############comment_detail=', comment_detail)
print("insert_sql=", insert_sql(data))