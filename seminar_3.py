'''
sp = list()
sp = [-1, True, "hello", 5.77, 8.999, "world"]

# print(sp)
# print(sp[2:5])

# for i in range(len(sp)):
#     print(f"{i} - {sp[i]}")

# for el in sp:
#     print(el, end = ' ')

# print(end = '\n')

sp.append('last')
sp.insert(0,'first')
# print(sp)

sp.remove(True)
del sp[0]
# print(sp)
a = sp.pop()
# print(a)
# print(sp)

t = tuple(sp)
# print(t)
# print('hi' in t)
# print('hello' in t)

d = {}
d['дядя ваня'] = 8645464
d['дядя вася'] = 21313231321
# print(d)
# print(d.keys())
# print(d.values())
# for i in d:
#     print(i)
# for key,value in d.items():
#     print(f"{key} - {value}")

s = {1,1,1,1,5,5,8,8,8,8,8}

s.add(7)
s.discard(1)
s.discard(2)

print(s)
'''


'''
Задача №1. Решение в группах Дан список чисел. 
Определите, сколько в нем встречается различных чисел. 
Input: [1, 1, 2, 0, -1, 3, 4, 4] Output: 6
'''

# a = [1, 1, 2, 0, -1, 3, 4, 4]
# print(len(set(a)))

'''
Задача №2. Решение в группах Дана последовательность из N целых чисел и число K. 
Необходимо сдвинуть всю последовательность (сдвиг - циклический) на K элементов вправо,  
K – положительное число. 
Input:   [1, 2, 3, 4, 5] k = 2 Output:  [4, 5, 1, 2, 3]
'''

# a = [1, 2, 3, 4, 5]
# b = a.copy()
# k = 2
# for i in range(len(a)):
#     b[(i + k) % len(a)] = a[i]
# print(b)

# k = int(input('Введите число K: '))
# s = [1, 2, 3, 4, 5]
# k = k % len(s)

# for _ in range (k) : 
#     s.insert(0, s.pop()) 

# print(s)

# a = [1, 2, 3, 4, 5]   # НЕ ЭФФЕКТИВНЫЙ
# k = 2
# for i in range(k):
#     a1 = a.pop(len(a) - 1)
#     a2 = a.insert(0, a1)
# print(a)    

# a = [1, 2, 3, 4, 5]
# k = 2

# t = a[-k:] + a[:-k]  
# print(t)

'''
Задача №3. Решение в группах Напишите программу для печати всех уникальных значений в словаре. 
Input:  [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII": " S005 "}, {" V ":" S009 "}, {" VIII ":" S007 "}] 
Output: {'S005', 'S002', 'S007', 'S001', 'S009'}
'''
# d = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII": " S005 "}, {" V ":" S009 "}, {" VIII ":" S007 "}]
# d1 = set()
# for i in d:
#     for j in i.values():
#         d1.add(j.strip())
# print(d1)

'''
Задача 1 
НЕГАФИБОНАЧЧИ по желанию
Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

Пример:
для k = 9 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] [Негафибоначчи]​
'''

# a=[0,1]
# k = 9
# for i in range(k-2):
#     a.append(a[i]+a[i+1])
# b=[]
# for i in range(1,len(a)):
#     if i%2==0:
#         b.insert(0,-a[i])
#     else:
#         b.insert(0,a[i])
# print(b+a)

a = [1,0,1]
k = 9
for i in range(k-2):
    a.append(a[-1]+a[-2])
    a.insert(0,a[-1]*((-1)**(i+1)))
print(a)