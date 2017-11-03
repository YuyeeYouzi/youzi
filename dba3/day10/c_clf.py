import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns
from mpl_toolkits.mplot3d import Axes3D #画3d
# classify   Classifier  分类器  简称clf
from sklearn.tree import DecisionTreeClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split 
from sklearn.metrics import classification_report,confusion_matrix

# 读取数据
df = pd.read_csv(r'D:\Documents\Tencent Files\2193116788\FileRecv\Iris.csv')
#print(df.head())\


#plt.scatter()
# SepalLengthCm SepalWidthCm
seto = df[df.Species == 'Iris-setosa']
vers = df[df.Species == 'Iris-versicolor']
virg = df[df.Species == 'Iris-virginica']
plt.scatter(seto.SepalLengthCm,seto.SepalWidthCm,label='Iris-setosa')
plt.scatter(vers.SepalLengthCm,vers.SepalWidthCm,label='Iris-versicolor')
plt.scatter(virg.SepalLengthCm,virg.SepalWidthCm,label='Iris-virginica')
plt.legend()
plt.title('Sepal Length & Width')
plt.xlabel('length');plt.ylabel('width')
plt.savefig('sepal.png') # 保存图片
plt.clf() # clear
# 因为下面这张图是在上面那张图上追加上去的。所以要用清除 plt.clf()
#plt.scatter(seto.PetalLengthCm,seto.PetalWidthCm,label='Iris-setosa',s=10) # s 是点的大小
#plt.scatter(vers.PetalLengthCm,vers.PetalWidthCm,label='Iris-versicolor',s=10)
#plt.scatter(virg.PetalLengthCm,virg.PetalWidthCm,label='Iris-virginica',s=10)
#plt.legend()
#plt.title('Petal Length & Width')
#plt.savefig('petal.png') # 保存图片

#sand = plt.figure().add_subplot(111,projection='3d')
#sand.scatter(seto.SepalLengthCm,seto.SepalWidthCm,seto.PetalLengthCm,label='Iris-setosa')
#sand.scatter(vers.SepalLengthCm,vers.SepalWidthCm,vers.PetalLengthCm,label='Iris-versicolor')
#sand.scatter(virg.SepalLengthCm,virg.SepalWidthCm,virg.PetalLengthCm,label='Iris-virginica')
#sand.legend()
#sand.set_xlabel('sepallength');sand.set_ylabel('sepalwidth');sand.set_zlabel('petallength')
#plt.show()
# 零。数据简单变换
le = LabelEncoder()
df.Species = le.fit_transform(df.Species.values)

# 一。获得学习集
#X_train = df.drop(['Id','Species'],axis = 1)
#y_train = df.Species
X = df.drop(['Id','Species'],axis = 1)
y = df.Species
# 交叉验证
X_train,X_test,y_train,y_test=train_test_split(X,y,train_size=0.6,test_size=0.4)
##########################################################################################
#########################不同的分类器就是使用不同的方法， 其他都一样######################
##########################################################################################
# 二。学习
clf = DecisionTreeClassifier()# 用决策树分类器学习
#clf = GaussianNB() # 朴素贝叶斯
clf.fit(X_train,y_train)
# 预测一个分类
#n = clf.predict([[4.4,1.5,1.8,2.3]])
#print(le.inverse_transform(n))


# 三。看分类结果好坏
y_pred = clf.predict(X_test)

#print(help(classification_report))
print('-----------------')
print(classification_report(y_test,y_pred))  # 分类报告
# 混淆矩阵
cm = confusion_matrix(y_test,y_pred)
print(le.classes_)
print(cm)
print(clf.score(X_test,y_test))

plt.imshow(cm,cmap = plt.cm.Blues)
plt.xticks(range(3),le.classes_)
plt.yticks(range(3),le.classes_)
half = cm.max()/2
for i in range(cm.shape[0]):
    for j in range(cm.shape[1]):
        plt.text(j,i,cm[i,j],
        color = 'white' if cm[i,j]>half else 'black',
        size=20)
plt.show()
