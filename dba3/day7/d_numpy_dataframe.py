import numpy as np
import pandas as pd

df = pd.DataFrame(
    np.random.randint(1,10,size=(18,4)),
    #index = list('abcdef'),
    columns=list('BADC')

    )

print(df.head(10))
print(df.tail(4))
print(df.describe())

'''

               A          B          C          D
count  20.000000  20.000000  20.000000  20.000000
mean    5.500000   4.100000   6.200000   5.750000
std     2.585384   2.573141   2.706717   2.074279  标准差
min     1.000000   1.000000   1.000000   1.000000
25%     3.750000   2.750000   4.500000   5.000000
50%     6.000000   3.000000   6.500000   6.000000
75%     7.250000   6.250000   9.000000   7.000000
max     9.000000   9.000000   9.000000   9.000000
'''
print(df.T)

'''
  0   1   2   3   4   5   6   7   8   9   10  11  12  13  14  15  16  17
A   6   4   7   3   4   5   9   7   6   5   8   1   7   2   8   2   1   1
B   6   7   2   4   7   2   9   5   1   9   9   9   9   6   3   8   1   4
C   3   9   2   6   2   2   4   8   7   4   1   2   8   6   6   8   9   6
D   4   4   6   7   5   2   2   2   4   6   5   2   4   6   3   6   5   5
'''
print(df.sort_index(axis=1)) #对行排序只要df.sort_index()
print(df.sort_values(by='A'))
print('---------二次排序--------')
print(df.sort_values(by=['A','B'])) # 二次排序

# 读取泰坦尼克号名单
df = pd.read_csv(r'D:\Documents\Tencent Files\2193116788\FileRecv\tai.csv')
print(df.head(10))
print(df.name)
#xingbie=df['sex'] 不对
print(df.sex.value_counts()) # -------------->名单里面有几个男的几个女的
male = df.sex.value_counts()['male']
print(male)
print(df.age.mean())
df = df.set_index(df.name)  #设置索引
print(df.head())
print(df.loc['Allison, Mrs. Hudson J C (Bessie Waldo Daniels)'])
#print(df.loc[5]) # 不行
print(df.ix[5])# ----------------------------------------------------------->loc+iloc的功能相当于ix
print(df.ix['Allison, Mrs. Hudson J C (Bessie Waldo Daniels)'])
print(df.iloc[0])
# select name,age from
print('----------------------------')
allison = df.loc['Allison, Mr. Hudson Joshua Creighton',['age','sex']]
print(allison)
allison = df.loc[['Allison, Mr. Hudson Joshua Creighton','Allison, Master. Hudson Trevor'],['age','sex']]
print(allison)
allison = df.loc['Allen, Miss. Elisabeth Walton':'Allison, Miss. Helen Loraine','age':'parch']
print(allison)

# iloc 和loc,用切片的话，loc是包括最后一个的，但是iloc是不包括的

print(df.shape[0]) # ----------->可以求总人数 len(df.index)
print((df.survived==0).sum())#------------>死亡人数
print(df.survived.value_counts()) # --------------->死亡人数
print((df.age>50).sum())
print(df[df.age>50]) #------------------------>显示所有年纪大于50的记录


