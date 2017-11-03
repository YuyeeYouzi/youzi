def foo():
    pass
#a = foo()
print(foo)

def add(a,b=0):
    return a+b
a = add(1,2)
b = add(5)
print(a)
print(b)
#sorted(lst,key=,reverse=)
def add(b,*a):
    print(b,a)
    return a
add(1,2,3,4)
b,*a=1,2,3,4
print(b,a)
def add(**a):
    print(a)

def foo(*b,**a):
    print(a,b)
    return a
foo(3,4,5,fh=1,rhh=False,name='cat')

#def add(a,b):
#    if not isinstance(a,int) or not isinstance(b,int):
#        raise TypeError('we need int')
#    rtn  = a+b
#    return rtn
#s = add('1',3.5)
#print(s)
#try:
#    a=add(1,'')
#    print(a)
#except Exception as e:
#    print(e)

#def foo(a,b,func=add):
#    return func(a,b)
def bar(select):
    def add(a,b):
        return a+b
    def multiply(a,b):
        return a*b
    def sub(a,b):
        return a-b
    if select =='+':
        rtn=add
    elif select =='*':
        rtn=multiply
    elif select =='-':
        rtn=sub
    return rtn
#add2 = bar()
#print(add2(3,5))
#print(bar('*')(3,5))
#lambda x,y:x+y
from operator import itemgetter
s='cadbe'
lst=[3,7,4,76,4]
r=zip(s,lst)

print(sorted(r,key=itemgetter(1)))
#print(sorted(r,key=lambda item:item[0]))
#print(r)


class Student():
    def __init__(self,name,score):#类似于构造器，当student=Student()时会调用
        self.__name = name
        self.__score = score
    
    def eat(self,food): #实例方法，对象方法
        print('{} eat {}'.format(self.__name,food))

    #def get_name(self):
    #    return self.__name

    #def set_name(self,name):
    #    self.__name=name
    
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self,name):
        self.__name=name

    @property
    def score1(self):
        return self.__score

    @score1.setter
    def score(self,score):
        self.__score=score

student = Student('tom',78)
#print(student.score)
print(student)
student.age=13 #动态绑定
#student2 = Student('jack',88)
#student2.eat('cake')#
print(student.name)
print(student.score)
student.name = 'aa'
student.score=99
print(student.name)
print(student.score)

# 类方法，cls是class的简写
#@classmethod
#def move(cls):
#    pass
#    
#staticmethod  
#def fly():
#
class Base():
    def foo(self):
        print('Base foo')

class A(Base):
    def foo(self):
        print('A foo')

a = A()
a.foo()

class mylist(list):
    pass

mylist = [1,2,3,5]
print(mylist[1])