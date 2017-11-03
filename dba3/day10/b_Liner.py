import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns

# 线性回归
from sklearn.linear_model import LinearRegression
from sklearn.externals import joblib 
# 训练集和测试集分两部分
# 交叉检验
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder

dct = {'height':(171,175,159,155,152,158,154,164,168,166,159,164,
                    171,175,159,155,152,158,154,164,168,166,159,164),
        'gender':('女','女','女','女','女','女','女','女','女','女','女','女','男','男','男','男','男','男','男','男','男','男','男','男'),
        'weight':(57,64,41,38,35,44,41,51,57,49,47,46,
                    57,64,41,38,35,44,41,51,57,49,47,46 )}

df = pd.DataFrame(dct) # 构造一个df
# 训练集是一个二维特征集，哪怕只有一个特征，[[5],[7],...] 变成二维的

le = LabelEncoder()
# 用labelEncoder把字符串转成数字
print(le.fit_transform(df.gender.values))
#df[df=='女']
print(df.head())

df = pd.read_csv(r'D:\Documents\Tencent Files\2193116788\FileRecv\51jobs.csv',
                encoding='gbk'
    )
print('--------------1------------')
#def foo(addr):
#    return addr[:2]
#df['addre'] = df['工作地点'].apply(foo) #--------------------------->我自己写的
def get_place(jobplace):
    #if '-' in jobplace:
    #    return jobplace.split('-')[0]
    #else:
    #    return jobplace
    return jobplace.split('-')[0] if '-' in jobplace else jobplace

def get_salary(salary):
    if '万/月' in salary:
        salary = salary[:-3].split('-')
        rtn = (float(salary[0])+float(salary[1]))/2*10000
    elif '千/月' in salary:
        salary = salary[:-3].split('-')
        rtn = (float(salary[0])+float(salary[1]))/2*1000
    elif '元/天' in salary:
        rtn = float(salary[:-3])*21.75
    elif '万/年' in salary:
        salary = salary[:-3].split('-')
        rtn = (float(salary[0])+float(salary[1]))/2*10000/12
    else:
        rtn = None
    return rtn

df = df.dropna()
df['地区'] = df['工作地点'].apply(get_place)
df['月薪'] = df['薪资'].apply(get_salary)
#print(df)
mean_salary = df.groupby('地区')['月薪'].mean()
print(mean_salary.idxmax(),mean_salary.max())


print('--------------2------------')
df_shanghai = df[df['地区']=='上海']
mean_salary = df_shanghai.groupby('学历')['月薪'].mean()
print(mean_salary)

# 使用labelEncoder
le = LabelEncoder()
df['地区']=le.fit_transform(df['地区'].values)
print(le.classes_)
#print(df['地区'])
###############################这两个选一个########################

# 哑变量
# 把df['学历']用哑变量表示
xueli = pd.get_dummies(df['学历'])
# 再拼接到原来的dataframe
df = pd.concat([df,xueli],axis=1)
df.to_csv('tmp.csv')
#print(xueli)


def predict_salary(xueli,place,exp):
    return salary