import numpy as np 
import pandas as pd
# 线性回归
from sklearn.linear_model import LinearRegression
from sklearn.externals import joblib 
# 训练集和测试集分两部分
# 交叉检验
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder

df = pd.read_csv(r'D:\Documents\Tencent Files\2193116788\FileRecv\51jobs.csv',encoding='gbk')
df = df.dropna()

# 一、得到工作地点
def get_place(place):
    return place.split('-')[0] if '-' in place else place
df['地区'] = df['工作地点'].apply(get_place)
le = LabelEncoder()
df['place']=le.fit_transform(df['地区'].values)
#print(le.classes_)

## 这个不好，还是改成上面这种
#xueli = pd.get_dummies(df['学历'])
## 再拼接到原来的dataframe
#df = pd.concat([df,xueli],axis=1)

# 二、得到薪资
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

# 三、得到学历
df['xueli'] = le.fit_transform(df['学历'].values)


# 四、得到经验
def get_exp(exp):
    if '-' in exp:
       exp = exp[:-3].split('-')
       rtn = (float(exp[0])+float(exp[1]))/2.0

    elif '无' in exp:
        rtn = 0
    else:
        rtn = float(exp[0])
    return rtn

# **********************老师写的***************************
def get_exp(exp):
    '''
    3-4年经验  2年经验 无工作经验  10年以上经验
    '''
    if '-' in exp:
        e = exp[:-3].split('-')
        rtn = (float(e[0])+float(e[1]))/2
    elif exp=='无工作经验' :
        rtn = 0
    elif exp=='10年以上经验':
        rtn = exp[:2]
    else:
        rtn = exp[0]
    return rtn
# *********************************************************
df['salary'] = df['薪资'].apply(get_salary)
df['exp'] = df['经验'].apply(get_exp)



'''
X = df[['place','xueli','exp']]
y = df.salary

# 交叉检验
(X_train,X_test,y_train,y_test)=train_test_split(X,y,train_size = 0.6,test_size=0.4) 
'''
X_train = df[['place','xueli','exp']]
y_train = df.salary

lr = LinearRegression()
lr.fit(X_train,y_train)

y_pred = lr.predict(X_train)
a1,a2,a3 = lr.coef_ # 斜率
b = lr.intercept_ # 截距

if __name__ == '__main__':
    # 本科2  大专1  高中4 硕士3 中专0
    #print(df.head())
    #print(df[df['学历']=='中专'].xueli)
    #print(lr.predict([[1],[1],[1]]))
    print(lr.predict([[1,1,1]]))
    