import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns
# 读取51job.csv
# 1 哪个城市平均月薪最高
# 2 上海各学历的平均月薪
# 3 黄金价格每天变化的范围分布
df = pd.read_csv(r'~/Desktop/dba3/51jobs.csv',
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
#le = 
