#函数返回值
def foo():
    return 1,2,3
a = foo()
print(a)
a,b,c=foo()
print(a,b,c)

def add(a,b):
    a=1
    return a+b
a = 2
b = 3
print(add(a,b))#----->相当于先赋值2，再运行函数，重新赋值a=1
print(a)#------->全局变量
print('-------------bar---------------')
def bar():
    print(a)
bar()

#闭包
a = 99
def foo():  #定义域
    a = 88 #---------------->没有88,就往上找，结果为99
    def bar(): #可以把函数名看成普通变量
        #a = 33
        print('bar in foo,a is',a) #a是几，看函数在哪里定义，不是看函数在哪里调用
    #bar()
    return bar
    def bar3():
        print('bar3 in foo,a is ',a)
        return bar,bar3
def bar1():
    print('bar1 out foo,a is',a)
bar2=foo()
#bar3(1)
bar2()
bar1()

b = 77
def abb():
    b = 66
    def ass():
        print('ass in abb,a,b is',a,b)
    return ass
def ass1():
    print('ass1 out abb,a,b is',a,b)
c=abb()
c()
ass1()

print('-------------------------函数做参数------------------')
def add(a,b):
    return a+b
def sub(a,b):
    return a-b

def select_function(function,a,b):
    return function(a,b)  #add(a,b)
result = select_function(add,1,3)
result1 = select_function(sub,1,3)
print(result)
print(result1)

print('-------------------递归------------------------')
def fib(n):
    if n == 0:
        rtn = 0
    elif n == 1:
        rtn = 1
    else:
        rtn = fib(n-1)+fib(n-2)
    return rtn

print(fib(7))

def fib(n):
    a,b=0,1
    while(n>0):
        a,b,n=b,a+b,n-1
    return a
print(fib(7))
 
lst = [3,7,[0,[9,5],7],1]
#lst2 = [3,7,0,9,5,7,1] 扁平化处理，用递归
# 我自己写的，不对啊
def flatten_list(lst):
    lst2=[]
    for n in lst:
        if isinstance(n,list):
            n_str = str(n)
            n_str.replace('[','').replace(']','')
    return lst2
print(flatten_list(lst))

# 老师讲的
def flatten_list(lst,rtn=None):
    if rtn==None:
        rtn = []
    for n in lst:
        if isinstance(n,list):
            flatten_list(n,rtn)
        else:
            rtn.append(n)
    return rtn
print(flatten_list(lst))

print('---------------------lambda----------------------')
def foo(a):
    return a+1
lam1 = lambda a:a+1
print(lam1(1))

lst=[(1,2),(4,1),(3,5)]
sorted_list=sorted(lst,key=lambda item:item[1])
print(sorted_list)

from functools import reduce 
xs = [1,2,3,4]
ys = list(map(lambda x:x+1,xs))
print(list(ys))
print(reduce(lambda x,y:x+y,ys))

str_number = '12345' #转成 int 12345
print(list(map(lambda x:int(x),str_number)))
numbers = map(lambda x:int(x),str_number)
# 匿名函数参数规则都一样，位置参数要写在默认参数前
print(reduce(lambda x,y:10*x+y,numbers))

g=(n*n for n in range(4))
lst=[n*n for n in range(4)]

def foo():
    #print(1)
    #print(2)
    #print(3)
    #print(4)
    yield 1
    yield 2
    yield 3
    yield 4
g = foo()
print(next(g))
print(next(g))
print(next(g))
print(next(g))
#print(next(g))

def bar():
    for n in range(4):
        yield n*n
g=bar()
print(next(g))
print(next(g))
print(next(g))
print(next(g))
#print(next(g))


#定义装饰器
def to_string(func): #func代表需要改变行为的原函数
    #rtn = func()
    def wrapper(a,b):
        rtn = func(a,b)
        return str(rtn)
    return wrapper

def print_line(func):
    def wrapper(a,b):
        print('---------------------------')
        return func(a,b)
    return wrapper

@to_string
@print_line
def add(a,b):#默认参数和返回值都是数字
    return a+b

@to_string
def sub(a,b):
    return a-b

@to_string
def multiply(a,b):
    return a*b

#print(type(add(1,2)))
#add=to_string(add)
#print(type(add(1,2)))
print(add(1,2))
print(sub(1,3))

# dict_select
dct = {
    '+':add,
    '-':sub,
    '*':multiply
}
print(dct['+'](1,3))
print(dct['-'](1,3))

def foo(a,b,c=0): #位置参数，默认参数
    print(a,b,c)
foo(1,b=9) #关键字参数
