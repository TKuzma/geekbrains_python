'''
print('Hello, world!')

n = 'str\'str'
print(n)

m = 'str"stry"'
print(m)

print(f"{n} - {m}")
print("{} - {}".format(n, m))

# print(1010)
"""
ctrl + k, ctrl + c -- закомментировать
ctrl + k, ctrl + u -- раскомментрировать
"""
"""
вот такой комментарий
"""

print('Введите число: ')
a = input()
print(a)
b = input('Введите еще одно число: ') 
print(b)
print(a, " + ", b, " = ", a + b)

print('Введите число: ')
x = int(input())
print(x)
y = int(input('Введите еще одно число: ')) 
print(y)
print(x, " + ", y, " = ", x + y)

c = 5.89
print(type(c))
c = int(c)
print(type(c))
# не все типы данных можно приводить

f1 = 1.898
f2 = 2.336
print(round(f1*f2, 2))

iter = 2
iter += 3 # iter = iter + 3
iter -= 4 # iter = iter - 4
iter *= 5 # iter = iter * 5
iter /= 6 # iter = iter / 6
iter //= 7 # iter = iter // 7
iter %= 8 # iter = iter % 8
iter **= 9 # iter = iter ** 9

a = 1 > 4
print(a) # false
a = 1 < 4 and 5 > 2
print(a) # true
a = 1 == 2
print(a) # false
a = 1 != 2
print(a) # true
a = 'qwe'
b = 'qwe'
print(a == b) # true
a = 1 < 3 < 5 < 10
print(a) # true

if condition:
    # условие
else:
    # условие

if condition1:
    # условие
elif condition2: # else if == elif
    # условие
else:
    # условие

# Сложные условия
if condition1 and condition2:
    # условие

if condition4 or condition3:
    # условие


while condition:
    # условие

n = int(input('Введите число: '))
sum = 0
while n > 0:
    x = n % 10
    sum += x
    n //= 10
print(sum)

i = 0
while i < 5:
    #if i == 3:
        #break  # использовать break нежелательно
    i += 1
else:
    print('Stop')
print(i)

# Находит минимальный делитель
n = int(input())
flag = True # Вместо break лучше использовать такую конструкцию
i = 2
while flag:
    if n % i == 0: # если остаток от деления числа n на i равен 0
        flag = False
        print(i)
    elif n // 2 < i: # делитель числа не может превышать введеное число, деленное на 2
        print(n)
        flag = False
    i += 1

for i in enumeration: # для перебора значений
    # условие

r = range(5) # 0 1 2 3 4
r = range(2, 5) # 2 3 4
r = range(0, -5) # ----
r = range(1, 10, 2) # 1 3 5 7 9
r = range(100, 0, -20) # 100 80 60 20
r = range (100, 0, -20)
for i in r:
    print(i)

for i in 'qwerty':
    print(i)

a = 'qwerty'
print(a[0])
for i in a:
    print(i)

line = ""
for i in range(5):
    line = ""
    for j in range(5):
        line += '*'
    print(line)

text = 'Тут НаПиСаН обычный текст'
print(len(text))
print('текст' in text)
print(text.lower())
print(text.upper())
print(text.replace('текст', 'ТЕКСТ'))

text = 'Тут НаПиСаН обычный текст'
print(text[0])  # Т
print(text[1])  # у
print(text[len(text)-1]) # т (которая в конце)
print(text[-1]) # то же самое, что и строка выше
print(text[-4]) # е
print(text[:]) # Тут НаПиСаН обычный текст
print(text[:2]) # с 0 по 2 (не вкл) 'Ту'
print(text[2:9]) # с 2 по 9 (не вкл) 'т НаПиС'
print(text[2:-12]) # с 2 до -12 'т НаПиСаН о'
print(text[::6]) # с начала до конца с шагом 6 'ТПойт'
print(text[0:len(text):6]) # то же самое, что и верхняя
text = text[0:2] + text[-5] + text[2:9:2]
print(text) # ТуттНПС
'''