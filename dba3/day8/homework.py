# 1.选出既是火又是龙的宠物  考虑type1 type2
# 2.找出HP最高的宠物，名字， HP量是多少
# 3.找出每个类别找出HP最高的宠物，名字， HP量是多少
# 4.type1 type2 一共有多少种不同种类
# 5.Defense大于150，的  平均speed
import numpy as np 
import pandas as pd

poke = pd.read_csv(r'D:\Documents\Tencent Files\2193116788\FileRecv\Pokemon.csv')
print(poke)

#lst=['Fire','Dragon']
#def foo(type):
#    if type==lst;
#        return type
#poke['Type 1']
#print(po)

print('---------------1---------------')
po1 = poke[(poke['Type 1']=='Fire') & (poke['Type 2']=='Dragon')]
po2 = poke[(poke['Type 1']=='Dragon') & (poke['Type 2']=='Fire')]
po = pd.concat([po1,po2],axis=0)
print(po)

print('---------------2----------------')
pHP=poke.sort_values(by='HP',ascending=False).head(1)
print(pHP)
print(pHP.Name,pHP.HP)

print(poke.HP.max())

print('--------------3----------------')
print(poke['Type 2'])
#p1 = poke['Type 2'].sort_values(by='HP',ascending=False)
#p1 = p1.head(1)
#print(p1)

print('---------------4------------------')
#m = users.groupby(['occupation','gender'])['age'].mean() # 复合索引
#print(m)
#print(m.index)
#
##以条件分组
#m = users.groupby([users.age>50,'occupation','gender'])['age'].mean()
#print(m)

pcount1 = poke.groupby(['Type 1']).count().Name
#pcount1 = pcount1.value_counts()
print(pcount1)
pcount2 = poke.groupby(['Type 2']).count().Name
print(pcount2)

print('---------------------5----------------------')
p5 = poke.groupby([poke.Defense>50])['Speed'].mean()
print(p5)