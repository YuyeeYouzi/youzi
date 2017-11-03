lst2=[1,-2,-3,4]
def poo(n):
    return n*n
print(list(map(poo,lst2)))
print(list(map(abs,lst2)))
print([abs(n)for n in lst2])

class Rec():
    def __init__(self,width,high):
        self.__width = width
        self.__high = high

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self,width):
        self.__width = width

    @property
    def high(self):
        return self.__high

    @high.setter
    def high(self,high):
        self.__high = high

    @property
    def area(self):
        return self.__high * self.__width

    def __repr__(self):
        return '{}-{}-{}'.format(self.width,self.high,self.area)

    def __add__(self,other):
        print(self.area + other.area)
        return self.area+other.area

    def __eq__(self,other):
        print(self.area==other.area)
        return self.area==other.area

#r = Rec(6,7)
#r2 = Rec(6,7)
##print(r,area)
##print(r)
#from urllib import request
#url='http://www.baidu.com'
#response = request.urlopen(url) 
##print(dir(response))
##print(response.status)
#html = response.read().decode('utf-8') #bytes
#print(html)

#a='你好'
#a1 = a.encode('utf-8')
#print(a1.decode('utf-8'))
#
#try:
#    #reponse=request.urlopen(url)
#    req=request.Request(url=url,headers=headers)
#    reponse=request.urlopen(req)
#    html=response.read().decode('utf-8')  #bytes
#except error.URLError as e:
#    print(e,url)
#except error.HTTPError as e:
#    print(e,url)
#except Exception as e:
#    print(e,url)
from collections import Iterable