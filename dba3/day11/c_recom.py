# recommend_pokemon_byname(pokemon_name):
# 
# recommend_pokemon_byattr(hp,attack,defense,spatk,spdef,speed)
# 
# 返回3个类似属性的pokemon


import random 
def _random_choose(lst,n=3):
    '''不重复的从一个容器中选择n个返回
    lst = [1,2,3,4,5,6,7,8,9]
    _random_choose(container,n=3)
    返回 随机n个
    '''
    lst = lst.copy()
    chosed_elements = []
    while n:
        element = random.choice(lst) # 从里面随机取一个
        lst.remove(element) # 原序列中把这个元素删了
        chosed_elements.append(element)
        n-=1
    return chosed_elements

lst = [1,2,3,4,5,6,7,8]
_random_choose(lst,3)

if __name__ == '__main__':
    pass

#[print(random.sample(lst,3)) for n in range(10)]