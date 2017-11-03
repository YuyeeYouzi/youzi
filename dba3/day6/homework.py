#    math    english  sports
#a   67  34  90
#b   87  98  98
#c   89  56  78
#d   54  54  56
#e   56  25  56
#f   67  78  87
#g   54  78  75
#h   98  57  56
#i   57  56  76
#
#1 求每个人的平均分和总分           
#2 求这个班每门课的平均分           
#3 求三门课都及格的人数            
#4 求有至少两门课及格的人数          
#5 sports有几个人大于90   
#6 几个人english分数 > math分数


import numpy as np
np.random.seed(50)
a = np.random.randint(50,100,size=(9,3))
print(a)

print('1.每个人的总分：',a.sum(axis=1))
print('1.每个人的平均分:',a.mean(axis=1))
print('2.每门课的平均分：',a.mean(axis=0))
b=(a>=60)
print(b)
lst=b.sum(axis=1)
count=0
for n in lst:
    if n == 3:
        count+=1
print('3.三门都及格的人数：',count)
print('3.三门都及格的人数：',(a>=60).sum(axis=1))
count1=0
for n in lst:
    if n>=2:
        count1+=1
print('4.至少有两门及格的人数：',count1)
ll=(a>=60).sum(1)
print('4.至少有两门及格的人数：',(ll>=2).sum())

sports=a[:,2:]
s = (sports>=90)
#print(a)
a_count=0
for n in s:
    if n:
        a_count+=1
print('5.sport成绩大于90的人：',a_count)
print('5.sport成绩大于90的人：',(sports>=90).sum())

english=a[:,1:2]
math=a[:,:1]
print(english)
print(math)
panduan=english>math
ss=0
for n in panduan:
    if n:
        ss+=1
print('6.english分数 > math分数：',ss)
print('6.english分数 > math分数：',panduan.sum())
