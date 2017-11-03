import numpy as np 
import pandas as pd 
df = pd.read_csv(r'D:\workspace\dba3\day10\tmp.csv',encoding='gbk')
print(df)
df = df.drop(['中专'],axis=1)
print(df.head())
df.to_csv(r'D:\workspace\dba3\day10\tmp.csv')