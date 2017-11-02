#coding:utf8
import urllib2,urllib
import json
import time
import random
import hashlib

fanyi_url = 'http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule'

headers = {
    "Host" : "fanyi.youdao.com",
    "Connection" : "keep-alive",
    "Content-Length" : "201",
    "Accept" : "application/json, text/javascript, */*; q=0.01",
    "Origin" : "http://fanyi.youdao.com",
    "X-Requested-With" : "XMLHttpRequest",
    "User-Agent" : "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36",
    "Content-Type" : "application/x-www-form-urlencoded; charset=UTF-8",
    "Referer" : "http://fanyi.youdao.com/",
    "Accept-Language" : "zh-CN,zh;q=0.8",
    "Cookie" : "OUTFOX_SEARCH_USER_ID=-2142593123@10.169.0.82; OUTFOX_SEARCH_USER_ID_NCOO=1364653123.9530659; JSESSIONID=aaasPgIFXTllihnO4eb7v; ___rl__test__cookies=1506477842098",
}

key = raw_input("请输入翻译的词：")

now = lambda : int(time.time() * 1000)
# salt = now()
salt = 1388888888888
sign = 'fanyideskweb' + key + str(salt) + "rY0D^0'nM0}g5Mm1z%1G4"
m5 = hashlib.md5()
m5.update(sign)
sign = m5.hexdigest()

data = {
    "i": key,
    "from" : 	"AUTO",
    "to" :	"AUTO",
    "smartresult": "dict",
    "client" :	"fanyideskweb",
    "doctype" : "json",
    "version"	: "2.1",
    "keyfrom" : "fanyi.web",
    "action	" : "FY_BY_REALTIME",
    "typoResult" : "true",
    "salt" : str(salt),
    "sign" : sign,
}
data = urllib.urlencode(data)
request = urllib2.Request(fanyi_url,data=data,headers=headers)
response = urllib2.urlopen(request)

print response.read()