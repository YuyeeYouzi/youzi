import numpy as np
import pandas as pd

users = pd.read_csv(r'D:\Documents\Tencent Files\2193116788\FileRecv\users.csv')

m = users.groupby(['occupation','gender'])['age'].mean() # 复合索引
print(m)
print(m.index)

#以条件分组
m = users.groupby([users.age>50,'occupation','gender'])['age'].mean()
print(m)

# 求两门成绩都及格的，名字
math = {'cat': 55, 'bob': 75, 'pig': 85, 'tom': 50, 'dog': 66}
english = {'cat': 95, 'bob': 88, 'pig': 85, 'tom': 50}
df = pd.DataFrame([math,english])
df.index=['math','english']
print(df)#------------------------------->后面不会了

df = df.T
df1 = df[(df.math>=60) & (df.english>=60)]
print(df1.index)
print(df)
# 总分从高到低打印出来
df['sum'] = df['math'].add(df['english'],fill_value=0) 
print(df.sort_values('sum',ascending=False))

# #########拼接
print('--------------上下拼接------------')
np.random.seed(5)
df1 = pd.DataFrame(np.random.randint(1,10,size=(3,4)))
df1.columns = list('ABCD')

df2 = pd.DataFrame(np.random.randint(1,10,size=(4,4)))
df2.columns = list('ABCD')

df = pd.concat([df1,df2],axis=0)
df = df.reset_index().drop('index',axis=1) #修改index
df = df.set_index(pd.Series(list('abcdefg'))) # 修改index
print(df)

print('----------左右拼接----------')
# 左右拼接
df = pd.concat([df1,df2],axis=1)
print(df)

print('---------------')
df.columns = df.columns.str.lower()
df.index = list('abcd')
df.index = df.index.str.upper()
print(df)