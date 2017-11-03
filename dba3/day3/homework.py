#输入的字典 = {'cat': 123, 'tom': 666, 'pig': 555, 'moon': 555}
#颠倒字典中的键和值 {'sdf':'1ff3'}
#写一个函数返回{123: 'cat', 666: 'tom', 555: ['pig', 'moon']}
#写一个函数，接收一个字典，返回一个键值颠倒字典，
#如果值不重复的话，直接键值颠倒
#如果值重复的话，把原来字典的键放在列表里
#做一下异常处理，检查这个参数是不是一个字典
#然后检查key是不是字符串，value是不是数字
#一个不符合就整个不处理



dct={'cat': 123, 'tom': 666, 'pig': 555, 'moon': 555}
dct2=dict.fromkeys(dct.values())
print(dct2)
for name,v in dct.items():
    if isinstance(dct2[v],list):
        dct2[v].append(name)
    if dct2[v]==None:
        dct2[v]=[name]
print(dct2)


def diandao(dct):#我自己写-------------------------------------->1
    dct2=dict.fromkeys(dct.values())
    for k,v in dct.items():
        if isinstance(dct2[v],list):
            dct2[v].append(k)
        if dct2[v]==None:
            dct2[v]=[k]
    return dct2
dct1={'cat': 123, 'tom': 666, 'pig': 555, 'moon': 555}
print(diandao(dct1))

def reverse_keyvalue(dct):#老师讲的----------------------------->2
    if not isinstance(dct,dict):
        raise TypeError('dct参数必须是字典')
    #所有键是不是字符串的布尔值
    keys_is_str = [isinstance(key,str) for key in dct]
    #字典值的遍历
    value_is_number = [isinstance(value,(int,float)) for value in dct.values()]
    if not all(keys_is_str):
        raise KeyError('所有键必须是字符串')
    if not all(value_is_number):
        raise ValueError('所有值必须是数字')

    dct_rtn = {} #键值颠倒的字典
    for name,score in dct.items():
        if not score in dct_rtn:
            dct_rtn[score]=name
        else:
            #555:'pig'---->555:['pig']
            dct_rtn[score]=[dct_rtn[score]]
            dct_rtn[score].append(name)
    print(dct_rtn)
print(reverse_keyvalue(dct))

def diandao1(dct,a=0):
    lst=[]
    for name in dct:
        if dct[name] not in lst:
            lst.append(name)
        else:
            a=1
            break
    if a==0:
        dct2={}
        for name,v in dct.items():
            dct2[v]=name
        return dct2
    elif a==1:
        dct3=dict.fromkeys(dct.values())
        for k,v in dct.items():
            if isinstance(dct2[v],list):
                dct3[v].append(k)
            if dct3[v]==None:
                dct3[v]=[k]
        return dct3
dct1={'cat': 123, 'tom': 666, 'pig': 555, 'moon': 555}
print(diandao1(dct1))


#def yichang(c):
#    if not isinstance(c,dict):
#        TypeError('非字典')
#    for k,v in c.items():
#        if not isinstance(k,str):
#            TypeError('非字符串')
#        if not isinstance(v,(int,float)):
#            TypeError('非数字')
#print(yichang())

    



