# Задача 34
"""
def rhythm(str):
    str = str.split()
    list = []
    for word in str:
        result = 0
        for i in word:
            if i in 'аеёиоуыэюя':
                result += 1
        list.append(result)
    return len(list) == list.count(list[0])

print('Введите: пара-ра-рам рам-пам-папам па-ра-па-дам')
str = input()
if rhythm(str):
    print('Парам пам-пам')
else:
    print('Пам парам')
"""

# Задача 36
"""
s = input() 
s_lst = s.split() 
tp = tuple(map(lambda x: tuple(x.split('=')), s_lst))
"""