import numpy as np
import pandas as pd

d = pd.DataFrame(np.random.randn(4,5))
print(d)
df = pd.DataFrame(
    np.random.randint(1,10,size=(5,4)),
    index=list('abcde'),
    columns =list('ABCD')

    )
print(df)

# 键作为columns名
data = {'name':['tom','bob','dog'],
            'phone':[123,555,678],   #'phone':np.array([123,555,678])也可以
            'age':18

}
df = pd.DataFrame(data)
print(df)
print(df['name'],type(df.name))

dict_a = {'name':'tom','score':99,'age':15}
dict_b = {'name':'ttt','score':88}
dict_c = {'name':'aaa','score':[88,77]}
df = pd.DataFrame([dict_a,dict_b,dict_c])
print(df)
print('--------------选一列df.name--------------')
print(df.name) # 就是一个series
print('---------------选一行---------------')
print(df.ix[0],'----',df.ix[0].name)
print('----------追加一列----------')
df['phone'] = [235,457,866]
print(df)
df['score2'] = df.score*2
print(df)
print('-----------删除一列-----------')
df1 = df.drop('score2',axis=1) #有个返回值
print(df1) 
print('-----------删除一行-----------')
df1 = df.drop(0,axis=0) #有个返回值
print(df1) 
print('----------添加一行-----------')
df.ix[4] = [46,'fgf',45,763,56]  #和越不越界没关系
print(df)
print('------------删除两列-------------')
df = df.drop(['score','score2'],axis=1)
print(df)
print('-------')
print(df['name'],type(df['name']))  #返回Series
print(df[['name']],type(df[['name']])) #返回DataFrame
print(df[['name','phone']])  #返回DataFrame
