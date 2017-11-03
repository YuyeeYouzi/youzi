class Person():
    def move(self):
        print('Person move')

class Animal():
    def move(self):
        print('Animal move')

#在几个父类没有共同父类的情况下，
#person和animal没有共同父类
#子类没有的方法或者属性会到父类中去查找
#查找顺序是从前到后（从左往右）
class Student(Person,Animal):
    pass

s = Student()
s.move()  #从前往后找

print('----------------父类有共同父类--------------------')
class Base():
    def move(self):
        print('Base move')

class Person(Base):
    pass
    #def move(self):
    #    print('Person move')

class Animal(Base):
    pass
    #def move(self):
    #    print('Animal move')

class Student(Animal,Person): #Animal-->Person-->Base
    pass

s = Student()
s.move()
print('-------------------------父类没有共同父类------------------')
class Base1():
    pass
    #def move(self):
    #    print('Base1 move')

class Base2():
    def move(self):
        print('Base2 move')

class Person(Base1):
    pass
    #def move(self):
    #    print('Person move')
    
class Animal(Base2):
    pass
    #def move(self):
    #    print('Animal move')
    
class Student(Person,Animal):
    pass

s = Student() 
s.move() #Person-->Base1-->Animal-->Base2

print('----------------有共同父类----------------')
#在有共同父类的情况下，从第一个开始找，如果第一个和第二个没有共同父类，
#找第一个的父类，第一个的父类和第二个的
#
class Base():
    def move(self):
        print('Base move')
class Base1(Base):
    pass
    #def move(self):
    #    print('Base1 move')

class Base2(Base):
    pass
    def move(self):
        print('Base2 move')

class Person(Base1):
    pass
    #def move(self):
    #    print('Person move')
    
class Animal(Base):
    pass
    def move(self):
        print('Animal move')
    
class Student(Person,Animal):
    pass

s = Student() 
s.move() #Person-->Base1-->Animal-->Base2-->Base

print('-------------------------类内建函数----------------------')
print(issubclass(Student,Base))# 子类
#print(issubclass(s,Base))#不行
print(isinstance(s,Base))# 的对象

class ABC(list,Student):
    pass

a = ABC('123')
a.move()
a.append(5)
print(a)

# 判断对象有没有某属性和方法
print(hasattr(a,'move'))
print(hasattr(a,'append'))
print(hasattr(list,'append'))
print(hasattr(a,'__init__'))
print(dir(a))
print(dir(Student))

#魔术方法
class Person():
    def __init__(self,name,age):
        self.name=name
        self.age=age
    pass
    def __str__(self):
        return 'name:{},age:{}'.format(self.name,self.age)

    def __len__(self): #可以用len函数
        return self.age

    def __add__(self,other): #可以用+操作符
        #return self.age+other.age
        return self.name+other.name

    def __eq__(self,other):
        return self.age==other.age
    def __gt__(self,other):
        return self.age>other.age
    def __ge__(self,other):
        return self.age>=other.age

    def __getitem__(self,item):
        if item=='name':
            return self.name
        elif item=='age':
            return self.age

    def __setitem__(self,item,value):
        if item=='name':
            self.name=value
        elif item=='age':
            self.age=value

    def __iter__(self):
        return [self.name,self.age]
    #def print_attrs(self):
    #    print(p.name,p.age)

p = Person('tom',77)
p2 = Person('jack',66)
print(p)
print(p2)
print(p.name,p.age)
print(p)
print(len(p))
print(p+p2)
print(p==p2) # 没写__eq__比较不明确，所以FALSE
print(p>p2)
print(p>=p2)
print(p2['name'])
#p.print_attrs()
p['name']=1
print(p['name'])

from collections import Iterable
print(isinstance(p,Iterable))

#for n in p:
#    print(n)