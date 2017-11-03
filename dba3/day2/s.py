s='fgoinfth'
lst=[1.2,4,6]
lst[0]
s[0]

sum(range(1,101))
sum(range(2,101,2))   #求偶数
s='fbgjhgmjhs'
print(s[1:5:2])#------->切片

lst=[1,2,3]
lst2=[]
#for n in lst:
#    lst2.append()



#'{:.2f}'.format(0.1465465)
#'{:.2f},{:.1f}'.format(0.1465465,9.35476)
#'{0:.2f},{1:.1f}'.format(0.1465465,9.35476)
#'{1:.2f},{0:.1f}'.format(0.1465465,9.35476)

s='https://www.zhihu.com/question/2999835'
lst=s.split('/')
print(lst[2])

names=[' Tom',' Jack ','Mary','Jerry ']
lst=[]
for n in names:
    lst.append(n.strip())
    #print(n.strip())
print(lst)

lst=[1,35,7,3,6,2,6,3,6,3,64]
lst1=[]
for n in lst:
    if n not in lst1:
        lst1.append(n)
print(lst1)


lst=[4,6,2,6,3]
lst1=[3,6,3,8]
from operator import itemgetter
z=list(zip(lst,lst1))
print(sorted(z,key=itemgetter(1)))
print(sorted(z,key=itemgetter(0)))

#func的作用是取得序列下标为括号中数字的元素
func=itemgetter(1)
print(func([8,9]))

lst0=[1,3,6,8]
lst=[]
for n in lst0:
    lst.append(n*n)
print(lst)
#列表生成式
lst=[n*n for n in lst0 if n%2==1]
lst=[n*n if n%2==1 else str(n) for n in lst0]
lst=[i*j for i in range(1,3) for j in range(2,4)]
lst=['{}*{}={}'.format(j,i,j*i) for i in range(1,3) for j in range(2,4)]
print(lst)

names=[' tom','jack ','mary',' jerry']
lst=[]
for name in names:
    lst.append(name.strip())
print(lst)
#改成列表生成式
lst2=[name.strip() for name in names]
print(lst2)

print(zip('123','abc'))
print(tuple(zip('123','abc')))
print(list(zip('123','abc')))
print(tuple(zip(['1','2','3'],['a','b','c'])))
print(list(zip(['1','2','3'],['a','b','c'])))
print(tuple(zip(('1','2','3'),('a','b','c'))))
print(list(zip(('1','2','3'),('a','b','c'))))

from operator import itemgetter
s=[('cat',44),('dog',78)]
print(sorted(s))
print(sorted(s,key=itemgetter(0)))
print(sorted(s,key=itemgetter(1)))

names=[' Tom',' Jack ','Mary','Jerry ']
lst=[n.strip() for n in names]
print(lst)

lst=['HELLO',123,234,'World','Python']
print([n.lower() if isinstance(n,str) else n for n in lst])
