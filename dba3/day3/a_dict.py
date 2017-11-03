#scores={'michael':95,'bob':75}
##print(scores.items(),type(scores.items()))
##print(list(zip([1,2],[3,4])))
#for key in scores: #不需要scores.keys()
#    print(key,scores[key])
#
#for item in [('michael',95),('bob',75)]:
##for item in scores.items():
#    print(item)
#    print(item[0],item[1])
#for key,value in scores.items():
#    print(key,value)




scores={'michael':95,'bob':75,'tom':50}
#1.
#for key in scores:
#    if scores[key]<60:
#        scores[key]='不及格'
#        print(key,scores[key])
#    else:
#        scores[key]='及格'
#        print(key,scores[key])
#2.
for key,value in scores.items():
    if value<60:
        value='不及格'
        print(key,value)
    else:
        value='及格'
        print(key,value)

    #print(['及格' if value>=60 else '不及格'])
 




# 统计元音个数
#  我自己写的--------------------------------------1
text='fjvlkdjhgvazkdsliouaeoiewtgpbv'
#a_count=0
#e_count=0
#u_count=0
#i_count=0
#o_count=0
#for n in text.lower():
#    if n == 'a' or n =='A':
#        a_count+=1
#    elif n == 'e' or n=='E':
#        e_count+=1
#    elif n == 'u' or n=='U':
#        u_count+=1
#    elif n == 'i' or n=='I':
#        i_count+=1
#    elif n == 'o' or n=='O':
#        o_count+=1
##print('{} de count is {}'.format('a',a_count))
#counter={}
#counter.update({'a':a_count,'e':e_count,'u':u_count,'i':i_count,'o':o_count})
#print(counter)

# 老师讲的-------------------------------------------2
#counter={'a':0,'e':0,'u':0,'i':0,'o':0}
#yuanyin='aeuio'
#counter = dict.fromkeys(list(yuanyin),0)
#print(counter)
#for char in text.lower():
#    if char in yuanyin:
#        counter[char]+=1
#print(counter)






#大小写对应 = {'A':'a','B':'b'...}26个字母对应
dct={}
zimu='abcdefgjijklmnopqrstuvwxyz'
# 我自己写的-------------------------------------1
for k in zimu:
    value=k.upper()
    dct.update({value:k})
print(dct)
# 老师教的---------------------------------------2
for k in zimu:
    dct[k.upper()]=k
print(dct)
# 老师教的---------------------------------------3
dct=dict(zip(zimu.upper(),zimu))
print(dct)


#颠倒键和值
scores={'michael':95,'bob':75,'tom':50}
# 我自己写的------------------------------------1
scores2={}
for k,v in scores.items():
    print(k,v)
    scores2[v]=k
print(scores2)
# 老师教的---------------------------------------2
# 用字典
scores3 = dict(zip(scores.values(),scores.keys()))
print(scores3)








# 键值颠倒，值有重复
scores={'michael':95,'bob':75,'tom':50,'cat':50}
#scores2 = {50:['tom','cat'],75:['bob']} 用列表放值
#lst=[]
#for k in scores:
#    print(scores[95])
# 不会，老师讲的--------------------------------------1
scores2=dict.fromkeys(scores.values())
print(scores2)
for name,score in scores.items():
    if isinstance(scores2[score],list):
        scores2[score].append(name)
    if scores2[score]==None:
        scores2[score]=[name]
print(scores2)
# 陆耀巍的--------------------------------------------2
scores2={}
for k,v in scores.items():
    if v not in scores2:
        scores2[v]=k    #没有则添加
    elif v in scores2:
        scores2[v]+=','+k   #有则修改
print(scores2)
