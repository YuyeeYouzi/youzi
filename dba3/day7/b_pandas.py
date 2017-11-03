#pandas 主要有三种类型
#对应于numpy 一维      二维      三维
#            Series  DataFrame   Panel
#          Pan Da S
#          
import numpy as np
import pandas as pd

scores = [77,45,76,37,17,75]
english_scores = [53,67,18,82,17,90]
s = pd.Series([1,3,5,6]) # 构建一个series
print(s,type(s)) 
print(s[1])
s = pd.Series()
s=pd.Series(scores,index=list('abcdef'))
print(s)
print(s,s['b'],s[1])
print('----------------------')
print(s.values,type(s.values))
print(s.shape)
print(s.index) #这个是可迭代对象
for name in s.index:
    print(name)

s2 = pd.Series(english_scores,index=s.index)
print(s2)
print(s2['a':'d']) # 这边没有包含不包含问题 用标签都包含的
print(s2[0:4]) # 用默认索引，这边的4还是不包含的

#s2 = pd.Series(english_scores,index=[1,2,3,4,5,6])
#print(s2)
#print(s2[4]) # 这种时候用的是自己定义的，不是默认的
#print(s2[0:4]) # 索引还是默认的，和单个的不一样
print(s2.sum(),np.sum(s2)) # 两种写法都可以
print(s2.mean())
print(s2[ ['a','e','d'] ]) # 选择多个，但是只能传一个，所以用列表
s2['b':'c']=99
print(s2)

#bc = s2['b':'c']
#print(bc)
#s2[:] = 0
#print(bc) # 也会改变
bc1 = s2['b':'c'].copy()
print(bc1)
#s2[:] = 0
print(bc1) #不会改变 深拷贝
print(s2)
print(s2.unique())
print(s2+1)
print(s2>60)
print(s2[s2>=60])
s60 = s2[s2>=60]
print(s60[1])

print('---------================----------------')
print(np.sqrt(s60))
print('c' in s60)

# 把字典转化为一维series
scores = {'cat':235,'tom':673,'pig':321}
scores = pd.Series(scores)
print(scores)

# 一维series（索引没有重复）转化为字典  series本身索引是可以重复的
#print(scores.values)
#print(scores.index)   我自己写的
print(dict(zip(scores.index,scores.values))) #------------------------->1

#if n in scores: #if中，n判断的就是索引
for n in scores: #for中查的是值          所以在if和在for中是有区别的
    print(n)
new_scores={}
for n in scores.index: #老师教的
    #print(n)
    new_scores[n] = scores[n]
print(new_scores) #---------------------------------------------------->2

# 生成式  老师教的
new_scores2 = {name:scores[name] for name in scores.index}
print(new_scores2) #---------------------------------------------------->3

print('-----------------------------------------')
print(scores)
scores.index = list('abc')
print(scores)
print(scores.value_counts(),'1111111111111')

scores_dict={'cat':None,'tom':673,'pig':321,'vv':456}
s = pd.Series(scores_dict)
print(s)
print(s.isnull())
print('-----------')
print(s.notnull())
print('-----------')
print(np.isnan(s))

