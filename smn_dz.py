# for i in range(4):
res = 0
num = str(input('1. Введите число: '))
for i in num:
    if i.isdigit():
        res += int(i)
print('Сумма цифр в числе', num, '=', res)

# for i in range(4):
res = 1
num = int(input('2. Введите число: '))
print('Ответ:')
for i in range(1, num+1):
    res *= i
    print(res, '\t')

# for i in range(4):
res = 0
num = int(input('3. Введите число: '))
for i in range(1, num+1):
    res += (1+1/i)**i
print('Ответ:', round(res, 3))

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
