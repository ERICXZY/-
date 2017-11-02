#coding:utf8
import requests
from lxml import etree
import urllib2

headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'
}

def getImage(content_url):
    response = urllib2.urlopen(content_url)
    html = response.read()
    xml = etree.HTML(html)
    image_url = xml.xpath('//cc//img[@class="BDE_Image"]/@src')
    for image in image_url:
        print 'saveing image %s' % image
        response = urllib2.urlopen(image)
        fname = image.split('/')[-1]
        with open('./images/' + fname,'wb') as f:
            f.write(response.read())


def getPage():
    base_url = 'https://tieba.baidu.com/f?kw=美女&pn='

    page = 0
    while page <= 450:
        pre_url = 'https://tieba.baidu.com'
        fullurl = base_url + str(page)
        # response = requests.get(fullurl,headers=headers)
        response = urllib2.urlopen(fullurl)
        html = response.read()
        xml = etree.HTML(html)

        # xpath 模糊查询
        links = xml.xpath('//a[contains(@class,"j_th_tit")]/@href')

        for link in links:
            content_url = pre_url + link
            getImage(content_url)

        page += 50

if __name__ == '__main__':
    getPage()