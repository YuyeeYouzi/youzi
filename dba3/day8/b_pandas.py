import numpy as np
import pandas as pd

np.random.seed(5)
df = pd.DataFrame(np.random.randint(1,10,size=(10,4)))
df.columns = list('ABCD')
df.iloc[[2,4,6],[1,3]] = np.nan
print(df)
print(df.dropna())
print(df.dropna(1))

# 填充缺失值
#df = df.fillna(0)
#print(df)

# 针对不同的列填充缺失值
#df = df.fillna({'B':777,'D':888})
#print(df)
#
# 填充平均值
dct = {'B':df.B.mean(),'D':df.D.mean()}
df = df.fillna(dct)

# 保留小数
df.B = np.round(df.B,1)
df.D = np.round(df.B,1)
print(df)

print('---------------------------------')
# 相同索引的项分别计算，没有对应索引的返回nan
s1 = pd.Series([1,2,3,4],index = list('abcd'))
s2 = pd.Series([1,2,3,4],index = list('ccaa'))
print(s1+s2)
print(s1*s2)
print(df)
# dataframe和series相加
print(df+df.ix[9])

df2 = pd.DataFrame(np.random.randint(1,10,size=(5,3)))
df2.columns = list('ABC')
df3 = df+df2
print(df3)

print(df.add(df2,fill_value=0))
s = pd.DataFrame(np.random.randint(1,9,size=(2,6)),columns=list('abcdef'))
s2 = pd.Series([3,5,7,3,6,7],index=list('abcdef'))
s1 = pd.Series([3,6,1,3,2,2],index=list('aefjtk'))
s3 = pd.DataFrame(np.random.randint(1,9,size=(3,4)),columns=list('adrh'))
print(s2)
print(s)
print(s+s2,'**************')
#print(s.add(s2,fill_value=1))
print(s.add(s3,fill_value=0))
print(s1.add(s2,fill_value=0))
#print(s3)

def add_one(x):
    return x+1
#df.D = df.D.apply(lambda x:x+1)
print('---------------==================')
df.D = df.D.apply(add_one) # add_one运用在df.D的每个元素上
df.ix[0] = df.ix[0].apply(add_one) # 运用于每一行
df = df.applymap(add_one) # add_one运用到df的每个元素上
# 运用在df的行或者列上
#df['max-min'] = df.apply(lambda x:x.max()-x.min(),axis=1) 

print(df)

users = pd.read_csv(r'D:\Documents\Tencent Files\2193116788\FileRecv\users.csv')
def age_range(age):
    if 0<age<=8:
        return '儿童'
    elif age<14:
        return '青少年'
    elif age<30:
        return '青年'
    elif age<55:
        return '中年'
    else:
        return '老年'
def foo(occ):
    return occ[:3]
users['年龄段']=users.age.apply(age_range)
users['foo']=users.occupation.apply(foo)
users.to_csv('usersage.csv')

#def doo(zip_code):
#    if zip_code in (857,940,320,435):
#        return '移动'
#    elif zip_code in (152,981,913,520):
#        return '联通'
#    elif zip in (100,907,303,292):
#        return '电信'
#
#users['运营商']=users.zip_code.apply(doo)
#print(users) # --------------------------------------我写的不对

users['haoma'] = users.zip_code.apply(foo)
#users['haoma'] = users.zip_code.apply(lambda x:x[:3])
#print(users)
def doo(haoma):
    if haoma in ('857','940','320','435'):
        return '移动'
    elif haoma in ('152','981','913','520'):
        return '联通'
    elif haoma in ('100','907','303','292'):
        return '电信'
    else:
        return '其他'
users['运营商']=users.haoma.apply(doo)
print(users)
#print(list(zip([1,2,3],['a','b','c'])))