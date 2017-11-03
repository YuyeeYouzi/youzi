import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns

# 线性回归
from sklearn.linear_model import LinearRegression
# 训练集和测试集分两部分
# 交叉检验
from sklearn.model_selection import train_test_split
# 以身高预测体重
dct = {'height':(171,175,159,155,152,158,154,164,168,166,159,164,
                    171,175,159,155,152,158,154,164,168,166,159,164),
        'gender':(0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1),
        'weight':(57,64,41,38,35,44,41,51,57,49,47,46,
                    57,64,41,38,35,44,41,51,57,49,47,46 )}
df = pd.DataFrame(dct) # 构造一个df
# 训练集是一个二维特征集，哪怕只有一个特征，[[5],[7],...] 变成二维的
#x_train = pd.Series(df.height) #Reshape your data either using array.reshape(-1, 1) if your data has a single feature or array.reshape(1, -1) if it contains a single sample.
x_train = df.height.values.reshape(-1,1) 
#print('***')
#print(df)
#print(df.height.values)
#print(df.height)
#print(type(df.height.values))
#print(x_train)
#print(type(x_train))
y_train = df.weight

lr = LinearRegression()
lr.fit(x_train,y_train) # fit学习  model.fit(x_train)

# 预测
print(lr.predict(162)) # 正常就是lr.predict([[162]])
print(lr.predict([[162],[180]]))

y_pred = lr.predict(x_train)
# ax+b=y
print(lr.intercept_) # 截距
print(lr.coef_) # 斜率
b = lr.intercept_
a = lr.coef_
# 画拟合后的直线
plt.plot(df.height,y_pred,marker='o',color='r') #------------------>1
plt.plot(df.height,a*df.height+b,marker='o',color='r') #----------->2
plt.scatter(df.height,df.weight)
plt.show()

print('----------------加一个特征值性别--------')
x_train = df[['height','gender']]
print('****')
print(type(df.height))
print(x_train)
y_train = df.weight
lr = LinearRegression()
lr.fit(x_train,y_train)
print(lr.predict([[163.5,0],[180,1]])) # 这里有几个就返回几个预测结果，而且y的这个值是一维的

y_pred = lr.predict(x_train)
print(np.round(y_pred,1)) # 预测的返回及结果是ndarray

# 验证结果
# 真实结果减去结果值，平方
cost = ((y_train-y_pred)**2).sum()
print(cost)
# 比方说第二种方法的cost比较小，说明第二种方法拟合的比较好

# ax1+bx2+c=y
# weight = 1.16*height+4*gender-133
a,b = lr.coef_ 
c = lr.intercept_
print(a,b,c)

from mpl_toolkits.mplot3d import Axes3D
sand = plt.figure().add_subplot(111,projection='3d')
sand.scatter(df.height,df.gender,df.weight)
#sand.plot(df.height,df.gender,df.weight)
sand.set_xlabel('height')
sand.set_ylabel('gender')
sand.set_zlabel('weight')
#plt.show()

print('---------------各种推销方式对销售额的影响-------------------')
df = pd.read_csv(r'D:\Documents\Tencent Files\2193116788\FileRecv\Advertising.csv')
print(df)
# 训练集
x_train = df[['TV','Radio','Newspaper']]
y_train = df.Sales
# 学习
lr = LinearRegression()
lr.fit(x_train,y_train)
y_pred = lr.predict(x_train) # 得到y的预测值
a,b,c = lr.coef_ # 斜率
d = lr.intercept_ # 截距
print(a,b,c,d)

#a1*tv+a2*radio+a3*newspaper+b=y
a1,a2,a3=lr.coef_ #coef_返回的是一个一维ndarray
d = lr.intercept_
print(a1,a2,a3,b)

# 检验结果
y_pred = lr.predict(x_train)
corr = pd.Series(y_pred).corr(y_train)
#corr = y_pred.reshape(-1,1).corr(y_train) # 'numpy.ndarray' object has no attribute 'values'
                                            #'numpy.ndarray' object has no attribute 'corr'
print(type(y_pred)) # 这个也是ndarray，之前就是因为也是这个，所以用reshape，这里所有的值都在一个[]中
print(type(y_train)) # Series，虽然一维，但是每个值都是拿的出来的，
print(corr) # 所以上面的预测值耀Series一下

#x_train = df.iloc[:150,:][['TV','Radio','Newspaper']]
#y_train = df.iloc[:150,:]['Sales']
#
#x_train = df.iloc[150:,:][['TV','Radio','Newspaper']]
#y_train = df.iloc[150:,:]['Sales']
print('------------验证测试分开-----------------')
X = df[['TV','Radio','Newspaper']] #x是矩阵   特征
y = df.Sales   # 标签
# 交叉验证  过拟合overfit  欠拟合
(X_train,X_test,y_train,
    y_test)=train_test_split(X,y,train_size = 0.6,test_size=0.4) 
    # 默认75 训练  25 测试
    # train_size,test_size 和不能大于1
    # 这里的0.6的值都是随机取的，所以每次取的值都不一样
lr2 = LinearRegression()    
lr2.fit(X_train,y_train)
print(lr2.coef_)

# 用test集验证结果
y_pred = lr2.predict(X_test)
print(y_pred)
corr = pd.Series(y_pred).corr(y_test)
cost=((y_test.values-y_pred)**2).sum()
print(y_train)
print(cost)

# 如果gender中'0'全是'女','1'全是'男'