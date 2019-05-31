import requests
import http.cookiejar
import time
import json
import codecs
import datetime



#登录网址
url = "http://ip.taobao.com/service/getIpInfo.php?ip="


def scan(ip):

    login_session = requests.Session()
    f = login_session.get(url+ip)
    print (f.json())
    json_data = f.json()
    json_str = json.dumps(json_data)
    data2 = json.loads(json_str)
    data = data2['data']
    print("国家为：", data['country'])
    return (data['country'])


with open('ip-3-22.txt','r',encoding = 'utf-8') as f:
    line = f.readlines()
    a = 1
    for i in line:
        a = a + 1
        print (a)
        print (i)
        IP_address = scan(i)
        if (IP_address != '中国'):
            print ('境外IP', i)
    
    f.close()

