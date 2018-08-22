import json
import requests, re, os, random
from lxml import etree
from urllib.parse import urlencode

print("result = ", 234)
agents = [
    "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.14 (KHTML, like Gecko) Chrome/10.0.601.0 Safari/534.14",
    "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.20 (KHTML, like Gecko) Chrome/11.0.672.2 Safari/534.20",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.27 (KHTML, like Gecko) Chrome/12.0.712.0 Safari/534.27",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/13.0.782.24 Safari/535.1"]
proxies = [{'http': 'http://121.43.170.207:3128'}, {'http': 'http://183.56.177.130:808'},
           {'http': 'http://121.42.167.160:3128'}, {'http': 'http://118.190.95.43:9001'}]
proxies = random.choice(proxies)
print('正在使用代理：', proxies)
headers = {'User-Agent': '%s' % random.choice(agents)}
print('正在使用请求头：', headers)


def gethtml(number, index=''):
    params = {
        'type': number,
        'query': index
    }
    url = 'https://weixin.sogou.com/weixin?' + urlencode(params)
    html = requests.get(url, headers=headers, proxies=proxies)
    html.encoding = 'utf-8'
    soup = etree.HTML(html.text)
    if html.status_code == 200:
        print('页面请求成功')
        return soup
    else:
        print('页面无法请求')


def get_articleurl(objects):
    urls = objects.xpath('//ul/li[starts-with(@id,"sogou_vr_11002601_box")]')
    for url in urls:
        arturl = url.xpath('//h3/a/@href')
        for art in arturl:
            art = art.replace('http', 'https')
            print(art)
            yield art


def parse_url(url):
    html = requests.get(url, headers=headers, proxies=proxies)
    html.encoding = 'utf-8'
    soup = etree.HTML(html.text)
    title = soup.xpath('//*[@id="activity-name"]/text()')[0].replace(' ', '')
    contents = soup.xpath("//p/span/text()")
    date = soup.xpath("//div[@id='meta_content']/em[@id='publish_time']/text()")
    print(title, contents, date)


def get_comments():
    params = {
         'f': 'json',
         'uin':'MjMxNzQ2NzIxNw%253D%253D',
         'key': '4fb12694827ad5dbad110c3cac8b640a382ec2d1be6d58b3ed2c4b074173d3631a109a4eae8e3208976345add9dc2ffda73e8b865e7cab1e68bdc4374b4bd62316ea9a7551f7ece60f9214a5d7a24376',
         'pass_ticket': 'zOpa1OLYssIM0Rv5t0a9gJSWnj%25252BQK%25252FhsSlS5BtvF0npZeSlYVMhv3QYrrhcy3%25252BE6',
         'wxtoken': '777',
         'devicetype': 'Windows%26nbsp%3B7',
         'clientversion': '62060426',
         'appmsg_token': '971_8aRswl1YGI7kydPAPbVCTEFo-Jt24KDpXwI_HUtabAT6lznDvoLKuppGVF1rlrgjL7SJ3X_Idpjs53jm',
         'x5': 0
    }
    _url = 'https://mp.weixin.qq.com/mp/getappmsgext'

    response = requests.post(url=_url, headers=headers, proxies=proxies, data=params)
    print('页面请求成功',response)
    json_result = json.loads(response.text)
    print('页面请求成功json_result', json_result)
    response.encoding = 'utf-8'
    # soup = etree.HTML(response.text)
    # if response.status_code == 200:
    #     print('页面请求成功')
    #     return soup
    # else:
    #     print('页面无法请求')


# if __name__ == '__main__':
#     # for number in range(2,100):
#     objects = gethtml(2, 'python')
#     art = get_articleurl(objects)
#     for ar in art:
#         parse_url(ar)
print("result = ", get_comments())