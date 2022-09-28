# N = int(input('1. Введите число: '))
# num = 1
# lsd = []
# for i in range(N):
#     lsd.append(str(num))
#     num*=-3
# print(', '.join(lsd))

# N = int(input('2. Введите число: '))
# # print('[', end='')
# lsd = []
# for n in range(1,N+1):
#     lsd.append((3*n+1))
# # print(', '.join(lsd), end='')
# # print(']', end='')
# print(lsd)

# stri_ = input('3. Введите две строки: \n')
# str_ = input()
# ar = []
# ray = []
# for i in range(len(stri_)):
#     ar.append(stri_)
# print(ar)

# a = "aaaaaaaaabaasss"
# b = "aba"
# length = len(a) - len(b)
# count = 0
# for i in range(length):
#     if b in a[i:i + len(b)]:
#         count += 1
# print(count)

# def f(a, b):
#     count = 0
#     for i in range(len(a) - len(b)):
#         print('->>', a[i:i + len(b)])
#         if b == a[i:i + len(b)]:
#             count += 1
#     return count


res = 0
num = str(input('1. Введите число: '))
for i in num:
    if i.isdigit():
        res += int(i)
print('Сумма цифр в числе', num, '=', res)
