#!/usr/local/python3/bin/python3

import requests
import http.cookiejar
import time
import json
import codecs
import datetime

#登录网址
url = "http://www.shsxs.me/auth/login"
#签到网址
checkin_url = 'http://www.shsxs.me/user/checkin'
#退出登录
logout_url = 'http://www.shsxs.me/user/logout'
#系统时间
ISOTIMEFORMAT = '%Y-%m-%d %H:%M'
thetime = datetime.datetime.now().strftime(ISOTIMEFORMAT)

login_headers = {
    'User-Agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.80 Safari/537.36",
    'Referer':"http://www.shsxs.me/auth/login",
}

login_session = requests.Session()
f = login_session.get('http://www.shsxs.me', headers = login_headers)
# print(f.headers)

postData = {
    'email': 'amareeee@163.com',
    'passwd': 'amarevpn'
}

username = []

with open('/home/username.json','r',encoding = 'utf-8') as f:
    d = json.load(f)
    username = d
    f.close()

def login(postData):
    response=login_session.post(url=url, data=postData, headers=login_headers)
    #解码后的返回数据
    print(response.content.decode('utf-8'))
    #获取返回状态
    print(response.status_code)
    #获取登录信息
    print(response.json())
    #签到
    response = login_session.post(url = checkin_url, headers = login_headers)
    #获取签到信息
    print(response.json())

    #退出登录
    login_session.get(url = logout_url, headers = login_headers)

    return response.json()

print('time')
print(thetime)    
#切换用户签到
for i in username.values():
    print (i)

    if(login(i)['msg'] == '您似乎已经续命过了...'):
        with codecs.open('/home/log.text', 'a', 'utf-8') as log:

            log.write(thetime +'\t' + i['email'] + '\t' + '签到失败')
            log.write('\n')
            log.close()

    time.sleep(3)
    
print('over')
    







