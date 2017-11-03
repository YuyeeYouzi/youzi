#encoding: utf-8

print(123)
print('欧巴')
'''print('欧巴')'''
type(id)
if 4:
    print('是一个4')
print(1 and [] and 3)
print(None and 2)
a=10
#if a<100:
#    print(a)
#elif a>:
#    print('a>100')
if 5<a<20:
    print(a)
bmi=46/(1.62**2)
if bmi<18:
    print("过轻")
elif bmi<25:
    print('正常')
elif bmi<28:
    print('过重')
elif bmi<32:
    print('肥胖')
else:
    print('严重肥胖')
print(bmi)

score=99
jieguo='及格' if score>60 else '不及格'
#      满足条件      条件判断   不满足条件的值
print(jieguo)

jieguo='优秀' if score>90 else '不优秀'
print(jieguo)

a=100
sum_=0
while a:
    if a%2==0:
        sum_+=a
    a-=1
print(sum_)

lst=[1,2,3,4,5,True,False,'fgh',None]
for n in lst:
    if isinstance(n,int):
        print(n+1)
    elif isinstance(n,str):
        print(n+str(1))
    else:
        print('None')

sum_1=0
for n in range(1,101):
    sum_1+=n
print(sum_1)


from itertools import product
for i,j,k in product(range(2),range(3),range(3)):
    print(i,j,k)

print(111,end='\n')
print(222,end='\t')
print(333,end='')
print('--------------------------------')
lst=['Bart',123,None,'Lisa','Adam']
for n in lst:
    #print(n)
    print('Hello,'+str(n))
print("----------------")
for n in lst:
    if isinstance(n,str):
        print('Hello,'+n)
   

a_count=i_count=e_count=u_count=o_count=0
text='''gvjfbjo sjrpfihbjp sjrogjjrea'''
for n in text:
    if n=='a':
        a_count+=1

    elif n=='i':
        i_count+=1
    elif n=='e':
        e_count+=1
    elif n=='u':
        u_count+=1
    elif n=='o':
        o_count+=1
#print('number of {} is {}'.format('a',a_count))
print(str(a_count)+'\n'+str(e_count)+'\n'+str(i_count)+'\n'+str(u_count)+'\n'+str(o_count))
print('{} de count is {}'.format('a',a_count))
print('{} de count is {}'.format('e',e_count))
print('{} de count is {}'.format('i',i_count))
print('{} de count is {}'.format('u',u_count))
print('{} de count is {}'.format('o',o_count))

from itertools import product
for i,j in product(range(1,10),range(1,10)):
    if(j<=i):
        print('{}*{}={}'.format(j,i,i*j),end='\t')
    if(i==j):
        print()

print('------------------------------')
for i in range(1,10):
    for j in range(1,i+1):
        print('{}*{}={}'.format(j,i,i*j),end='\t')
    print()



