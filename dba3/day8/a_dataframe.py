import numpy as np
import pandas as pd

np.random.seed(5)
df = pd.DataFrame(np.random.randint(1,10,size=(10,4)))
df.columns = list('ABCD')
#df.index = list('')
#df = pd.read_csv(r'D:\Documents\Tencent Files\2193116788\FileRecv\tai.csv')
##print(df.head)
#df = set_index(df.name)
#print(df.name)
print(df.iloc[2:5])
print(df.iloc[[3,6],[1,2]])
print(df.ix[df.A>5,['C','D']])
print(df.loc[df.A>5,['C','D']]) # 用标签的
print(df)
print(df.ix[4]) #选标签 默认是选标签
print(df.iloc[4]) #选索引
print(df.A.value_counts())
print('--------------------------')
print(df.sum()) # 纵向求和

#df.ix['sum']=df.sum() #添加一行
#print(df)
#df.sum(axis=1)
#df['sum'] = df.sum(1) #添加一列  ##########################注意添加一行和添加一列的区别
#print(df)

print('-----------',df)
df.ix[1,1]=np.nan  #这里用的是索引,不是标签
print(df)
print(df.sum(axis=1,skipna=False))

print(df.idxmax(1))  #最大值的标签  默认是0 这里的0和1是axis

#df.reset_index(np.array('abcdefghij'))
df=df.set_index(pd.Series([1,2,3,4,5,6,7,8,9,10])) # 修改index，list不能用
df.index=[1,2,3,4,5,6,7,8,9,10]
#print(df)
print(df)
print(df.ix[1:3,1:3])
print(df.sort_values(by='A'))
print(df.A.quantile(0.2)) # 分位数
df['A2'] = df.A.rolling(3).sum()
print(df)
print(df.A.corr(df.B)) #相关系数
print(df.A.cov(df.B)) #协方差
users = pd.read_csv(r'D:\Documents\Tencent Files\2193116788\FileRecv\users.csv')
#print(users)
#print(users.head(20))

print(len(users.index))
print(users.shape[0]) #几条数据
print(len(users.columns))
print(users.shape[1]) #几个字段
print(users.occupation)

print(users.occupation.values) # 这个不好，有重复
print(users.occupation.unique().size)
print(users.occupation.unique().shape[0])
print(users.occupation.value_counts())
print('-------------=========================--------------')
print(users.age.mean())
print(users[users.gender=='M'].age.mean())
print(users.age[users.gender=='M'].mean())