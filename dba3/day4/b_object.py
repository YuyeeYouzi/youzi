class Student():
    x = 1 #类属性

lst = list() #实例化一个对象
s=Student() #实例化一个对象
print(type(s))
print(Student.x)
print(s.x) #对象中找不到变量到类属性中找，包括动态
Student.a = 2 #动态绑定  a = 2
del Student.x #删除一个属性
#print(s.x)  AttributeError: 'Student' object has no attribute 'x'
print(s.a)

print('-----------实例属性-------------')
#class Student():
#    x = 1 #类属性
#    def __init__(self,name,score):
#        # 实例初始化函数
#        self.__name = name
#        self.__score = score
#        #self.subject = subject
#    def get_name(self):
#        return self.__name
#
#    def set_name(self):
#        self.__name = name
#
#    def get_score(self):
#        return self.__score
#
#    def set_score(self):
#        self.__score = score
#
#
#    @property  
#    def name(self): #对应get_name
#        return self.__name
#    @name.setter
#    def name(self,name):
#        self.__name = name
#
#    @property
#    def score(self):
#        return self.__score
#
#    @socre.setter
#    def score(self,score):
#        self.__score = score
#
#    def study(self,subject):
#        self.subject = subject #可以随时绑定属性
#        print('{} is studying'.format(self.__name))
#    def __eat(self,food): #私有就是前面加两个下划线命名的属性和方法
#        pass
#
#    @staticmethod
#    def foo():
#        print('student foo is staticmethod')
#
#    @classmethod
#    def bar(cls):
#        print('student foo is classmethod',cls.__name__)

#s = Student('tom',99,'math')
#print(s.name,s.score)
#s.study('english')
#print(s.subject)
#s.name='cat'
#print(s.name)#
#print(s.name)

#类也是一个对象
#class type():
#   pass
#   ...
#Student = type() type Student = new type(...)
#                 type str = new str(...)
#                 

class Person():
    def __move(self): #对象的方法要加self
        print('person is move')

    def __init__(self,name):
        self.__name=name
    def get_a_name(self,name):
        self.__name = name

    @property
    def name(self):
        print('----')

    def eat(self,food):
        print('{} is eating {}'.format(self.__name,food))
p = Person('tom') #传参的话一定耀写__init__
p.get_a_name('cat')

print('----------------继承--------------')
#子类继承父类所有非私有方法
class Student(Person):
    pass