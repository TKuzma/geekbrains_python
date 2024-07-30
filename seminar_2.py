# num = int(input("Введите число "))
# if num % 2 == 0:
# print("вы ввели четное число")
# if num % 2 == 1:
# print("вы ввели нечетное число")

# if num == 0:
# print("вы ввели ноль")
# elif num % 2 == 0:
# print("вы ввели четное число")
# else:
# print("вы ввели нечетное число")

# for i in range(10):
# num = int(input("Введите число "))
# if num == 0:
# print("вы ввели ноль")
# elif num % 2 == 0:
# print("вы ввели четное число")
# else:
# print("вы ввели нечетное число")
'''
while True:
    num = int(input("Введите число для анализа, для выхода из цикла введите ноль "))
    if num == 0:
        print("вы ввели ноль")
        break
    elif num % 2 == 0:
        print("вы ввели четное число")
    else:
        print("вы ввели нечетное число")
'''

'''
Задача №1.
По данному целому неотрицательному n вычислите значение n!. 
N! = 1 * 2 * 3 * … * N (произведение всех чисел от 1 до N) 0! = 1 
Решить задачу используя цикл while Input: 5 Output: 120
'''

if 1 == 11:
    n = int(input('Введите число: '))

    def factorial(n):
        res = 1
        i = 1
        while i <= n:
            res *= i
            i += 1
        return res

    print(factorial(n))


'''
Дано натуральное число A > 1. 
Определите, каким по счету числом Фибоначчи оно является, то есть выведите такое число n, что φ(n)=A. 
Если А не является числом Фибоначчи, выведите число -1. Input: 5 Output: 6
'''

a = int(input('Введите натуральное число: '))

first = 1
second = 0
current = first + second
n = 3
while current < a:
    n += 1
    second = first
    first = current
    current = first + second
if a != current:
    print(-1)
else:
    print('n = ', n)

