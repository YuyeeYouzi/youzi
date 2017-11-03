import numpy as np
from copy import copy,deepcopy
np.random.seed(13)
arr = np.random.randint(1,10,size=(4,2))
print(arr)
print(arr[0])
print(arr[0][1])

print(arr[1:3]) #切片
arr1d=np.arange(10)
print(arr1d)
s=arr1d[1:4] #[1,2,3] 还是指向arr1d
s1=deepcopy(arr1d[1:4])
s2=arr1d[1:4].copy()
print(s)
print(s1)
print(s2)
arr1d[1:8] = 99
print(arr1d)
print(s)
print(s1)
print(s2)

np.random.seed(13)
a=np.arange(1,10).reshape(3,3)
print(a,'---------------')
print(a[:2])

a= np.arange(1,10)
print(a)
b=a**2
print(b)
print(b[1])
i = np.array([2,4,5,5,3])
print(b[i])
print(b[[2,4,5,5,3]])

j = np.array([[2,3],[6,7]])
print(a[j])

#a = b.reshape(4,3)
#print(a,'-----------reshape a')
#
print('--------------------------------------')
a= np.arange(1,10).reshape(3,3)
print(a)
print(a.sum())
print(a.sum(axis=0)) #纵向
print(a.sum(0))
print(a.sum(axis=1)) #横向

a=np.array([1,2,3])
b=a
a+=np.array([1,1,1])
print(b)
a=np.array([1,2,3])
b=a
a=a+np.array([1,1,1])
print(b)

a = [1,2,3]
b = a
a +=[1,1,1]
print(b)

a = [1,2,3]
b = a
a = a+[1,1,1]
print(b)

a='abc'
b=a
a+='11'
print(b)
print(a)

a = np.arange(1,10)
a >5
print(a>5)
print(a[a>5])
print(a[(a>2)&(a<7)])

b = np.arange(1,13).reshape(4,3)

print(b[b>5]) # 选出数组中大于5的元素  和b的形状无关
print((b>5).sum()) #几个元素大于5

print(a[:,2:])