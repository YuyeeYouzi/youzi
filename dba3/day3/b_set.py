a = set()   #定义一个空集合
a = {1,2,3,5,6}  #直接定义集合
lst = [1,4,56,8,4,3,6,3,6]
a = set(lst)   #用构造器定义
lst=list(a)
lst = list(set(lst))
print(lst)
print(a,type(a))

s={id,type,help,str}
print(s)
# 添加元素
a.add(1)
print(a)  #添加元素，有则不添加
a.update([2,3,4])
a.update({99,100})
print(a)
a.remove(1)
print(a)

print(set('1234')>set('12435'))
print(set('1234')<set('12435'))
print(set('12346')>=set('12435'))
jiaoji = set('sheep') & set('shop')
print(jiaoji)
bingji = set('sheep') | set('shop')
print(bingji)
buji = set('sheep') - set('shop')
print(buji)

# 两门成绩都及格的同学的名字
#   分别找出及格的名字，并求交集
math = {'cat': 55, 'bob': 75, 'pig': 85, 'tom': 50, 'dog': 66}
english = {'cat': 95, 'bob': 88, 'pig': 85, 'tom': 50}
math_set=set()
#print(type(math_set))
english_set=set()
for n,v in math.items():
    if v>=60:
        math_set.add(n)
for n,v in english.items():
    if v>=60:
        english_set.add(n)
allpass=english_set & math_set
print(allpass)

[n**2 for n in range(1,11)]  #列表
{n**2 for n in range(1,11)}  #集合
{n:n**2 for n in range(1,11)}  #字典
print('----------------------------')
# 字典是无序的，不能排序
# 按成绩从高到低。打印出学生的名字
from operator import itemgetter
math = {'cat': 55, 'bob': 75, 'pig': 85, 'tom': 50, 'dog': 66}
#没写出来
math_scores=[]
math_name=set()
for name,score in math.items():
    math_scores.append(score)
for score in sorted(math_scores,reverse=True):
    if score == math.values():
        math_name.add(math.name())
print(math_name)

# 老师讲的-----------------------------------------------1
sorted_scores = sorted(math.values(),reverse=True)
print(sorted_scores)
scores2 = {}
for name,score in math.items():
    scores2[score] = name
for score in sorted_scores:
    print(scores2[score])

# 赵丹翔的-----------------------------------------------2
from operator import itemgetter
print(math.items())
sorted_items=sorted(math.items(),key=itemgetter(1),reverse=True)
print(sorted_items)
for item in sorted_items:
    print(item[0])

