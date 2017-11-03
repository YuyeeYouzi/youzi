lst=['Bart',123,None,'Lisa','Adam']
for n in lst:
    if isinstance(n,str):
        print('hello '+n+' !')
        print('hello {}'.format(n))


s='afgjolma'

for i in range(1,10):
    for j in range(1,i+1):
        print('{}*{}={}'.format(j,i,j*i).center(9),end='')
        print('{}*{}={}'.format(j,i,j*i),end='\t')
    print()


'''1,去掉names中元素两边的空格并生成一个新的列表
names={' ton', ' jack', 'mary',' bob '}
不用strip'''
names={' ton', ' jack', 'mary',' bob '}
new_names=list()
for name in names:
    #striped_name=name.strip()
    striped_name=' '
    for n in name:
        if n !=' ':
            striped_name+=n
    new_names.append(striped_name)
print(new_names)

#2.
lst=[3,7,[0,[9,5],7],1]
#lst2=[3,7,0,9,5,7,1]#扁平化处理
#'abc-fdg-'.replace('-'.'+')
import re
re sub()
lst_str = str(lst)#字符串形式'lst=[3,7,[0,[9,5],7],1]'
#lst_str2=lst_str.replace('[','').replace(']','')
lst_str2=re.sub(r'[\[/]]','',lst_str)
print(lst_str2)
lst3=lst_str2.split(',')
print(lst3)
lst2=[int(n) for n in lst3]
print(lst2)