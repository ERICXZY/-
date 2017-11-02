#coding:utf8
import urllib2
import urllib
import ssl
ssl._create_default_https_context = ssl._create_unverified_context  #指定不需要验证证书
#跳过安全证书验证

# base_url = 'https://www.12306.cn/mormhweb/'
base_url = 'https://www.baidu.com/'

response = urllib2.urlopen(base_url)
print response.read()