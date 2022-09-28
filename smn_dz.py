# for i in range(4):
from typing import List


res = 0
num = str(input('1. Введите число: '))
for i in num:
    if i.isdigit():
        res += int(i)
print('Сумма цифр в числе', num, '=', res)

# for i in range(4):
res = 1
num = int(input('2. Введите число: '))
for i in range(1, num+1):
    res *= i
    print(res)

# for i in range(4):
res = 0
num = int(input('3. Введите число: '))
for i in range(1, num+1):
    res += (1+1/i)**i
print(round(res, 3))

# for i in range(4):
print('Введите 3 числа:')
N = int(input)
a = int(input)
b = int(input)
List = []
# for i in range(-N, N):
