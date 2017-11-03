#numpy  处理矩阵
#pandas  基于numpy  数据处理
#scikit-learn  python机器学习(深度学习 tensorflow theano keras)
#malplotlib  seaborn  基于前者

import numpy as np 
import random

arr = np.array([1,2,3])
arr1 = np.array([[1,2],[3,4]])
arr = np.array([(1,2),(3,4)]) #和上面一样
arr = np.array([[1,2],
                [3,4],
                [3,4,5]])
arr2 = np.array([[1,2],
                 [3,4],
                 [3,4]],dtype=np.float32
                 )
print(arr,type(arr))
print(arr,'维度：',arr.ndim)
print(arr.shape)
print(arr1.shape) #shape返回的是元组
print(arr2.dtype)
print(arr2)
#arr = np.array(range(1,11))
arr = np.arange(1,7)

print(arr,arr.shape)
arr2 = arr.reshape(2,3)
arr3 = arr.reshape(2,3,1)
print(arr2,arr2.shape)
print(arr3,arr3.shape)
arr = np.arange(1,9)
arr = arr.reshape(-1,2)
print(arr)

arr = np.zeros((3,4))
print(arr)
arr = np.ones((2,3,4))
print(arr)

print('-------------------random---------------')
print(np.random.rand(2,3))
print(np.random.rand())

print('---------------randint-----------------')
print(np.random.randint(3,size=(3,2))) #0~2中取
np.random.seed(13) #seed后面产生固定的随机数
arr = np.random.randint(3,8,size=(3,2)) #伪随机数
print(arr) #3~7中取
np.random.shuffle(arr)  #没有返回值
print(arr)

arr=np.random.randint(1,10,size=(5,3))
print(arr)
np.random.seed()
np.random.shuffle(arr)
print(arr)

arr = np.random.randint(1,10,size=(3,3))
print(arr)

print('--------随机产生不重复1-9的数，组成3*3的二维数组----------------------')
arr = np.arange(1,10) #不会重复1~9
np.random.shuffle(arr)
print(arr) #(9,)
arr2 = arr.reshape(3,3)
print(arr2)

a = np.arange(12).reshape(3,4)
i=np.array([[0,1],[1,2]])
j=np.array([[2,1],[3,3]])
a[i,j]
print(a)
print(a[i,j])
a = np.arange(12)**2
i=np.array([1,1,3,8,5])
j=np.array([[3,4],[9,7]])
print(a)
print(a[i])
print(a[j])
a = np.arange(10)
print(a>5)
print(a[a==5])