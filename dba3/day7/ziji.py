import numpy as np
import pandas as pd
data = {'name':['tom','bob','fog'],
        'phone':[123,444,555],
        'year':2017,
        'xuehao':pd.Series([4,6,8])
}
df = pd.DataFrame(data)
print(df)

np.random.seed(6)
df = pd.DataFrame(np.random.randint(10,size=(6,4)),index=list('abcdef'))
df.columns=list('ABCD')
print(df)
print(df.values)
print(df.shape)
print(df.describe())
print(df.sum(0))
print(df.sum(1))
#d=df.sort_values(by='G')
#print(d)
##d=df.sort_values(by='g')
##print(d)#
#print(df['a':'h'])
print(df['a':'b'],"-------------")
print(df[['A','B']])
print(df.loc[:,'A':'B'])
print(df.iloc[:,1:2])
print(df[df.A>5])
print(df[df>5])
#print(df[df.a==2])
print(df['D'].isin([2,3,4]))
print(df[df['D'].isin([2,3,4])])
print('----------------')
print(df.D.shift(1),"-------------")
df = pd.DataFrame(np.arange(20).reshape(5,4),columns=list('abcd'))
df.loc[0:3,'d']=np.nan
print(df)
print(df.dropna(1))
print(df.fillna({'d':5}))
s1 = pd.Series(range(4),index=list('abce'))
s2 = pd.Series(range(4),index=list('bcdf'))
print(s1)
print(s2)
print(s1+s2)
df1 = pd.DataFrame(np.arange(9).reshape(3,3))
df2 = pd.DataFrame(np.arange(16).reshape(4,4))
print(df1)
print(df2)
print(df1+df2)
df = pd.DataFrame(np.arange(16).reshape(4,4))
s = pd.Series([3,5,8])


print(s)
print(df-s)
print(df.sub(s,axis=0))
print(df>1)
print(df)
print(df[0])
df = pd.DataFrame(
    {'A':['foo','bar','foo','bar','foo','bar','foo','foo'],
     'B':['one','one','two','three','two','two','one','three'],
     'C':np.random.randint(8,size=8),
     'D':np.random.randint(8,size=8)
    }
    )  
print(df) 
print(df.groupby('A').sum()) 
print(df.groupby(['A','B']).sum())
