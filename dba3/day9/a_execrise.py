import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns
plt.rcParams['font.sans-serif'] = ['SimHei'] # 指定默认字体
df = pd.read_csv(r'D:\Documents\Tencent Files\2193116788\FileRecv\Pokemon.csv')

df.columns = df.columns.str.lower()
# legendary宠物的数量
print(df[df.legendary==True].shape[0])

df = df.set_index(df.name)

df = df.drop('name',axis=1) # 删除列
#print(df)
Pikachu = df.loc['Pikachu']
print(Pikachu)

# ==================这两种结果一样==========================
# 用set
type1 = df['type 1'].unique()
type2 = df['type 2'].dropna().unique() # 去除nan的再求unique
all_type = set(type1) | set(type2) # 集合
print(all_type)

# 用numpy集合逻辑
#np.union1d([type1,type2])
print(np.union1d(type1,type2))
# ============================================================

fire_dragon = df[((df['type 1']=='Fire' )& (df['type 2']=='Gragon'))|
                   ((df['type 2']=='Fire' )& (df['type 1']=='Gragon'))
                   ]
print(fire_dragon)

# 找到hp最低的宠物和他的hp量
print(df['hp'].idxmin(),df['hp'].min())

# 某类别中某属性最高的宠物
typefire = df[(df['type 1']=='Fire') | (df['type 2']=='Fire')]
print(typefire.attack.idxmax(),'*************')
print(typefire.sort_values(by='attack')[-3:]) #tail tail(3)

# 某类型有多少种
type1=df['type 1'].value_counts()
type2=df['type 2'].value_counts()
total=type1+type2
print(total['Fire']) # Fire是index

print('-----------------------------------------')
#strong = df.sort_values(by='total',ascending=False)
#strong = strong.drop_duplicates(subset=['type 1'],keep='first')
#print(strong)


# 画图
# plt.plot
def hist():
    bins = range(0,200,20) # start end width
    plt.hist(df['attack'],bins,width=16) #,color='r') # hist是柱状图
    plt.xlabel('攻击力')
    # 画一条竖直的线  axhline 水平线
    #plt.axvline(40,color='red')
    plt.axvline(df.attack.mean(),color='red',linestyle='dashed')# ,color='red'
    plt.ylabel('个数',rotation=0)
    plt.show()

#hist()
#
#
#(1,1)  (1,2) (3,3)
# scatter(所有X的值，所有y的值)
#plt.scatter([1,1,3], [1,2,3])
#plt.xlim(0, 5) # 坐标轴的范围
#plt.ylim(0, 5)
#plt.show()
# 散点图
def scatter():
    fire = df[df['type 1']=='Fire']
    water = df[df['type 1']=='Water']
    glass = df[df['type 1']=='Grass']
    plt.scatter(fire.attack,fire.defense,label='fire',color='r',marker='*')
    plt.scatter(water.attack,water.defense,label='water',color='#3344ff',s=10) # s=size
    plt.scatter(glass.attack,glass.defense,label='glass',color='#669856',marker='+')
    plt.xlabel('hp')
    plt.ylabel('speed') # 坐标名称
    plt.legend() # 右上角的注释
    plt.show()

#scatter()


def jointplot():
    fire = df[ df['type 1'] == 'Fire' ]
    water = df[ df['type 1'] == 'Water' ]
    sns.jointplot(x=fire.attack, y=fire.defense)
    sns.jointplot(x=water.attack, y=water.defense)
    plt.show()

#jointplot()

#sns.set_style('darkgrid') # white whitegrid black blackgrid
##print(df['type 1'].value_counts())
#sns.countplot(x=df['type 1'])
#plt.show()  # 计数图

# 盒形图 都是真实的值
def boxplot():
    df2 = df[['hp','attack','defense','sp. atk','sp. def','speed']]
    sns.boxplot(data=df2,whis=1.5) # whis默认就是1.5，可以不写
    print(df.hp.sort_values().values)
    plt.show()  

#boxplot()

def boxplot2():
   
    sns.boxplot(x='type 1',y='attack',data=df) 
    #print(df.hp.sort_values().values)
    plt.show()  

#boxplot2()

df1=df['type 1'].value_counts()
lst=df1.index
size=df1.values
print(size)
print(lst)
plt.pie(size,labels=lst,autopct='%1.1f%%') # ,explode=explode
plt.axis('equal') 
plt.title('不同类型宠物')
plt.show()#    ----------------------------------------------->我自己写的

def boxplot3():
    # 筛选一下数据，
    data = df[df.generation.isin([1,2])]
    data = data[data['type 1'].isin(['Fire', 'Water'])]
    #
    sns.violinplot(x='type 1', y='speed', 
        data=data, hue='generation', split=True)
    #plt.show()
#boxplot3()


counts = df.generation.value_counts()
counts['others']=counts[3:].sum()
counts=counts[[1,2,3,'others']]
#print(counts)
#print(counts.sort_index())
plt.pie(counts.values,explode=(0.1,0,0,0),autopct='%1.1f%%',labels=counts.index)
plt.axis('equal') 
#plt.show()

df = df.groupby(['generation', 'type 1']).count().reset_index()
print(df,'!!!!!!!!!!!!!!!!!!')
df = df[['generation','type 1','total']]
df = df.pivot(
        index='generation', 
        columns='type 1',
        values='total'
    )
df = df[['Fire','Water','Dragon']]
print(df)
df.plot(marker='*')
plt.show()