from copy import copy,deepcopy #------------------------->深拷贝才是真正的拷贝
#import copy
class Person():
    def __init__(self,name,scores):
        self.name=name
        self.scores=scores

p1=Person('cat',[98,44,78])
p1_copy = copy(p1)
p1_deepcopy = deepcopy(p1)
print(p1)
print(p1_copy) #p1 is p1_copy false

print(id(p1.scores)) #----------------->列表是可变的，深拷贝会改变
print(id(p1_copy.scores))
print(id(p1_deepcopy.scores))

print(id(p1.name))#---------------->字符串本身不可变，所以深拷贝也一样
print(id(p1_copy.name))
print(id(p1_deepcopy.name))

p1.scores.append(110)
print(p1.scores)  #[98, 44, 78, 110]
print(p1_copy.scores) #[98, 44, 78, 110]
print(p1_deepcopy.scores) #[98, 44, 78]

#print(__name__)
#if __name__ == '__main__':
#    print(__name__)





#import os # 操作系统
#import sys # 你运行的这个Python系统

class Rectangle():
    def __init__(self,width,high):
        self.__width=width
        self.__high=high

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self,width):
        self.__width=width

    @property
    def high(self):
        return self.__high

    @high.setter
    def high(self,high):
        self.__high=high

    @property
    def area(self):
        return self.__high*self.__width


    def __str__(self):
        return 'width:{},high:{}'.format(self.__width,self.__high)

    def __add__(self,other):
        return self.area+other.area

    def __eq__(self,other):
        return self.high==other.high and self.width==other.width

r=Rectangle(3,4)
r1=Rectangle(5,7)
print(r.area)
print(r1.area) #area上面没有property的话，这里就要用（r1.area()）
print(r+r1)
print(r==r1)