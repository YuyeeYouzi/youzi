+#import urllib #urllib urllib2
#urllib.request
from urllib import request,error
from lxml import etree

url = 'http://www.51job.com/'
response = request.urlopen(url) # 打开url获取内容
#html = response.read() #bytes
#html=html.decode('gbk')
#print(html)

#headers = {
#    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.221 Safari/537.36 SE 2.X MetaSr 1.0',
#    #'Connection':'keep_alive'
#}
##构造一个请求
#req = request.Request(url,headers=headers)
##html = request.urlopen(req)
##html=html.read().decode('gbk')
##print(html)
#try:
#    html = request.urlopen(req).read().decode('gbk')
#except Exception as e:
#    print(e,url)

xml = '''
<bookstore>
    <title lang="en">Tom Jarry</title>
    <book>
        <title lang="en">Harry Potter<price>555</price></title>
        <price id='111'>29.99</price>
    </book>
    <book>
        <title lang="cn" >Learning XML</title>
        <price id='222'>39.95</price>
    </book>
</bookstore>
'''
#xml = etree.Html(xml)
xml = etree.ElementTree(etree.HTML(xml))
print(xml)

#print(xml.xpath('/html/body/bookstore/book'))  绝对路径
print(xml.xpath('//bookstore/book/..'))  #相对路径
print(xml.xpath('//bookstore/book/title/@lang')) #属性
print(xml.xpath('//title/text()')) #文本
print(xml.xpath('//book/title/text()'))
print(xml.xpath('//bookstore/title/text()'))
print(xml.xpath('//bookstore/book[1]/title/price/text()')) # book后面的括号写不写都一样
print(xml.xpath('//bookstore/book/title[1]')) # 下标从1开始
print(xml.xpath('//bookstore//title[1]'))#---->有3个
print(xml.xpath('//bookstore/title[1]'))#---->1个 
print(xml.xpath('//bookstore//price[@id]'))
print(xml.xpath('//bookstore//price[@id="222"]'))
print(xml.xpath('//bookstore/*')) #book下的所有子节点
print(xml.xpath('//bookstore/*[@*]'))

def get_html(url)
    try:
        response = request.urlopen(url)
    except error.URLError as e:
        print(e,url)
    except error.HTTPError as e:
        print(e,url)
    except Exception as e:
        print(e.url)
    return html


