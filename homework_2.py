'''
На столе лежат n монеток. 
Некоторые из монеток лежат вверх решкой, а некоторые – гербом. 
Ваша задача - определить минимальное количество монеток, которые нужно перевернуть, 
чтобы все монетки лежали одной и той же стороной вверх.

Входные данные:
На вход программе подается список coins, где coins[i] равно 0, 
если i-я монетка лежит гербом вверх, и равно 1, 
если i-я монетка лежит решкой вверх. Размер списка не превышает 1000 элементов.

Выходные данные:
Программа должна вывести одно целое число - минимальное количество монеток, которые нужно перевернуть.

Пример использования На входе:
coins = [0, 1, 0, 1, 1, 0]
На выходе:
3
'''
# Мой варинат
# coins = [0, 1, 0, 1, 1, 1, 1]
# el0 = 0
# elcount0 = coins.count(el0)
# el1 = 1
# elcount1 = coins.count(el1)
# count = 0

# if len(coins) > 1000:
#     print('Недопустимое количество элементов')
# else:
#     if elcount0 <= elcount1:
#         for i in range(len(coins)):
#             if coins[i] == el0:
#                 coins[i] = el1
#                 count += 1
#     else:
#         for i in range(len(coins)):
#             if coins[i] == el1:
#                 coins[i] = el0
#                 count += 1

# print(count)

# Второй вариант
# count_zero = 0
# count_one = 0

# for coin in coins:
#     if coin == 0:
#         count_zero += 1
#     else:
#         count_one += 1

# if count_one > count_zero:
#     print(count_zero)
# else:
#     print(count_one)


'''
Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. 
Петя помогает Кате по математике.
Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. 
Для этого Петя делает две подсказки. Он называет сумму этих чисел S и их произведение P. 
Помогите Кате отгадать задуманные Петей числа.
Примечание: числа S и P задавать не нужно, они будут передаваться в тестах. 
В результате вы должны вывести все возможные пары чисел X и Y через пробел, такие что X <= Y.

Пример
На входе:
s = 12
p = 27

На выходе:
3 9
'''
s = 12
p = 27

# Мое решение
def find_numbers(S, P):
    results = []
    for X in range(1, 1001):
        for Y in range(1, 1001):
            if X + Y == S and X * Y == P and X <= Y:
                results.append((X, Y))
    return results

# Пример использования
S = int(input("Введите сумму S: "))
P = int(input("Введите произведение P: "))

pairs = find_numbers(S, P)
for pair in pairs:
    print(pair[0], pair[1])

# Второй вариант
solutions = []
for i in range(1, 1001):
    for j in range(1, 1001):
        if s == i + j and p == i * j:
            solutions.append((min(i, j), max(i, j)))
solutions = list(set(solutions))

for solution in solutions:
    print(solution[0], solution[1])





'''
Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.

Пример
n=16

#Вывод
1
2
4
8
16
'''
# Мой вариант
# n = 16
# i = 2
# b = 0
# while True:
#     res = i ** b
#     if res > n:
#         break
#     print(res)
#     b += 1

# Второй вариант
# i = 0
# while 2 ** i <= n:
#     print(2 ** i)
#     i += 1
