#coding:utf8
import urllib2
import urllib

base_url = "https://tieba.baidu.com/f?&pn="

# pn = (page - 1) * 50   获取pn的公式  page范围：1-n
def save_page(html,fname):
    """
    html : 获取到html页面内容
    :param html:
    :return:
    """
    with open('./tieba/' + fname.decode('utf-8'),'w') as f :
        f.write(html)

def get_page(name,start,end):

    for i in range(int(start),int(end) + 1):
        pn = (i - 1) * 50
        qs = {
            'kw' : name,
        }
        qs = urllib.urlencode(qs)

        request = urllib2.Request(base_url + str(pn) + '&' + qs)  # 生成页码
        response = urllib2.urlopen(request)
        html = response.read()
        save_page(html,name + '_' + str(i) + ".html")

if __name__ == '__main__':
    tieba_name = raw_input('贴吧名称：')  #返回字符型
    start = raw_input('输出起始页：')
    end = raw_input('输出结束页：')

    get_page(tieba_name,start,end)