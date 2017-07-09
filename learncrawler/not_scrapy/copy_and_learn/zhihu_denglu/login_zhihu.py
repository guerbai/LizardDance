# -*- coding: utf-8 -*-
from HTMLParser import HTMLParser
import requests

if __name__ == "__main__":
    phonenum='xxxxxxxxxxx'
    pwd='xxxxxxx'
    mainURL='http://www.zhihu.com/'
    loginURL='http://www.zhihu.com/login/phone_num'
    
    headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/28.0.1500.72 Safari/537.36'}
    
    s = requests.session()
    r = s.get(mainURL)
    print r.cookies     #打印页面cookies，可在终端自己查看
    
    login_data = {'_xsrf':r.cookies['_xsrf'], 'phone_num':phonenum, 'password':pwd, 'rememberme':'y'}
    t = s.post(loginURL, login_data, headers)
    print t.text        #显示登录结果，正常情况下应该是{"r:"0,"msg":"\u767b\u9646\u6210\u529f"}，"msg"字段中显示的是登录结果(Unicode)

    t = s.get(mainURL,verify=False)
    print  t.text.encode('utf-8')
    
    f = open('zhihu_test.html','w')
    f.write(t.text.encode('utf-8'))