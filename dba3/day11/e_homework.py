# recommend_pokemon_byname(pokemon_name):
#  1   100
# recommend_pokemon_byattr(hp,
#       attack,defense,spatk,spdef,speed)
# 推荐属性相似的3个pokemon
# 只考虑HP Attack  Defense Sp. Atk Sp. Def Speed

# 返回3个类似属性的pokemon

import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns
from sklearn.preprocessing import MinMaxScaler, StandardScaler # 数据规范化
from sklearn.cluster import KMeans
df = pd.read_csv(r'D:\Documents\Tencent Files\2193116788\FileRecv\Pokemon.csv')
df.columns = df.columns.str.lower() # 将columns都转成小写
#print(df.head())
df = df.ix[:,['attack','defense','sp. atk','sp. def','speed']]

# 画盒型图，过滤掉异常值
#sns.boxplot(y=df.attack) #attack<170
#sns.boxplot(y=df.defense) #defense<150
#sns.boxplot(y=df['sp. atk']) # sp. atk<165
#sns.boxplot(y=df['sp. def']) # sp. def<150
#sns.boxplot(y=df.speed) # speed<150
#plt.show()
df = df[(df.attack<170) & (df.defense<150) & (df['sp. atk']<165) & (df['sp. def']<150) & (df.speed<150)]
ss = StandardScaler()
#ss = MinMaxScaler()
scaled = ss.fit_transform(df)
print(scaled)

# 肘方法 估计聚类分多少类

#x = range(3,40)
#inertias = []
#for n in range(3,40):
#    inertia = KMeans(n_clusters=n).fit(scaled).inertia_
#    inertias.append(inertia)
#
#plt.plot(x,inertias)
#plt.show()
model = KMeans(n_clusters=10)
model.fit(scaled)
print(model.inertia_) # 可能是分10类
# 聚类 ，每个类型的中心点
center = model.cluster_centers_ # 因为不是原数据
print(ss.inverse_transform(center)) # 之前用什么方法转过去，就用什么方法转过来