import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns
from sklearn.preprocessing import MinMaxScaler, StandardScaler # 数据规范化
from sklearn.cluster import KMeans
from mpl_toolkits.mplot3d import Axes3D 
sand = plt.figure().add_subplot(111,projection='3d')

df = pd.read_csv(r'D:\Documents\Tencent Files\2193116788\FileRecv\consumption_data.csv')
df = df.ix[:,['R','F','M']]
#plt.scatter(df.R,df.M) #f<40 r<100 m<25000
#plt.show()#

# 过滤掉异常值
df = df[(df.F<40) & (df.R<44) & (df.M<2500)]
#sns.boxplot(y=df.R)# 竖过来，横的就是不写y=
#plt.show()

# 数据规范化 ，不然数据相差很大
ss = StandardScaler() # 标准规范化
#ss = MinMaxScaler() # 最后结果只是0-1  最大最小规范化
scaled = ss.fit_transform(df)
print(scaled)

model = KMeans(n_clusters=5,max_iter = 40)
# n_clusters=3 model.inertia_=1449
# n_clusters=5 model.inertia_=929
# n_clusters=7 model.inertia_=697
# n_clusters=9 model.inertia_=598
# n_clusters=11 model.inertia_=520
# 点越多效率越慢
# 肘方法 估计聚类分多少类
#x = range(3,40)
#inertias = []
#for n in range(3,40):
#    inertia = KMeans(n_clusters=n).fit(scaled).inertia_
#    inertias.append(inertia)
#
#plt.plot(x,inertias)
#plt.show()

model.fit(scaled)
print('-------------')
print(model.inertia_)
#print(model.labels_) # 聚类之后的标签
#df['分类']=model.labels_
#print(df)
#df.to_csv('temp.csv')
#
# 聚类 ，每个类型的中心点
center = model.cluster_centers_ # 因为不是原数据
print(ss.inverse_transform(center)) # 之前用什么方法转过去，就用什么方法转过来
d = ss.inverse_transform(center) # fit_transform
sand.scatter(df.R,df.F,df.M,c=model.labels_) # 分成不同的颜色，c 如果是df.R的话，就是根据df.R分颜色，现在就是根据labels分颜色
sand.set_xlabel('R')
sand.set_ylabel('F')
sand.set_zlabel('M')
#plt.show()

# 每个类别有多少数量
df['分类'] = model.labels_
count = df.groupby('分类').size()
print(count)
f = pd.DataFrame(d,columns = list('RFM'))
print(f)
f['分类数量']=count
print(f) #-------------------------------------------------->我自己写的

print(pd.Series(model.labels_))
labels = pd.Series(model.labels_)
label_cnt = labels.value_counts()
df_centers = pd.DataFrame(d)
#print(label_cnt)
#print(df_centers)
#df_label_cnt = df_centers.add(label_cnt,axis=1)
df_cnt = pd.concat([df_centers,label_cnt],axis=1)
df_cnt.columns = list('RFM')+['类别数量'] # 老师用的是下面这个，但是我加了一列，不能用
#df_cnt.columns = list(df.columns)+['类别数量']
#print(df_centers)
print(df_cnt) #----------------------------------------------->老师写的