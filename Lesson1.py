# x = '*'
# y = 'Раз'
# t = 'Два'
# r = 'Три'
# print(x, y, t, r, sep='*')


# s1 = "*"
# s2 = "Раз"
# s3 = "Два"
# s4 = "Три"
#
# # s1, s2, s3, s4 =input()
#
# s1 = input()
# s2 = input()
# s3 = input()
# s4 = input()
#
# print(s2, s3,s4, sep= s1)

# x = input()
# print('Привет, ' + x + '!')

# x = int(input())
# y = 9
# i = 10
# print(x)
# print(y)
# print(i)

#
# num, num1, num2=int(input()), int(input()), int(input())
# print(num+num1+num2)

# a = int(input())
# # a = 25
# V = 3
# S = 6*a**2
#
# print(f'объем', '=', a ** V)
# print(f'площадь', '=', S)


# a = int(input())
# b = int(input())
# # a = 1
# # b = 1
# x = 3*(a + b)**3 + 275*b**2 - 127*a - 41
# print(x)

# x = 20
# x = int(input())
# y = 21 + 1
# i = 19 - 1
# print('Следующее за числом ' + str(x) + ' число: ' + str(y) +'\n'
#       'Для числа ' + str(x) +' предыдущее число: ' + str(i))





# x = 20
# x = int(input())
# y = 21
# i = 19
# print('Следующее за числом',x, 'число:', x+1, '\n'
#      'Для числа',x, 'предыдущее число:',x-1)


# x = int(input())
# print('Следующее за числом',x,'число:',x+1, '\n'
#       'Для числа',x, 'предыдущее число:',x-1)

# mon = int(input())
# cpu = int(input())
# key = int(input())
# mouse = int(input())
# print((mon + cpu + key + mouse) * 3)

# x = 2
# y = 7
#
# print(f'{x} + {y} = {x+y}')
# print(f'{x} - {y} = {x-y}')
# print(f'{x} * {y} = {x*y}')

# a = int(input())
# d = int(input())
# n = int(input())
# an = a + d*(n-1)
# print(an)


# x = 7
# y = x*2
# i = x*3
# t = x*4
# r = x*5
# print(x,y,i,t,r,sep='---')

# b1 = int(input())
# q = int(input())
# n = int(input())
# bn = b1 * (q**(n - 1))
#
# print(bn)


# x = int(input())
# print(x//100)


# sch = 3
# manda = 6
# print(manda//sch)
# print(manda%sch)

# x = int(input())
# print(x//2 + x%2)


# a = 1
# m = a - a // 4 * 4
# print(a // 4 + (m // 3 + m // 2 + m % 2) % 2)




# min = 150
# hour = min//60
# min3 = min%60
#
# print(f'{min} мин - это {hour} час {min3} минут.')

# min = int(input())
# # print(150%60)
# print(f'{min} мин - это {2%min} час {min%60} минут.')

# num = 123
# digit3 = num % 10
# digit2 = (num // 10) % 100 // 2
# digit1 = num // 10 // 2
# print(f'Сумма цифр = {digit2}\nПроизведение цифр = {digit1}')


# abc = 123
# c = abc % 10
# b = (abc % 100) // 10
# a = abc // 100
# print(f'{abc}, {acb}, {bac}, {bca}, {cab}, {cba}', sep='\n')


# a = 3
# b = 2
# x = (a+b)**2
# y = a**2 + b**2
#
# print(f'Квадрат суммы {a} и {b} равен {x}')
# print(f'Сумма квадратов {a} и {b} равна {y}')

# a = 9

# b = 29
# c = 7
# d = 27
# x = (a**b) + (c**d)
# print(x)

# a = int(input())
# b = 10*a + a
# c = 100*a + aa
# print(a + b + c)

# answer = input('Какой язык программирования мы изучаем? : ')
# if answer == 'Python':
#     print('Верно! Мы ботаем Python =)')
#     print('Python - отличный язык!')
# else:
#    print('Не совсем так!')

#######################if x > 7	если x больше 7
####################### if x < 7	если x меньше 7
####################### if x >= 7	если x больше либо равен  7
####################### if x <= 7	если x меньше либо равен  7
####################### if x == 7	если x равен  7
####################### if x != 7	если x не равен  7

# age = 6
# if 3 <= age <= 6:
#     print('Вы ребёнок')
# a = 2
# b = 2
# c = 4
# if a != b != c:
#     print('числа не равны')
# else:
#     print('числа равны')

# qa1 = input('Твой язык: ')
#
#
# if qa1 == "Python":
#     print('Yes')
# else:
#     print('No')



# num = int(input('Число: '))
# last_digit = num % 10
# first_digit = num // 10
#
# if last_digit == first_digit:
#     print('Yes')
# else:
#     print('No')

# num1, num2, num3 = 15, 10, 35
# counter = 0  # переменная счётчик
# if num1 % 2 == 1:
#     counter = counter + 4  # увеличиваем счётчик на 1
# if num2 % 2 == 0:
#     counter = counter + 1  # увеличиваем счётчик на 1
# if num3 % 2 == 1:
#     counter = counter + 1  # увеличиваем счётчик на 1
# print(counter)

# x, y = input(), input()
#
# if x == 'qwerty':
#     print('Пароль принят')
# if y == 'qwerty':
#     print('Пароль принят')

# x, y = input(), input()
# if x == y:
#
#     print('Пароль принят')
#
# else:
#     print('Пароль не принят')

# x = int(input())
# if x % 2 == 0:
#     print('Четное')
# else:
#     print('Нечетное')

# x = 1614
#
# if (x // 1000) + (x % 10) == ((x % 1000) // 100) - ((x % 100) // 10):
#     print("ДА")
# else:
#     print('НЕТ')

# x = int(input())
# if x < 18:
#     print('Доступ запрещен')
# else:
#     print('Доступ разрешен')

# a = 1
# b = 2
# c = 3
#
#
# if  b-a==c-b:
#     print('YES')
# else:
#     print('NO')

# x = 8
# y = 11
# if x <= y:
#     print(x)
# else:
#     print(y)

# a = [1,2,3,4]
# min(a)
# if min(a):
#     print(min(a))
# else:
#     print(min(a))

# x = int(input())
#
# if 1 <= x <= 13:
#     print('детство')
# if 14 <= x <= 24:
#     print('молодость')
# if 25 <= x <= 59:
#     print('зрелость')
# if 60 <= x:
#     print('старость')

# a = 4
# b = -22
# c = 1
# sum = 0
# x = str.isdigit(a)
# print(x+sum)

# a = 4
# b = -22
# c = 1
#
# if a>0 == a:
#     a == a
# if a<0 == 0:
#     a = 0
# if b>0 == b:
#     b == b
# if b<0 == 0:
#     b = 0
# if c>0 == c:
#     c == c
# if c<0 == 0:
#     c = 0
# print(a+b+c)


# age = int(input())
# if 7 <= age <= 9: #if age >= 7 and age <=12:
#     print('go')
# else:
#     print('no')

#Напишите программу, которая определяет, является ли заданное натуральное число трёхзначным
# num = int(input())
# if 100 <= num <= 999:     # num >= 100 and num <= 999
#     print('Число является трёхзначным')
# else:
#     print('Число не является трёхзначным')
x = 2

#Напишите программу, которая проверяет, что все три цифры натурального трёхзначного числа различны.
# num = int(input()) #946
#
# d3 = num % 10 #6
# d2 = num % 100 // 10 #4
# d1 = num // 100 #9
#
# if d3 != d2 and d3 != d1 and d2 != d1:
#     print('Цифры различны')
# else:
#     print('Цифры не различны')


# Напишите программу, которая по координатам точки, не лежащей на
# осях координат, определяет номер координатной четверти, в которой она находится

# x = int(input())
# y = int(input())
#
# if x > 0 and y > 0:
#     print('1 четверть')
# if x < 0 and y > 0:
#     print('2 четверть')
# if x < 0 and y < 0:
#     print('3 четверть')
# if x > 0 and y < 0:
#     print('4 четверть')

# x = 2
# if x > -1 and x < 17:
#     print("Принадлежит")
# else:
#     print("Не принадлежит")



# x = -44
# # if x <= -3 or x >= 7:
# #     print("Принадлежит")
# # else:
# #     print("Не принадлежит")

# x = -331
# if x > -30 and x <= -2 or x > 7 and x <= 25:
#     print("Принадлежит")
# else:
#     print("Не принадлежит")

# y = 1043
#
# if 1000 <= y <= 9999 and (y % 7 == 0 or y % 17 == 0):
#     print('YES')
# else:
#     print('NO')

# a = 5
# b = 2
# c = 3
#
# if a + b > c and a + c > b and b + c > a:
#     print("YES")
# else:
#     print("NO")

# x = 2020
# if x % 4 ==0 and (not x % 100 == 0 or x % 400 == 0):
#     print('Yes')
# else:
#     print('NO')


# a = 4
# b = 4
# c = 5
# d = 4
# if a == c or b == d:
#     print('YES')
#
# else:
#     print('NO')

# a = 4
# b = 4
# c = 5
# d = 5
# if (-1 <= a - c <= 1) and (-1 <= b - d <= 1):
#     print('YES')
#
# else:
#     print('NO')

#Даны три целых числа. Определите, сколько среди них совпадающих.  Использование каскадного условного оператора и логического оператора or.
# a, b, c = int(input()), int(input()), int(input())
# if a == b == c:
#     print(3)
# elif a == b != c or b == c != a or a == c != b:
#     print(2)
# else:
#     print(0)

# n = 2204
# k = 1505
# if n > k:
#     print('NO')
# elif k > n:
#     print('YES')
# else:
#     print("Don't know")

# a = 145
# b = 145
# c = 139
# if a == b == c:
#     print('Равносторонний')
# elif a == b or b == c or a == c:
#     print('Равнобедренный')
# elif a != b != c:
#     print('Разносторонний')

# a = 1
# b = 2
# c = 3
#
# if b < a < c or c < a < b:
#     print(a)
# elif a < b < c or c < b < a:
#     print(b)
# else:
#     print(c)

# x = 12
#
#
# if x == 2:
#     print(28)
# elif (x < 8 and x % 2 == 0) or (x > 7 and x % 2 != 0):
#     print(30)
# else:
#     print(31)

# x = int(input())
# if x <= 68 and x >= 64:
#     print('Полусредний вес')
# elif x <= 63 and x >= 60:
#     print('Первый полусредний вес')
# elif x <= 59:
#     print('Легкий вес')


# r = input('+,-,*,/') #r = input()
# a = 9
# b = 0
# if r == '+':
#     print(a + b)
# elif r == '-':
#     print(a - b)
# elif r == '*':
#     print(a * b)
# elif r == '/':
#     if b == 0:
#         print('На ноль делить нельзя!')
#     else:
#         print(a / b)
# else:
#     print('Неверная операция')






# a = 'красный'
# b = 'синий'
# if (a == 'красный' or b == 'красный') and (a == 'синий' or b == 'синий'):
#     print('фиолетовый')
# elif (a == 'красный' or b == 'красный') and (a == 'желтый' or b == 'желтый'):
#     print('оранжевый')
# elif (a == 'желтый' or b == 'желтый') and (a == 'синий' or b == 'синий'):
#     print('зеленый')
# else:
#     print('ошибка цвета')







# x = 4
# if x > 36 or x < 0:
#     print('ошибка ввода')
# elif x == 0:
#     print('зеленый')
# elif 1 <= x <= 10:
#     if x % 2 == 0:
#         print('черный')
#     else:
#         print('красный')
# elif 11 <= x <= 18:
#     if x % 2 == 0:
#         print('красный')
#     else:
#         print('черный')
# elif 19 <= x <= 28:
#     if x % 2 == 0:
#         print('черный')
#     else:
#         print('красный')
# elif 29 <= x <= 36:
#     if x % 2 == 0:
#         print('красный')
#     else:
#         print('черный')


# a = 7
# b = 12
#
# num = {1: 'I', 2: 'II', 3: 'III', 4: 'IV', 5: 'V', 6: 'VI', 7: 'VII', 8: 'VIII', 9: 'IX', 10: 'X'}
# if a <= 10:
#     print(num[a])
# else:
#     print('oшибка')
# if b <= 10:
#     print(num[b])
# else:
#     print('oшибка')




# a = 7
# if a == 1:
#     print('YES')
#
# elif 2 <= a <= 5:
#     if a % 2 == 0:
#         print('NO')
#     else:
#         print('YES')
# elif 6 <= a <= 20:
#     if a % 2 == 0:
#         print('YES')
#     else:
#         print('NO')
# elif a > 20:
#     if a % 2 == 0:
#         print('NO')
#     else:
#         print('YES')
#

#Даны две различные клетки шахматной доски. Напишите программу, которая определяет,
#может ли слон попасть с первой клетки на вторую одним ходом. Программа получает на вход
#четыре числа от 1 до 8 каждое, задающие номер столбца и номер строки сначала для первой
#клетки, потом для второй клетки. Программа должна вывести «YES», если из первой клетки ходом
#слона можно попасть во вторую или «NO» в противном случае.
# x1 = 4
# y1 = 4
# x2 = 5
# y2 = 5
# if (x1 - y1) == (x2 - y2) or (x1 + y1) == (y2 + x2):
#     print('YES')
# else:
#     print('NO')

# x1 = 1
# y1 = 1
# x2 = 8
# y2 = 8
#
# if  (x1 - x2) * (y1 -y2) == 2 or (x1 - x2) * (y1 -y2) == -2:
#     print('YES')
# else:
#     print('NO')

#Ход ферзя
# x1 = 1
# y1 = 1
# x2 = 2
# y2 = 2
# if x1 == x2 or y1 == y2 or (x1 - y1) == (x2 - y2) or (x1 + y1) == (x2 + y2):
#     print('YES')
# else:
#     print('NO')


# n = 5
# m = 10.5
# if n <= 2:
#     print(n * 10.5)
# elif n > 2:
#     print(21 +(n -2) * 4)

# x = 3384390.4339
# y = int(x * 10)
# c = y % 10
# print(c)


# x = 945
# a = x % 10 #5
# b = (x % 100) // 10 #4
# c = x // 100 #9
# r = min(a, b, c)
# t = max(a, b, c)
# y = a + b + c - r - t
# if c - b == y:
#     print('Число интересное')
# else:
#     print('Число неинтересное')

#Манхетское расстояние!!!
# p1 = 10
# p2 = 15
# q1 = 21
# q2 = 13
# m = abs(p1 - q1) + abs(p2 - q2)
# print(m)



# мой вариант правильный
# a = 'novgorod' #8
# b = 'Piterburg' #9
# c = 'Moscva' #6
# a1 = len(a) #8
# b2 = len(b)#9
# c3 = len(c) #6
# x = max(a1, b2, c3)
# y = min(a1, b2, c3)
# if a1 == y and b2 == x:
#     print(a, b, sep='\n')
# elif b2 == y and a1 == x:
#     print(b, a, sep='/n')
# elif b2 == y and c3 == x:
#     print(b, c, sep='/n')
# elif c3 == y and b2 == x:
#     print(c, b, sep='\n')
# elif a1 == y and c3 == x:
#     print(a, c, sep='\n')
# elif c3 == y and a1 == x:
#     print(c, a, sep='\n')
#
# a = 'novgorod' #8
# b = 'Piterburg' #9
# c = 'Moscva' #6
# a1 = len(a) #8
# b2 = len(b)#9
# c3 = len(c) #6
# x = max(a1, b2, c3)
# y = min(a1, b2, c3)
#
# if a1 >= b2 >= c3:
#     print(c, a, sep='\n')
# elif b2 >= a1 >= c3:
#     print(c, b, sep='\n')
# elif a1 >= c3 >= b2:
#     print(b, a, sep='\n')
# elif b2 >= c3 >= a1:
#     print(a, b, sep='\n')
# elif c3 >= a1 >= b2:
#     print(b, c, sep='\n')
# elif c3 >= b2 >= a1:
#     print(a, c, sep='\n')


#Дизавинчи
# a = input('Стиль: ') #4
# b = int(input('Какое количество людей: ')) #6
# c = int(input('Какой размер: ')) #10
#
# if a == 'Цифровая живопись' and b == 1 and c == (40_50):
#     t = 73 + 3 + 20
#     print('Цена: ' + str(t))
# elif a == 'Импасто' and b == 3 and c == (40_60):
#     t = 253 + 38 + 23
#     print('Цена: ' + str(t))
# elif a == 'Цифровая живопись' and b == 3 and c == (40_50):
#     t = 73 + 57 + 3
#     print('Цена: ' + str(t))

# a = 'abc'
# b = 'a'
# c = 'abcde'
# a1 = len(a) #3
# b1 = len(b) #1
# c1 = len(c) #5
# x = max(a1, b1, c1)
# y = min(a1, b1, c1)
# t = a1 + b1 + c1 - x - y
# if x - t == t - y:
#     print('YES')
# else:
#     print('NO')

# text = 'Какой сегодня день недели?'
#
#
# if 'суббота' in text or 'воскресенье' in text:
#     print('YES')
# else:
#     print('NO')

# email = 'aaaa@bbb.com'
# if '@' in email and '.' in email:
#     print('YES')
# else:
#     print('NO')


# import math
#
# num1 = math.sqrt(2)     # вычисление корня квадратного из двух
# num2 = math.ceil(3.8)   # округление числа вверх
# num3 = math.floor(3.8)  # округление числа вниз
#
# print(num1)
# print(num2)
# print(num3)

# from math import *
#
# num1 = sqrt(2)     # вычисление корня квадратного из двух
# num2 = ceil(3.8)   # округление числа вверх
# num3 = floor(3.8)  # округление числа вниз
#
# print(num1)
# print(num2)
# print(num3)

#Если нужно использовать только некоторые функции модуля, то мы можем импортировать только их следующим образом:

# from math import sqrt, ceil
#
# print(sqrt(25))
# print(ceil(34.7))
#
# print(floor(12.8))  # приведет к ошибке, так как функция floor не подключена

# from math import *
# x1 = 2.0
# y1 = 2.5
# x2 = 44.155
# y2 = 100.50
#
# p1 = sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2 )
#
# print(p1)

# import math
#
# r = 554.6
# s = math.pi * (r ** 2)
# c = math.pi * 2 * (r)
# print(s)
# print(c)

# from math import *
# a = 1.0
# b = 2.0
# ar = (a + b) / 2
# ge = sqrt(a * b)
# ga = ((a * b) * 2) / (a + b)
# qa = sqrt((a ** 2 + b ** 2) / 2)
#
# print(ar)
# print(ge)
# print(ga)
# print(qa)


# from math import *
#
# x = radians(float(input()))
# # r = (x * pi) / 180 # формула из градусов в радианы
# t = sin(x) + cos(x) + tan(x) * tan(x)
# print(t)



# from math import *
#
# x = 5.5
# a = floor(x) + ceil(x)
#
# print(a)

# from math import *
#
# a = 1
# b = 2
# c = 1
#
# d = b ** 2 - (4 * (a * c)) #Дискриминант
# d3 = - (b) / (2*a)

# if d < 0:
#     print('Нет корней')
# elif d == 0:
#     print(d3)


# if d3 <= 0:
#     print(d3)
#
# else:
#     print('Нет корней')




# from math import *
#
# n = 3
# a = 2.0
# S = (n * (a ** 2)) / (4 * tan(pi / n))
# print(S)

# for i in range(8):
#     num = int(input())
#     print('Квадрат вашего числа равен: ', num * num)
# print('Цикл завершен')


# text = 'Век живи - век учись.'
# r = 10
# for i in range(r):
#     print(text)

# for i in range(6):
#     print('AAA')
# for i in range(5):
#     print('BBBB')
# print('E')
# for i in range(9):
#     print('TTTTT')
# print('G')

# n = 1
#
# for i in range(n):
#     print('*' * 19)

# Если мы хотим начать с 1, то можем написать код:

# for i in range(10):
#     print(i + 1, '-- Привет')

# name = 'LeBron'
# for _ in range(10):
#     print(_, name)

# number = 9
# for number in range(number + 1):
#     print('Квадрат числа', number, 'равен', number * number)

# n = 3
# for i in range(n):
#     print((n - i) * '*')

# m = 10
# p = 50
# n = 6
#
# for i in range(n):
#     print(i + 1,  m * (p / 100 + 1) ** i)

#Важно
# zp = 100
# day = 7
# per = 30
# for i in range(day):
#     print(i + 1, zp * (per / 100 + 1) ** i)
#           i + 1, zp *            + формула процента) ** степень дня) 1 день, 2 день

# for i in range(100, 1000):  # перебираем числа от 100 до 999
#     if i % 10 == 2:         # используем остаток от деления на 10, для получения последней цифры
#         print(i)

# for i in range(56, 17, -2): #3 параметр рэндж считает четные числа
#     print(i)

# for i in range(5, 0, -1):
#     print(i, end=' ')
# print('Взлетаем')

# m = 1
# n = 9
# for i in range(m, n + 1):
#     print(i)

# m = 1
# n = 5
#
# if m < n:
#     for i in range(m, n + 1):
#         print(i)
# else:
#     for i in range(m, n -1, -1):
#         print(i)


# m = 77
# n = 62
# if m > n:
#     for i in range(m, n, -2):
#         print(i)
# elif m % 2 == 0:
#     for i in range(m -1, n - 1, -2):
#         print(i)


# m = 77
# n = 62
#
#
# for i in range(m - 1 + m % 2, n - 1, -2): #формула: я непойму нахуя делать 77 - 1 и 77 %2 = 1,
#     # по итогу 76 + 1 будет 77, то есть m
#     print(i)


# m = 1
# n = 20
# for i in range(m, n + 1):
#     if i % 10 == 9:
#         print(i)
#     elif i % 17 == 0:
#         print(i)
#     elif i % 15 == 0:
#         print(i)



# n = 5
# for i in range(1, 11):
#     print(n, 'x', i, '=', n * i)


# num = 17
# flag = True
#
# for i in range(2, num):
#     if num % i == 0:        #  если исходное число делится на какое-либо отличное от 1 и самого себя
#         flag = False
#
# if num == 1:
#     print('Это единица, она не простая и не составная')
# elif flag == True:
#     print('Число простое')
# else:
#     print('Число составное')


# largest = -1
# for i in range(10):
#     num = -46
#     if num > largest:
#         largest = num
# print('Наибольшее число равно', largest)
#
# largest = -22  # принимаем первое число за максимальное
# for i in range(9):
#     num = -44
#     if num > largest:
#         largest = num
# print('Наибольшее число равно', largest)

# total = 0
# for i in range(1, 6):
#     total += i
#     print(total, end='')


# counter = 0
# a = 1
# b = 10
# for i in range(a, b + 1):
#     if i ** 3 % 10 == 4 or i ** 3 % 10 == 9:
#         counter = counter + 1
# print(counter)

# total = 0
# n = 5
# for i in range(n):
#     num = 5
#     total = total + num
# print(total)

# from math import *
# n = 10
# for i in range(1, n):
#     num = n + (1 / (i + 1))
#     num2 = num + 1 + log(n)
# print(num2)


# counter = 0
# for i in range(1, 101):
#     if i ** 2 % 10 == 9:
#         counter = counter + 1
#     # print(counter)
#     print(f"{i=} {counter=} {i ** 2 % 10 =}")

# counter = 0
# for i in range(1, 51):
#     if i ** 2 % 10 == 4:
#         counter = counter + 1
# # print(counter)
#     print(f"{i=} {counter=} {i ** 2 % 10 =}")

# total = 0
#
# for i in range(10, 31):
#     if i % 2 == 0:
#         total += i
# print(total)

# from math import *
# counter = 0
# n = 10
# for i in range(1, n + 1):
#     num = (1 / i)
#
#     counter = counter + num
# print(counter - log(n))
#
#счетчик
# counter = 0
# n = 10
# for i in range(1,  n + 1):
#
#     if i ** 2 % 10 == 2 or i ** 2 % 10 == 5 or i ** 2 % 10 == 8:
#         counter += i
# print(counter)

#Мультипликатор
# total = 1
# n = 3
# for i in range(1, n + 1):
#
#     total = total * i
# print(total)





# total = 1
#
# for i in range(10):
#     num = 12
#     if num != 0:
#         total = total * num
# print(total)

# total = 0
# n = 10
# for i in range(1, n + 1):
#     if n % i == 0:
#         total += i
# print(total)

# total = 0
# n = 3
# for i in range(1, n + 1):
#     if i % 2 != 0:
#         total += i
#     elif i % 2 == 0:
#         total -= i
# print(total)




# n = 11
# flag = True
# for i in range(n):
#     if n % 2 == 0:
#         flag = False
#
# if n % 2 == 0:
#     print('YES')
# elif n % 2 != 0:
#     print('NO')

# counter = 0
# poem = 'у лукоморья дуб зеленый, златая цепь на дубе том, и днем и ночью ходит кот ученый'
# list_vowels = 'аеёиоуыэюя' #['а','е','ё','и','о','у','ы','э','ю','я']
# poem_length = len(poem)
# while counter != poem_length:
#     if poem[counter] in list_vowels:
#         print(f'Да, {poem[counter].lower()} - гласная')
#     else:
#         print(f'Нет, {poem[counter].lower()} - согласная')
#     counter += 1

# index = 0
# poem = 'у лукоморья дуб зеленый, златая цепь на дубе том, и днем и ночью ходит кот ученый'
# list_vowels = 'аеёиоуыэюя' #['а','е','ё','и','о','у','ы','э','ю','я']
# poem_length = len(poem)
# poem_volwers = ''
# while index != poem_length:
#     if poem[index] in list_vowels:
#         poem_volwers += poem[index]
#     index += 1
# print(poem_volwers)

# counter = 0
# poem = 'у лукоморья дуб зеленый, златая цепь на дубе том, и днем и ночью ходит кот ученый'
# poem_lenght = len(poem)
# data = [2, 3, 4, 5, 7]
#
# for i in data:
#     counter += i
#     print(counter)



# counter1 = 0
# counter2 = 0
# wom = [44, 75, 56, 99, 77]
# man = [155, 44, 65, 43, 84]
# for i in wom:
#     counter1 += i
# for i in man:
#     counter2 += i
# if counter1 > counter2:
#     print(f'Женщины живут дольше мужчин на {counter1 - counter2} лет')
# elif counter2 > counter1:
#     print(f'Мужчины живут дольше женщин на {counter2 - counter1} лет')


# total = 1
# n = 2
# a = 2
# for i in range(1, n + 1):
#     if i == 1:
#         total *= a
#     elif i > 1:
#         total += a ** 2
# print(total)
#
# counter1 = 0




# flag = 'YES'
# num = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
# for i in num:
#     if i % 2 != 0:
#         flag = 'NO'
#
# print(flag)


# n = 179
# while n > 0:
#     digit3 = n % 10
#     n //= 10
#     print(digit3, end='')

# n = 179
# mindig = 10
# maxdig = -1
# while n > 0:
#     digit3 = n % 10
#     mindig = min(mindig, digit3)
#     maxdig = max(maxdig, digit3)
#     n //= 10
# print(mindig, maxdig)


# n = 5
# num1 = -1
# num2 = -1
# for i in range(1, n + 1):
#     num = 5
#     if num > num1:
#         num2 = num1
#         num1 = num
#     elif num > num2:
#         num2 = num
# print(num1)
# print(num2)

# n = 22
# f1 = 0
# f2 = 1
#
# for i in range(1, n + 1):
#     f1, f2 = f2, f1 + f2
#     print(f1, end=' ')


# text = input()
# while text != 'КОНЕЦ':
#     num = int(text)
# print(text)
# text = input()


# text = input()
# while text != 'КОНЕЦ' and text != 'конец':
#     print(text)
#     text = input()

# counter = 0
# text = input()
# while text != 'стоп' and text != 'хватит' and text != 'достаточно':
#     text = input()
#     counter += 1
# print(counter)


# num = 49
# while num % 7 == 0:
#     print(num)
#     num = 2


# counter = 0
# num = int(input())
# while num >= 0:
#     counter += num
#     num = int(input())
# print(counter)

# counter = 0
# num = int(input())
# while num >= 0 and num < 6:
#
#     if num == 5:
#         counter += 1
#     num = int(input())
# print(counter)

# counter = 0
# price = 49
#
# while price >= 25:
#     counter += 1
#     price -= 25
# while price >= 10:
#     counter += 1
#     price -= 10
# while price >= 5:
#     counter += 1
#     price -= 5
# while price >= 1:
#     counter += 1
#     price -= 1
# print(counter)

# print('pass')
# response = input()
# while response != 'qwerty':
#     response = input('NO: ')
# print('YES')


# while True: print(eval(input('Numbers')))


# n = int(input())
# while n != 0:  # пока в числе есть цифры
#     last_digit = n % 10  # получить последнюю цифру
#     print(last_digit)
#     n = n // 10  # удалить последнюю цифру из числа


# num = int(input())
# has_seven = False  # сигнальная метка
#
# while num != 0:
#     last_digit = num % 10
#     if last_digit == 7:
#         has_seven = True
#     num = num // 10 #Убираем последнюю цифру
#
# if has_seven == True:
#     print('YES')
# else:
#     print('NO')


# num = 12345
# while num != 0:
#     last_dig = num % 10
#     print(last_dig)
#     num = num // 10

# num = 5086334
# while num != 0:
#     last_dig = num % 10
#     print(last_dig, end='')
#     num = num // 10

# num = 26670
# max_dig = 0
# min_dig = 9
# while num != 0:
#     last_dig = num % 10
#     if last_dig < min_dig:
#         min_dig = last_dig
#
#     if last_dig > max_dig:
#         max_dig = last_dig
#
#     num = num // 10
#
# print('Максимальная цифра равна', max_dig)
#
# print('Минимальная цифра равна', min_dig)

# counter = 0
# counter2 = 0
# total = 1
# arif = 0
# first_num = 0
# first_last_num = 0
# num = 5678
# last_dig2 = num % 10
# while num != 0:
#     last_dig = num % 10
#     counter += last_dig
#     counter2 += 1
#     total *= last_dig
#     arif = counter / counter2
     # first_num = (num % 10 ** (counter2 - 1))
#     first_last_num = first_num + last_dig2
#     num = num // 10
# print(counter)
# print(counter2)
# print(total)
# print(arif)
# print(first_num)
# print(first_last_num)



# n = 476962
# while n > 9:
#     last_dig = n % 10
#     n = n // 10
#print(last_dig)



# counter = 0
# n = 1111
# last_dig = n % 10
# while n != 0:
#     last_dig2 = n % 10
#     if last_dig == last_dig2:
#         counter += 0
#     else:
#         counter += 1
#     n = n // 10
#
# if counter == 0:
#     print('YES')
# else:
#     print('NO')







# flag = True
# n = 43321 #9876543210
#
# while n // 10 > 0:
#     if (n // 10) % 10 <= n % 10:
#         flag = False
#     n = n // 10
#     print(flag)
#
# if flag == True:
#     print('YES')
# else:
#     print('NO')


# n = 106553210   #5321 #1234
# # prelast_dig = n % 100 // 10
# # last_dig2 = n % 10
# while n % 10 <= n % 100 // 10:
#     n = n // 10
#     print(n)
# print('YES' if n < 10 else 'NO')



# n = 15
# for i in range(2, n + 1):
#     if n % i == 0:
#         break
# print(i)




# n = 10
# for i in range(1, n + 1):
#     if 5 <= i <= 9 or 17 <= i <= 37 or 78 <= i <= 87:
#         continue
#     print(i)




# flag = False
# n = 20
# num = n
# while n != 0:
#     # last_dig = n % 10
#     if n == 22:
#         flag = True
#         break
#     # n //= 10
#     n -= 1
#
# if flag is True:
#     print('V chisle ', num, "est' ", n)
# else:
#     print('V chesle ', num, 'net 22')








# n = 495672
#
# while n > 10:
#     last_dig = n % 10
#     n //= 10
# print(last_dig)


# counter = 0
# n = 14111
# last_dig = n % 10
# while n != 0:
#     last_dig2 = n % 10
#     if last_dig != last_dig2:
#         counter += 1
#     n //= 10
# if counter == 0:
#     print('YES')
# else:
#     print('NO')


# n = 52321
# while n % 10 <= n % 100 // 10:
#     n //= 10
# print('YES' if n < 10 else 'NO')


# flag = True
# n = 554311
# b = 'YES'
# while n // 10 != 0:
#     last_dig = n % 10
#     prelast = n % 100 // 10
#     n //= 10
#     if last_dig > prelast:
#         b = 'NO'
#
# print(b)

# counter = 0
# max_dig = -10**6 - 1
#
# for i in range(1, 11):
#     x = -44
#     if x < 0:
#         counter += x
#     if x > max_dig and x < 0:
#         max_dig = x
# if counter < 0:
#     print(counter)
#     print(max_dig)
# else:
#     print('NO')

# s = 0 #3
# for i in range(1, 8): #1
#     n = int(input())
#     if n % 2 == 0:
#         s += n
#
# if s > 0:
#     print(s)
# else:
#     print(0)


# n = 555555
# max_dig = -1
#
# while n != 0:
#     digit = n % 10
#     if digit % 3 == 0:
#         if digit > max_dig:
#             max_dig = digit
#
#     n = n // 10
# if max_dig == -1:
#     print('NO')
# else:
#     print(max_dig)

# n = 456
# while n > 9:
#     n //= 10
# print(n)

# n = 53453 #1
# product = 1 #2
# while n != 0: #3
#     digit = n % 10
#     product *= digit
#     n //= 10
# print(product)

#
# n = 8
# for i in range(n):
#     for j in range(3):
#         print(n, end=' ')
#     print()

# n = 3
# for i in range(1, n + 1):
#     for j in range(5):
#         print(i, end=' ')
#     print()
#
# n = 3
# for i in range(1, n + 1):
#     for k in range(1, 10):
#         print(f'{i} + {k} = {i + k}', end='\n')
#     print()

# n = 11
# for i in range(n//2+1):
#     # for _ in range(n - 1, 1, -1):
#     for k in range(i + 1):
#         print('*', end='')
#     print()
# for _ in range(n//2, 0, -1):
#     for _1 in range(_):
#         print('*', end='')
#     print()

# n = 5
# for i in range(1, n + 1):
#     for k in range(i):
#         print(i, end='')
#     print()

# from string import printable
# password = 'gT4!'
# for b1 in printable:
#     if b1 == password[0]:
#         print(b1)
# for b2 in printable:
#     if b2 == password[1]:
#         print(b2)
# for b3 in printable:
#     if b3 == password[2]:
#         print(b3)
# for b4 in printable:
#     if b4 == password[3]:
#         print(b4)

# for b in range(0, 100):
#     for c in range(0, 100):
#         for t in range(0, 100):
#             if 10 * b + 5 * c + 0.5 * t == 100 and b + c + t == 100:
#                 print('b = ', b, 'c = ', c, 't = ', t, end=' ')
#     print()

# counter1 = 0
# counter2 = 0
# wom = [44, 75, 56, 99, 77]
# man = [155, 44, 65, 43, 84]
# for i in wom:
#     counter1 += i
# for i in man:
#     counter2 += i
# if counter1 > counter2:
#     print(f'Женщины живут дольше мужчин на {counter1 - counter2} лет')
# elif counter2 > counter1:
#     print(f'Мужчины живут дольше женщин на {counter2 - counter1} лет')



# list1 = [1, 2, 3, 4], [2, 3, 4, 5], [3, 4, 5, 6]
# list2 = [7, 1, 9, 1], [2, 2, 2, 2], [3, 3, 3, 3]
# c = []
# for i, j in enumerate(list1):
#     r = []
#     for k, _ in enumerate(j):
#         r.append(_ + list2[i][k])
#     c.append(r)
#
# print(c)

# total = 0
# n = 6
# for i in range(1, n + 1):
#     for k in range(i):
#         total += 1
#
#         print(total, end=' ')
#     print()

# total = 0
# n = 5
#
# for i in range(1, n + 1):
#     for k in range(i):
#         print(k + 1, end='')
#     for j in range(i - 1, 0, -1):
#
#         print(j, end='')
#     print()


# counter = 0
# a = 101
# b = 110
# largest = 0
# for i in range(a, b + 1):
#     total = 0
#     for j in range(1, i + 1):
#         if i % j == 0:
#             total += j
#             if total >= counter and i >= largest:
#                 counter = total
#                 largest = i
# print(largest, counter, end=' ')



# n = 5
# for i in range(1, n + 1):
#     total = 0
#     for k in range(1, i + 1):
#         if i % k == 0:
#             total += 1
#     print(i, total * '+', sep='')




# num = 192
# while num > 9:
#     sum = 0
#     while num > 0:
#         last_dig1 = num % 10
#         sum += last_dig1
#         num //= 10
#     num = sum
# print(num)


# a = 2
# b = 15
# for i in range(a, b + 1):
#     counter = 0
#     for k in range(1, i + 1):
#         if i % k == 0:
#             counter += 1
#     if counter == 2:
#         print(i)


# tracker1 = 0
# tracker2 = 0
# tracker3 = 0
# tracker4 = 0
# for i in range(2): # 1 блок 1
#     tracker1 += 1 # 2
#     for m in range(2): # 2 блок 2 1
#         tracker2 += 1 # 4
#         for j in range(2): # 3 блок 4 1
#             tracker3 += 1 # 8
#             for l in range(2): # 4 блок 8 1
#                 tracker4 += 1 # 16
#
# print(tracker1)
# print(tracker2)
# print(tracker3)
# print(tracker4)

# n = 3
#
# for i in range(1, n + 1):
#     total = 1
#     counter = 0
#     for k in range(1, i + 1):
#         total *= k
#         counter += total
# print(counter)


    # n = 8
    # count = 0
    # maximum = -10**6 - 1 # МАКС делящиеся нацело
    # for i in range(1, n + 1):
    #     x = 11
    #     if x % 4 == 0:
    #         count += 1
    #         if x > maximum:
    #             maximum = x
    # if count > 0:
    #     print(count)
    #     print(maximum)
    # else:
    #     print('NO')

# n = 3
# for i in range(1, n + 1):
#     for k in range(1, i + 1):
#         print(i)

# n = 5
# for i in range(1):
#     print(19 * '*')
# for j in range(n - 2):
#     print('*', 1 * '*', sep='                 ')
# for k in range(1):
#     print(19 * '*')


# three_num = 0
# replay_last_dig = 0
# even_dig = 0
# bigger5 = 0
# dig7 = 1
# dig5_0 = 0
#
# n = 56689932106
# last_dig2 = n % 10
# while n != 0:
#     last_dig = n % 10
#     if last_dig == 3:
#         three_num += 1
#     if last_dig2 == last_dig:
#         replay_last_dig += 1
#     if last_dig % 2 == 0:
#         even_dig += 1
#     if last_dig > 5:
#         bigger5 += last_dig
#     if last_dig > 7:
#         dig7 *= last_dig
#     if last_dig == 5 or last_dig == 0:
#         dig5_0 += 1
#
#     n //= 10
# print(three_num)
# print(replay_last_dig)
# print(even_dig)
# print(bigger5)
# print(dig7)
# # if dig7 != 0:
# #     print(dig7)
# # else:
# #     print(1)
# print(dig5_0)

# total = 0
# total2 = 0
# counter = 0
# for i in range(1, 33):
#     for k in range(1, 33):
#         for j in range(1, 33):
#             for _ in range(1, 33):
#                 if i != k and i != j and i != _ and k != j and k != _ and j != _:
#                     total = i**3 + k**3
#                     total2 = j**3 + _**3
#                     if total == total2:
#                         counter = total
#                         print(counter)

#
# s = 'abc'
# for i in range(-1, -len(s) - 1, -1):
#     print(s[i])


# text = 'Hi 8 Python'
# numbers = '0123456789'
# counter = 0
# for i in range(len(text)):
#     for k in range(len(numbers)):
#         if numbers[k] in text[i]:
#             counter += 1
# if counter > 0:
#     print('Цифра')
# else:
#     print('Цифр нет')

# string = 'bcd+a++++**31415'
# plus = '+'
# star = '*'
# plus1 = 0
# star1 = 0
# for i in range(len(string)):
#     for k in range(len(plus)):
#         if plus in string[i]:
#             plus1 += 1
#         for j in range(len(star)):
#             if star in string[i]:
#                 star1 += 1
# print('Символ + встречается', plus1, 'раз')
# print('Символ * встречается', star1, 'раз')


# string = 'bcd+a++++**31415'
# string_lenght = len(string)
# index = 0
# index2 = 0
# plus = '+'
# star = '*'
# plus1 = 0
# star1 = 0
# while index != string_lenght:
#     if string[index] in plus:
#         plus1 += 1
#     index += 1
# while index2 != string_lenght:
#     if string[index2] in star:
#         star1 += 1
#     index2 += 1
#
#
# print('Символ + встречается', plus1, 'раз')
# print('Символ * встречается', star1, 'раз')



# text = 'aaaabbccd'
# counter = 0
# letters = ''
# for i in text:
#     if i in letters:
#         counter += 1
#     letters += i
# print(counter)

#
# text = 'Вдохновение – это умение приводить себя в рабочее состояние!'
# vowels = 'ауоыиэяюёе'
# consonants = 'бвгджзйклмнпрстфхцчшщ'
# counter_for_vowels = 0
# counter_for_consonants = 0
# for i in text:
#     if i.lower() in vowels:
#         counter_for_vowels += 1
#     elif i.lower() in consonants:
#         counter_for_consonants += 1
# print(f'Количество гласных букв равно {counter_for_vowels}')
# print(f'Количество согласных букв равно {counter_for_consonants}')
#
#
# text = 'Вдохновение – это умение приводить себя в рабочее состояние!'
# len_symbol_text = len(text)
# vowels = 'ауоыиэяюёе'
# consonants = 'бвгджзйклмнпрстфхцчшщ'
# counter_for_vowels = 0
# counter_for_consonants = 0
# index = 0
# while index != len_symbol_text:
#     if text[index].lower() in vowels:
#         counter_for_vowels += 1
#     elif text[index].lower() in consonants:
#         counter_for_consonants += 1
#     index += 1
# print(f'Количество гласных букв равно {counter_for_vowels}')
# print(f'Количество согласных букв равно {counter_for_consonants}')

# num = 1025
# text = ''
# while num > 0:
#     text = str(num % 2) + text cчитаем двоичную систему
#     num //= 2
# print(text)


# text = 'потоп'
# print('YES' if text[:] == text[::-1] else 'NO')

# text = 'Hello'
# result_string = ''
# for i in range(len(text) - 1, -1, -1):
#     result_string += text[i]
#
# print(result_string)

# string = 'abcdefghijklmnopqrstuvwxyz'
# len_string = len(string)
# x3_string = string[:] + string[:] + string[:]
# first_string = string[0]
# first3_letters = string[0:3]
# last3_letters = string[-3:]
# versa_string = string[::-1]
# remote_string = string[1:-1]
# print(len_string)
# print(x3_string)
# print(first_string)
# print(first3_letters)
# print(last3_letters)
# print(versa_string)
# print(remote_string)

# string = 'abcdefghijklmnopqrstuvwxyz'
# symbol3 = string[2]
# pre_last_symbol = string[-2]
# first5_symbol = string[:5]
# all_string = string[0:-2]
# even_symbol = string[::2]
# contants_symbol = string[1::2]
# versa_string = string[::-1]
# versa2 = string[-1::-2]
# print(symbol3)
# print(pre_last_symbol)
# print(first5_symbol)
# print(all_string)
# print(even_symbol)
# print(contants_symbol)
# print(versa_string)
# print(versa2)

# string = 'abcdefg'
# len_string = len(string)
# x = len(string)//2 + len(string) % 2 #делим строку на 2
# slice1 = string[0:x]
# slice2 = string[x:]
# print(slice2 + slice1)

# name = 'Chris Alan'
# name_cap = name.title()
#
# if name == name_cap:
#     print('YES')
# else:
#     print('NO')

# string = input().lower()
# good = 'хорош'
# if good in string.lower():
#     print('YES')
# else:
#     print('NO')


# string = 'abcABCD12345'
# string_upper = string.upper()
# counter = 0
# num = '0123456789'
# for i in string:
#     if i not in string_upper and i not in num:
#         counter += 1
# print(counter)

# string = 'abfr4cABCD12345'
# letter_lower = string.lower()
# num = '01234567789'
# index = 0
# counter = 0
# counter2 = 0
# while index != len(string):
#     if string[index] == letter_lower[index]:
#         counter += 1
#         if string[index] in num:
#             counter2 += 1
#     index += 1
# print(counter - counter2)

# string = 'abcABCD12345'
# letter_lower = 'abcdefghijklmnopqrstuvwxyz'
# counter = 0
# for i in string:
#     if i in letter_lower:
#         counter += 1
# print(counter)
#
# s = 'Hello world'
# print(s.count(' ') + 1)

# text = 'АааГГЦЦцТТттт'
# text = text.lower()
# print('Аденин:', text.count('а'))
# print('Гуанин:', text.count('г'))
# print('Цитозин:', text.count('ц'))
# print('Тимин:', text.count('т'))


# string = '1v2b3n4m5k6h7GDFGDFd'
# counter = 0
# index = 0
# while len(string) != index:
#     if string[index] not in string.upper():
#         counter += 1
#     index += 1
# print(counter)

# score_mess = 3
# counter = 0
# for i in range(score_mess):
#     mess1 = '11helpme11jim11'
#     if mess1.count("11") >= 3:
#         counter += 1
# print(counter)

# string = 'l33t 3301'
# num = '0123456789'
# counter = 0
# index = 0
# for i in range(len(string)):
#     if string[index] in num:
#         counter += 1
#     index += 1
# print(counter)


# string = 'l33t 3301'
# num = '0123456789'
# counter = 0
# if string.count('3') in num:
#     counter += 1
# print(counter)

# string = 'l33t 3301'
# string2 = ''
# num_list = '0123456789'
# for i in string:
#     if i in num_list:
#         string2 += i
# print(len(string2))
#
# n = 'l33t 33701'
# counter = 0
# for i in range(10):
#     counter += n.count(str(i))
# print(counter)

# string = 'www.stepik.org'
# if string.endswith('.com') or string.endswith('.ru'):
#     print('YES')
# else:
#     print('NO')

# string = 'www.stepik.org'
# if string.count('.com') == True or string.count('.ru') == True:
#     print('YES')
# else:
#     print('NO')

# string = '1112211111111111111111111111111111111111'
# counter2 = 0
# letter = ''
# counter = ''
# for i in string:
#     counter = string.count(i)
#     if counter >= counter2:
#         counter2 = counter
#         letter = i
# print(letter)

# string = 'abcdefgfhfabc'
# score = string.count('f')
# if score == 1:
#     print(string.find('f'))
# elif score >= 2:
#     print(string.find('f'), string.rfind('f'))
# else:
#     print('NO')

# string = 'ahahahahaha'
# slices1 = string[:string.find('h')]
# slices2 = string[string.rfind('h') + 1:]
# print(slices1 + slices2)

# price = '10k'
# crypto = 'Bitcoin'
# year = 2010
# s = 'In {0}, someone paid {1} {2} for two pizzas.'.format(year, price, crypto)
#
# print(s)

# year = 2010
# amount = '10K'
# currency = 'Bitcoin'
#
# print(f'In {year}, someone paid {amount} {currency} for two pizzas.')

# num1 = 65
# num2 = 70
# for i in range(num1, num2 + 1):
#     print(chr(i),end=' ')

# string = 'Hello world!'
# for i in string:
#     print(ord(i), end=' ')

# string = 'Hello world!'
# index = 0
# symbol_uni = 0
# while index != len(string):
#     symbol_uni = ord(string[index])
#     index += 1
#     print(symbol_uni, end=' ')



# shift = 14
# text = 'hmispcy'
# alfa = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'.lower()
# new_alfa = alfa[shift:len(alfa)] + alfa[0:shift]
# for k in text:
#     for_cipher = 0
#     for i in new_alfa:
#         if k != i:
#             for_cipher += 1
#         elif k == i:
#             break
#     print(alfa[for_cipher], end='')

# string = 'Python'
# new_string = ''
# index = -1
# for i in string:
#     index += 1
#     if index % 3 == 0:
#         continue
#     new_string += i
# print(new_string)

# string = 'Python'
# for i in range(len(string) + 1):
#     if i % 3 != 0:
#         print(string[i], end='')

# string = '1231'
# print(string.replace('1', 'one'))

# string = 'affective'
# count = 0
# for i in string:
#     if i == 'f':
#         count += 1
# if count == 1:
#     print('-1')
# elif count == 0:
#     print('-2')
# else:
#     print(string.replace('f', ' ', 1).find('f'))

# string = 'affective'
# if string.count('f') == 1:
#     print('-1')
# elif string.count('f') == 0:
#     print('-2')
# else:
#     print(string.replace('f', ' ', 1).find('f'))


# string = 'abch12345h'
# versa_string = ''
# for i in string:
#     if i != 'h':
#         versa_string += i
#     elif i == 'h':
#         print()

# string = 'ahbhchdheha'
# first_h = string.find('h')
# second_h = string.rfind('h')
# index_string1 = string[0:first_h]
# index_string2 = string[second_h:first_h:-1]
# index_string3 = string[second_h:]
# print(index_string1 + index_string2 + index_string3)


# num = 5
# new_list = list(range(1, num + 1))
# print(new_list)

# num = 5
# alfa = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
# print(alfa[:num])


# numbers = [12.5, 3.1415, 2.718, 9.8, 1.414, 1.1618, 1.324]
# min1 = [min(numbers)]
# max1 = [max(numbers)]
# print(sum(min1 + max1))

# rainbow = ['Red', 'Orange', 'Yellow', 'Green', 'Blue', 'Indigo', 'Violet']
# count = 0
# for i in rainbow:
#     if i == 'Green':
#         rainbow[count] = 'Зеленый'
#     elif i == 'Violet':
#         rainbow[count] = 'Фиолетовый'
#     count += 1
# print(rainbow)

# numbers1 = [1, 2, 3]
# numbers2 = [6]
# numbers3 = [7, 8, 9, 10, 11, 12, 13]
# print(numbers1 * 2 + numbers2 * 9 + numbers3)

# numbers = [2, 6, 3, 14, 10, 4, 11, 16, 12, 5, 4, 16, 1, 0, 8, 16, 10, 10, 8, 5, 1, 11, 10, 10, 12, 0, 0, 6, 14, 8, 2, 12, 14, 5, 6, 12, 1, 2, 10, 14, 9, 1, 15, 1, 2, 14, 16, 6, 7, 5]
# print(len(numbers))
# print(numbers[-1])
# print(numbers[::-1])
# print('YES' if 5 in numbers and 17 in numbers else 'NO')
# del numbers[0]
# del numbers[-1]
# print(numbers)

# num = 5
# count = 0
# mylist = []
# while num > count:
#     string = 'fa'
#     mylist.append(string)
#     count += 1
# print(mylist)

# num = 5
# count = 0
# mylist = []
# for i in range(1, num + 1):
#     string = 'fae'
#     mylist.append(string)
# print(mylist)

# alfa = 'abcdefghijklmnopqrstuvwxyz'
# for i in range(1, len(alfa) + 1):
#     for k in range(1, i + 1):
#         print(k, end='')
#     print()

# alfa = 'abcdefghijklmnopqrstuvwxyz'
# mylist = []
# index = 0
# for i in range(1, len(alfa) + 1):
#     for k in alfa[index]:
#         mylist.append(k * i)
#     index += 1
# print(mylist)

# mylist = []
# index = 1
# for i in range(ord('a'), ord('z') + 1):
#     mylist.append(chr(i) * index)
#     index += 1
# print(mylist)

# n = 5
# mylist = []
# for i in range(1, n + 1):
#     num = 2
#     mylist.append(num ** 3)
# print(mylist)

# num = 36
# mylist = []
# for i in range(1, num + 1):
#     if num % i == 0:
#         mylist.append(i)
# print(mylist)

# n = 5
# mylist = []
# total = 0
# for i in range(n):
#     numbers = int(input()) #1 2 3 4 5
#     total += numbers
#     mylist.append(total)
#     total = numbers
# print(mylist[1:])

# n = 5
# list1 = []
# list2 = []
# count = 0
# for i in range(n):
#     num = int(input())
#     list2.append(num)
# while len(list2) > 1:
#     count = list2[0] + list2[1]
#     list1.append(count)
#     del list2[0]
# print(list1)

# n = 5
# list1 = []
# list2 = []
# count = 0
# for i in range(n):
#     num = int(input())
#     list2.append(num)
# for i in range(len(list2)):
#     if len(list2) < 2:
#         break
#     count = list2[0] + list2[1]
#     list1.append(count)
#     del list2[0]
# print(list1)

# n = 1
# mylist = []
# mylist2 = []
# counter = 0
# for i in range(n):
#     num = int(input())
#     mylist.append(num)
# print(mylist[::2])

# n = 10
# mylist = []
# for i in range(n):
#     num = int(input())
#     mylist.append(num)
# del mylist[1::2]
# print(mylist)

# mylist = 'abcdef'
# index = []
# index.append(mylist[1])
# print(index)

# n = 5
# k = 2 - 1
# mylist = []
# string2 = ''
# for i in range(n):
#     string = 'input()'
#     if len(string) < 3:
#         continue
#     elif len(string) >= 3:
#         mylist.append(string[k])
# print(mylist.join(mylist))

# n = 5
# mylist = []
# string2 = []
# for i in range(n):
#     string = input()
#     string2.append(string)
#
# last = 2
# for j in string2:
#     if len(j) >= last:
#         mylist.append(j[last-1])
# string3 = ''.join(mylist)
# print(string3)


# n = 5
# string2 = []
# for i in range(n):
#     string = input()
#     string2.append(string)
# last = 2
# string3 = ''
# for j in string2:
#     if len(j) >= last:
#         string3 += j[last-1]
# print(string3)


# n = 5
# string2 = []
# for i in range(n):
#     string = input()
#     string2.append(string)
#
# index = 0
# last = 2
# string3 = ''
# while len(string2) != index:
#     if len(string2[index]) >= last:
#         string3 += string2[index][last-1]
#     index += 1
# print(string3)

# n = 3
# mylist = []
# for i in range(n):
#     string = input()
#     mylist.extend(string)
# print(mylist)

# n = 5
# counter = 0
# mylist1 = []
# mylist2 = []
# for i in range(1, n + 1):
#     num = 1
#     f = (num ** 2) + 2 * num + 1
#     mylist1.append(num)
#     mylist2.append(f)
# print(*mylist1, sep='\n')
# print()
# print(*mylist2, sep='\n')

# n = 3
# mylist = []
# for i in range(n):
#     num = int(input())
#     mylist.append(num)
# min1 = min(mylist)
# max1 = max(mylist)
# mylist2 = []
# for k in mylist:
#     if k != min1 and k != max1:
#         mylist2.append(k)
# print(*mylist2, sep='\n')

# n = int(input())
# mylist = []
# for i in range(n):
#     mylist.append(int(input()))
# for k in mylist:
#     if k != min(mylist) and k != max(mylist):
#         print(k)
#
# n = 5
# mylist = []
# for i in range(n):
#     mylist.append(input())
# string = []
# for k in mylist:
#     if k not in string:
#         string.append(k)
# print(*string, sep='\n')


# n = 5
# mylist = []
# for i in range(n):
#     string_search = input()
#     mylist.append(string_search)
# search_request = input()
# mylist2 = []
# for k in mylist:
#     if search_request.lower() in k.lower():
#         mylist2.append(k)
# print(*mylist2, sep='\n')
#

# n = int(input())
# mylist = []
# for i in range(n):
#     string_search = input()
#     mylist.append(string_search)
#
# n_search = int(input())
# mylist_search = []
# for j in range(n_search):
#     search_request = input()
#     mylist_search.append(search_request)
# search_request = mylist_search
# mylist2 = []
# for k in mylist:
#     if mylist_search.lower() in k.lower():
#         mylist2.append(k)
# print(*mylist2, sep='\n')

# n = int(input())
# mylist = []
# for i in range(n):
#     string_search = input()
#     mylist.append(string_search)
#
# n_search = int(input())
# mylist_search = []
# for j in range(n_search):
#     search_request = input()
#     mylist_search.append(search_request)
#
# search_request2 = ' '.join(mylist_search)
# mylist2 = []
# for k in mylist:
#     if search_request2.lower() in k.lower():
#         mylist2.append(k)
# print(*mylist2, sep='\n')

# n = int(input())
# mylist = []
# for i in range(n):
#     string_search = input()
#     mylist.append(string_search)
#
# n_search = int(input())
# mylist_search = []
# for j in range(n_search):
#     search_request = input()
#     mylist_search.append(search_request)
#
# mylist2 = []
# for k in mylist:
#     counter = 0
#     for _ in mylist_search:
#         if _.lower() in k.lower():
#             counter += 1
#             if counter == len(mylist_search):
#                 mylist2.append(k)
# print(*mylist2, sep='\n')


# mylist = []
# for i in range(int(input())):
#     mylist.append(int(input()))
# mylist2 = []
# for i in mylist:
#     if i <= -1:
#         mylist2.append(i)
# for k in mylist:
#     if k == 0:
#         mylist2.append(k)
# for j in mylist:
#     if j >= 1:
#         mylist2.append(j)
# print(*mylist2, sep='\n')

# string = 'У лукоморья дуб зеленый златая цепь на дубе том'
# list1 = string.split()
# print(*list1, sep='\n')

# string_fio = 'Гуев Тимур Ахсарбекович'.split()
# mylist = []
# for i in string_fio:
#     mylist.append(i[0])
# print(*mylist, sep='.', end='.')

# string = 'C:\Windows\System32\calc.exe'.split("\\")
# print(*string, sep='\n')

# string_num = '5 3 1 7 10 2'.split()
# plus = '+'
# for i in string_num:
#     print(plus * int(i))

# string_ip = '192.168.0.300'.split('.')
# counter = 0
# for i in string_ip:
#     if int(i) <= 255:
#         counter += 1
# if counter == 4:
#     print('ДА')
# else:
#     print('НЕТ')

# string_ip = '192.1111.0.1111'.split('.')
# counter = 0
# for i in string_ip:
#     if int(i) >= 255:
#         print('НЕТ')
#         break
# else:
#     print('ДА')


# string_num = 'qwerty and password'
#
# separator = '**'
# index = 0
# new_string = ''
# while index != len(string_num):
#     for i in string_num[index]:
#         new_string += i + separator
#     index += 1
# print(new_string[:-len(separator)].replace(' ', ''))

# string_num = 'qwerty and password'
# s = '**'.join(string_num)
# print(s)

# string_num = '3 3 3 3 3'.split()
# counter = 0
# for i in range(len(string_num)):
#     for k in range(i + 1, len(string_num)):
#         if string_num[i] == string_num[k]:
#             counter += 1
# print(counter)

# food = ['Рис', 'Курица', 'Рыба', 'Брокколи', 'Рис']
# while 'Рис' in food:
#     food.remove('Рис')
# print(food)

# numbers = [8, 9, 10, 11]
# numbers[1] = 17
# numbers.extend([4, 5, 6])
# numbers.pop(0)
# copy_numbers = numbers.copy()
# numbers.insert(3, 25)
# print(numbers + copy_numbers)

# string_numbers = '3 4 5 2 1'
# numbers = string_numbers.split()
# mylist = []
# for i in numbers:
#     mylist.append(int(i))
# num_max = max(mylist)
# num_min = min(mylist)
# if mylist.index(num_min) > mylist.index(num_max):
#     mylist.insert(mylist.index(num_min), num_max)
#     mylist.remove(num_min)
#     mylist.insert(mylist.index(num_max), num_min)
#     mylist.remove(num_max)
# else:
#     mylist.insert(mylist.index(num_max), num_min)
#     mylist.remove(num_max)
#     mylist.insert(mylist.index(num_min), num_max)
#     mylist.remove(num_min)
#
# string1 = []
# for k in mylist:
#     string1.append(str(k))
# print(*string1)

#
# string_text = '	William Shakespeare was born in the town of Stratford, England, in the year 1564. When he was a young man, Shakespeare moved to the city of London, where he began writing plays. His plays were soon very successful, and were enjoyed both by the common people of London and also by the rich and famous. In addition to his plays, Shakespeare wrote many short poems and a few longer poems. Like his plays, these poems are still famous today.'
# articul = 'a an the'
# count = 0
# for i in string_text.split():
#     if i.lower() in articul.lower().split():
#         count += 1
# print('Общее количество артиклей:', count)

# a = [[12, 4, 11, 6],
#      [5, 14, 55, 6],
#      [6, 7, 8, 9]
#      ]
# mist = 0
# for k in range(4):
#     for i in range(3):
#
#         mist += a[i][k]
#         print(a[i][k], end=' ')
#     print()

# mylist = []
# for i in range(int(input())):
#     string = input()
#     mylist.append(string)
# mylist = ['print("Введите своё имя")', 'name = input()', 'print("Введите пароль, если имеется")'
#                                     '# ахахахах вам не поймать меня', 'password = input()', 'if password == "hoover":',
#           'print("Здравствуйте, рыцарь", name)         #долой Макнамару', 'elif password == "noncr":',
#           'print("Здравствуйте, паладин", name)', 'elif password == "gelios":',
#           'print("Здравствуйте, старейшина", name)          #Элайджа вперёд', 'else:',
#           'print("Здравствуйте, послушник", name)']
# for k in mylist:
#     if '#' in k:
#         k = k[:k.index('#')]
#     print(k.rstrip())

# string = '4 5 1 2 3 8'.split()
# string2 = string.copy()
# string.sort()
# string2.sort(reverse=True)
#
# print(f'{string} ', end='\n'
#                                   f'{string2}')

# string = '4 5 1 2 3 8'.split()
# s = []
# for i in string:
#     s.append(int(i))
#     s.sort()
# print(*s)
# s.sort(reverse=True)
# print(*s)

# def cat_voice(voice = 'Meow!'):
#     return voice
# x = cat_voice()
# print(x * 2)
#
# def dog_voice(voice = 'Woof!'):
#     return voice
# y = dog_voice()
# print(y * 2)

# def get_voice(animal):
#     if animal == 'cat':
#         print('Meow!')
#         return animal
#     elif animal == 'dog':
#         print('Woof!')
#         return animal
#
#
# value = get_voice('cat')
# value = get_voice('dog')

# def generation_odd_numbers(a, b):
#     odd_list = []
#     for i in range(a, b +1):
#         if i % 2 != 0:
#             odd_list.append(i)
#     print(odd_list)
#
#
# generation_odd_numbers(1, 20)


#List Comprehension
# greetings = ['hello', 'hi', 'hey', 'hola']
# letter_list = [letter[1] for letter in greetings]
# print(letter_list)

# greetings = ['hello', 'hi', 'hey', 'hola']
# letter_list = []
# for i in greetings:
#     letter_list.append(i[1])
# print(letter_list)

# digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# new_list = [odd for odd in digits if odd % 2 != 0]
# print(new_list)

# digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# new_list = []
# for i in digits:
#     if i % 2 != 0:
#         new_list.append(i)
# print(new_list)
#
# def draw_box():
#     for i in range(1):
#         print(10 * '*')
#     for k in range(12):
#         print('*', 1 * '*', sep='        ')
#     for j in range(1):
#         print(10 * '*')
#
#
# draw_box()

# def draw_triangle():
#     for i in range(11):
#         print(i * '*')
#
#
# draw_triangle()

# def draw_triangle(fill='*', base=9):
#     for i in range(base//2+1):
#         for k in range(i + 1):
#             print(fill, end='')
#         print()
#     for _ in range(base//2, 0, -1):
#         for _1 in range(_):
#             print(fill, end='')
#         print()
#
# draw_triangle()

# def print_fio(name, surname, patronymic):
#     for i in surname[0].title():
#         print(i, end='')
#     for k in name[0].title():
#         print(k, end='')
#     for j in patronymic[0].title():
#         print(j, end='')
#
#
#
# print_fio('Александр', 'Пушкин', 'Сергеевич')


# def print_digit_sum(num):
#     mylist = []
#     while num > 0:
#         last_dig = num % 10
#         mylist.append(last_dig)
#         num //= 10
#     print(sum(mylist))
#
#
# print_digit_sum(12345)


# def convert_to_celsius(temp):
#     result = (5 / 9) * (temp - 32)
#     return result
#
# # основная программа
# temp = float(66.7)
# celsius = convert_to_celsius(temp)
# print(celsius)  # градусы Цельсия

# def complex(num1, num2):
#     return num1 * num2
#
#
#
# x = complex(5, 2)
# print(x)
# x = complex(5, 4)
# print(x)

# def sum_digits(n):
#     result = 0
#     while n > 0:
#         result += n % 10
#         n //= 10
#     return result
#
#
# n = 55
# print(sum_digits(n))

# def convert_to_miles(km):
#     return km * 0.6214
#
# km = int(input())
# print(convert_to_miles(km))

# def get_days(month):
#     mon = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
#     return mon[month - 1]
#
#
# month = 1
# print(get_days(month))

# def get_factors(num):
#     mylist = []
#     for i in range(1, num + 1):
#         if num % i == 0:
#             mylist.append(i)
#     return mylist
#
#
# num = 10
# print(len(get_factors(num)))


# def find_all(target, symbol):
#     mylist = []
#     for i in range(len(target)):
#         if symbol in target[i]:
#             mylist.append(i)
#     return mylist
#
#
# target = 'abcdabcaaa'
# symbol = 'a'
# print(find_all(target, symbol))


# def merge(list1, list2):
#     mylist = []
#     for i in list1:
#         mylist.append(i)
#     for k in list2:
#         mylist.append(k)
#     mylist.sort()
#     return mylist
#
#
# list1 = [1, 3, 2]
# list2 = [5, 6, 7, 8]
# print(merge(list1, list2))

# def merge(list1, list2):
#     k = list1 + list2
#     k.sort()
#     return k
#
#
# list1 = [1, 3, 2]
# list2 = [5, 6, 7, 8]
# print(merge(list1, list2))


# def quick_merge(mylist2):
#     mylist = []
#     for i in range(len(mylist2)):
#         mylist.append(mylist2[i])
#     mylist.sort()
#     return mylist
# 
#
# num = 3
# mylist2 = []
# for k in range(num):
#     string_num = [int(i) for i in input().split()]
#     mylist2 += string_num
# print(*quick_merge(mylist2))

# def is_valid_triangle(side1, side2, side3):
#     if side1 + side2 > side3 and side1 + side3 > side2 and side3 + side2 > side1:
#         return True
#     else:
#         return False
#
#
# side1, side2, side3 = 2, 2, 2
# print(is_valid_triangle(side1, side2, side3))

# def is_prime(num):
#     for i in range(num, num + 1):
#         count = 0
#         for k in range(1, i + 1):
#             if i % k == 0:
#                 count += 1
#         if count == 2:
#             return True
#         else:
#             return False
#
#
# num = 10
# print(is_prime(num))


# def is_prime(num):
#     for i in range(num, num + 1):
#         count = 0
#         for k in range(1, i + 1):
#             if i % k == 0:
#                 count += 1
#         if count == 2:
#             return True
#         else:
#             return False
#
#
# def get_next_prime(num):
#     num += 1
#     if is_prime(num) == False:
#         while is_prime(num) != True:
#             num += 1
#     return num
#
#
# num = 7
# print(get_next_prime(num))


# def is_password_good(password):
#     count_l = 0
#     count_low = 0
#     count_up = 0
#     count_d = 0
#     num = '0123456789'
#     for i in range(len(password)):
#         if len(password) >= 8:
#             count_l += 1
#         if password[i] in num:
#             count_d += 1
#         if password[i].upper() == password[i] and password[i] not in num:
#             count_up += 1
#         if password[i].lower() == password[i] and password[i] not in num:
#             count_low += 1
#     if count_l >= 1 and count_d >= 1 and count_up >= 1 and count_low >= 1:
#         return True
#     else:
#         return False
#
#
# password = 'FFFFFFFFFFFFF2f'
# print(is_password_good(password))


# def is_one_away(word1, word2):
#     count = 0
#     for i in range(len(word1)):
#         if word1[i] != word2[i]:
#             count += 1
#     return count == 1 and len(word1) == len(word2)
#
#
# word1 = 'bike'
# word2 = 'hike'
# print(is_one_away(word1, word2))

# def is_palindrome(text):
#     if text.lower().replace(' ', '').replace(',', '').replace('.', '').replace('-', '').replace('!', '').replace('?', '')\
#             == text[::-1].lower().replace(' ', '').replace(',', '').replace('.', '').replace('-', '').replace('!', '').replace('?', ''):
#         return True
#     else:
#         return False
#
#
# text = 'Zoo belt to be Russia, is sure bottle booz.'
# print(is_palindrome(text))


# def is_valid_password(password):
#     count_prime = 0
#     flag = False
#     if len(password) > 3:
#         return False
#     if password[0] != password[0][::-1]:
#         return False
#     num = int(password[1])
#     for i in range(num, num + 1):
#         for k in range(1, i + 1):
#             if i % k == 0:
#                 count_prime += 1
#     if count_prime == 2:
#         flag = True
#     num2 = int(password[2])
#     if num2 % 2 != 0:
#         return False
#     return flag
#
#
# password = '11111:71:90000'.split(':')
# print(is_valid_password(password))

# def is_correct_bracket(text):
#     count = 0
#     for i in range(len(text)):
#         if text[i] == '(':
#             count += 1
#         elif text[i] == ')':
#             count -= 1
#             if count < 0:
#                 return False
#     if count == 0:
#         return True
#     elif count > 0:
#         return False
#
# text = '(((('
# print(is_correct_bracket(text))


# def convert_to_python_case(text):
#     mylist = []
#     for i in range(len(text)):
#         if text[i] == text[i].lower():
#             mylist.append(text[i])
#         elif text[i] == text[i].upper():
#             mylist.append('_')
#             mylist.append(text[i].lower())
#     if mylist[0] == '_':
#         del mylist[0]
#     return ''.join(mylist)
#
#
# text = 'ThisIsCamelCased'
# print(convert_to_python_case(text))

# def convert_to_python_case(text):
#     string = ''
#     for i in text:
#         if i.isupper():
#             string += '_'
#         string += i.lower()
#     return string[1:]
#
#
# text = 'ThisIsCamelCased'
# print(convert_to_python_case(text))

