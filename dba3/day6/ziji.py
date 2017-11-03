import numpy as np
a = np.array([1,2,3])
print(type(a))
print(a.dtype)   #dtype
b = np.array([[1,2],[3,4,5]])
print(b)
print(b.ndim)  #维度
np.array(range(1,10))
s = np.arange(10).reshape(2,5) #numpy的方法是arange
#print(s)
#print(np.ones(1,2,3))#

a2 = np.ones((3,3))
a2 = np.ones([3,3])
print(a2)
print(a)
print(a**2)
print(a>4)
a*=3
print(a)
print(a[a>4])

np.random.seed(6)
ss=np.random.randint(1,10,size=(9,3))
print(ss)
print(ss>3)
print((ss>3).sum(1))