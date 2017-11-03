a=1.243678
print(round(a,3))
print(pow(2,3))
print(pow(a,3))

import numpy as np
#np.random.seed(50)
a = np.random.randint(50,100,size=(9,3))
print(a)

scores=a[:,0]
print(np.where(scores>=60,'A','C'))
print(np.where(scores>=60,scores,'C'))
print(np.where(scores>=60,scores,np.nan))
print(np.where(scores>=60,(np.where(scores>=80,'A','B')),'C'))
# &
jige=np.where(scores>=80,'A','B')
print(np.where(scores>=60,jige,'C'))

print('----------------------------集合------------------------')
a = np.array([1,2,3,4])
b = np.array([4,5,5,7])
print(np.unique(b)) # 去重
print(np.intersect1d(a,b)) # 交集
print(np.union1d(a,b)) # 并集
print(np.in1d(a,b)) # 是否包含在y中

# 不管是几维，都当成一维处理
a2 = np.array([[1,2],[3,4]])
b2 = np.array([[1,2],[6,3],[7,8]])
print(np.intersect1d(a2,b2))
print(np.union1d(a2,b2))
print(np.in1d(a2,b2))

print('--------------------投掷硬币------------------')
import matplotlib.pyplot as plt
s = np.random.randint(0,2,size=500)
#print(s)
print(np.where(s==0,-1,1).cumsum())
#np.where(s==0,-1,s).cumsum()
s1=np.where(s==0,-1,1).cumsum()
plt.plot(s1) # 画图
#plt.show() # 显示图形

#画图例题
'''
import matplotlib.pyplot as plt
a = np.array([1,2,3,4,5,6])
plt.plot(a) # 画图
plt.show() # 显示图形
'''
# 一次投500次，投1000次
s = np.random.randint(0,2,size=(1000,500))
print(np.where(s==0,-1,1).cumsum())

# 投两个骰子，用穷举法得出结果的概率
a = np.random.randint(1,7,size=50)
b = np.random.randint(1,7,size=50)
c=a+b
print(a)
print(b)
print(c)
print((c>10).sum()/50)# -------------------------------------------->1
print((c==12).sum()/50)

c1 = np.random.randint(1,7,size=(2,100))
print(c1) 
l=0
for n in range(1,101):
    cc=c1[:,n-1:n].sum()
    if cc==12:
        l+=1  
print(l/100) #------------------------------------------------------->2

# 老师讲的
total=9999
np.random.seed(6) #为了看结果，所以保证结果不变。可加可不加
a = np.random.randint(1,7,size=(2,total))
#print((a[0]==a[1]).sum()) # 对子
duizi=(a[0]==a[1]).sum()
print(duizi/total,1/6)
dui6 = ((a[0]==a[1]) & (a[0]==6)).sum()
print(dui6/total,1/36)#---------------------------------------------->3

#ndarray
np.matrix
a = np.array([[1,2],[3,4]])  
b = np.array([[2,4],[1,2]]) 
print(a+b,'-------------')
print(a*b)
print(a.dot(b))
print(b.dot(a))
print(a.T)

