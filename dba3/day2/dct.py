#from operator import Itemgetter
#import json

#dct={}
#dct={'name':'tom','score':99,'aaa':True,'bb':None}  #((1,3),1):1
#
#dct=dict()  #dict dct= new dict()
#dct=dict(name='tonm',score='43')
#
#dct=dict([('name','tom'),('score',99)])  #列表里面放元组
#print(dct)
#names=['aa','bb','ss']
#score=[34,43,76]
#name_score=dict(zip(names,score))
#print(name_score)
#
#
#dct2=dict.fromkeys('name','score')
#dct2=dict.fromkeys(dct.keys())
#print(dct2)
#
#
#
#
#dct['name']
#dct['name']='jack' #赋值
#dct_json=json.dumps(dct)
#print(dct_json,type(dct_json))
#dct2=json.loads(dct_json)
#print(dct2,type(dct2))
#
#
#dct['age']=90
##update 更新dct
#dct.update({'name':'zoo','score':50,'gender':'M'})
#print(dct)#
#for i in enumerate('dhgfkgjth'):
#    print(i)
#
#s=['apple','orange','banana']
#for n in s:
#    print('{} is sweet'.format(n))
#print('banana'.count('a'))

#from operator import itemgetter
#s=[['a','h1'],['1','200']]
#print(sorted(s,key=itemgetter(1)))
#
#
#a = ['hakshfwfhaksgfdg']
#print(a[::2])
#a = ['h','k','h','w','h','k','g','d']
#b=('a','b','c')
#print(b[::2])
#
from lxml import etree
html='''
<bookstore>
    <book class='th'>
        <title lang="en">Harry Potter</title>
        <price>29.99</price>
    </book>
    <book class='th vip' lang='cn'>
        <title lang="cn">Learning XML</title>
        <title lang="en">Learning Python</title>
        <price>39.95</price>
    </book>
</bookstore>
'''
html = etree.HTML(html)
html = etree.ElementTree(html)
print(html)
print(html.xpath('bookstore'))
#print(html.xpath('//bookstore/book[1]/title'))
#print(html.xpath('//bookstore/book/title[1]'))
#print(html.xpath('//bookstore/book/title'))
#print(html.xpath('//@lang'))
#print(html.xpath('//title/@lang'))
#print(html.xpath('//title/text()'))
#print(html.xpath('//title[2]/text()'))
#print(html.xpath('//book[2]/title[2]/text()'))
#print(html.xpath('//title/text()')[2])
#print(html.xpath('//book[contains(@class,"th")]'))
print(html.xpath('//title[contains(text(),"Learning")]'))
