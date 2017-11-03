# 函数是一个代码单元，函数也是对象
# callable
#def 函数名():
#    代码块
def add(a,b=0):#positional argument 位置参数概念
    return a+b
add(1)
#def sorted(iter,key=None,reverse=False):#不报错，是因为有默认值
#sorted(list)
# 函数调用的时候，称作关键字参数keyword argument
# sorted(lst,key=xxxx,reverse=True)
# 关键字参数不必用定义的顺序调用
def my_abs(x):
    if x<0:
        x=-x
    return x
print(my_abs(-1))

# 定义函数时，位置参数写在默认参数前面
def add2(a,b=0,c=0):
    return a+b+c
# 调用函数时，位置参数写在关键字参数前面
#add2(c=1,b=2,3) 都不对
#add2(2,a=1,b=2) 都不对

#定义一个求次方的函数，默认求平放
#def mull(a,n=2):
#    if not isinstance(a,(int,float)) or not isinstance(n,(int,float)):
#        #print('参数异常')
#        #return
#        #print(a**n)
#        raise TypeError('参数异常')#throw抛异常
#    #if isinstance(a,(int,float)) and isinstance(n,(int,float)):
#    return a**n
#try:
#    1/0
#    aaa
#    mull(4,'4')
#    #1/0
#except TypeError as e:
#    print(e)
#except NameError as e:
#    print(e)
#except Exception as e:
#    print(e)
#mull('3')

#def foo():
#    if not fgvjrj:
#    if not kjbfv:

def add(a,b=2):
    if not isinstance(a,(int,float)) or not isinstance(b,(int,float)):
        raise TypeError()
    return a+b
try:
   add('1')
except TypeError as e:
    print(e)
#print(add('1'))


def append_list(val,lst=[]):#尽量用不可变类型做默认参数
    lst.append(val)
    return lst
def append_list(val,lst=None):
    if lst == None:
        lst = []  #每次调用时，[]都是一个不同的对象
    lst.append(val)
    return lst    
list1 = append_list(10)
list2 = append_list(123,[])
list3 = append_list('a')
print(list1)
print(list2)
print(list3)




a=b=c=d=f=g=0
#if a>0 and b>0 and c>0 and d>0 and f>0 and g>0:
conditions=[a>0,b>0,c>0,d>0,f>0,g>0]
conditions=[1,2,3]
conditions=[]#-------------------------->True   有一个false就是false
print(all(conditions))  #all的参数是一个列表  全为TRUE才是TRUE
print(any([]))#----------------->False    有一个TRUE就是true   操作的是[]里面的