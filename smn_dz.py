# Задание 1 Напишите программу, которая принимает на вход 
# вещественное число и показывает сумму его цифр.

# for i in range(4):
res = 0
num = str(input('1. Введите число: '))
for i in num:
    if i.isdigit():
        res += int(i)
print('Сумма цифр в числе', num, '=', res)

# Задание 2 Напишите программу, 
# которая принимает на вход число N и выдает 
# набор произведений чисел от 1 до N.

# for i in range(4):
res = 1
num = int(input('2. Введите число: '))
print('Ответ:')
for i in range(1, num+1):
    res *= i
    print(res, '\t')

# Задание 3 Задайте список из n чисел последовательности (1+1/n)^n 
# и выведите на экран их сумму,
# округлённую до трёх знаков после точки.

# for i in range(4):
res = 0
num = int(input('3. Введите число: '))
for i in range(1, num+1):
    res += (1+1/i)**i
print('Ответ:', round(res, 3))

# Задание 4 Задайте список из N элементов, 
# заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на позициях a и b.
# Значения N, a и b вводит пользователь с клавиатуры.

# for i in range(4):
N = int(input('4. Введите значение границ списка: '))
List = []
for i in range(-N, N):
    List.append(i)
print(List, '\n Введите желаемы значения позиций в списке: ')
a = int(input())
b = int(input())
if a<N*2 and b<N*2:
    res = List[int(a)] * List[int(b)]
    print('Произведение элементов списка на позициях', a, 'и', b, '=', res)
else:
    print('Задано неверное значение позиций!') 

# Задание 5 Реализуйте алгоритм перемешивания списка.

# for i in range(4):
import random
N = int(input('5. Введите значение границ списка: '))
List = []
for i in range(-N, N):
    List.append(i)
print(List, '\n Перемешанный: ')
ListR = []
for i in List:
    rndi = random.uniform(-N, N)
    List[i] = List[int(rndi)]
print(List)