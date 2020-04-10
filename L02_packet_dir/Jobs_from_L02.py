#Задачи на циклы и оператор условия------
#----------------------------------------

'''
*******************************************************************************************
Задача 1
Вывести на экран циклом пять строк из нулей, причем каждая строка должна быть пронумерована.
'''
'''
print('Задача 1. Данный скрипт выводит на экран циклом пять пронумерованных строк из нулей.')
for i in range(1,6,1): print(i,') ', 0, sep='')
'''

'''
*******************************************************************************************
Задача 2
Пользователь в цикле вводит 10 цифр. Найти количество введеных пользователем цифр 5.
'''
'''
def is_digit(string):
    flag_ok = 0
    if string.isdigit():
        if len(string)==1 and (int(string) >=0 and int(string) <= 10): return True
    else:
        return False
five = 0
err = 0
i = 0
print('Задача 2. Данный скрипт подсчитывает количество цифр 5, введённых пользователем в цикле 10 цифр.')
print('Прошу 10 раз, поочерёдно ввести любую цифру от 0 до 9.')
while i < 10:
    i = i + 1 - err
    print('введите цифру N', i, sep = '', end = ' ')
    user_digital = input(':')
    if is_digit(user_digital):
        user_digital = int(user_digital)
        if user_digital == 5: five = five + 1
        if i == 10: print('Ответ, количество цифр 5, введённых пользователем в цикле 10 цифр =', five)
        err = 0
    else:
        err = 1
        print('Это не цифра алфавита десятичной системы счисления!')
    continue
'''

'''
*******************************************************************************************
Задача 3
Найти сумму ряда чисел от 1 до 100. Полученный результат вывести на экран.
'''
'''
print('Задача 3. Данный скрипт подсчитывает сумму ряда чисел от 1 до 100 и выводит результат на экран.')
sum = 0
for i in range(1,101): sum += i
print('Ответ, сумма ряда чисел от 1 до 100 =', sum)
'''

'''
*******************************************************************************************
Задача 4
Найти произведение ряда чисел от 1 до 10. Полученный результат вывести на экран.
'''
'''
print('Задача 4. Данный скрипт подсчитывает произведение ряда чисел от 1 до 10 и выводит результат на экран.')
proizv = 1
for i in range(1,11): proizv = proizv * i
print('Ответ, произведение ряда чисел от 1 до 10 =', proizv)
'''

'''
*******************************************************************************************
Задача 5
Вывести цифры числа на каждой строчке.
'''
'''
print('Задача 5a. Данный скрипт выводит цифры числа на каждой строчке начиная справа-налево.')
integer_number = 2129
print('Число для вывода его цифр на каждой строчке начиная справа-налево:', integer_number)
while integer_number > 0:
    print(integer_number % 10)
    integer_number = integer_number // 10
'''
'''
print('Задача 5b. Данный скрипт выводит цифры числа на каждой строчке начиная слева-направо.')
integer_number = 2129
print('Число для вывода его цифр на каждой строчке начиная слева-направо:', integer_number)
k = 10**(len(str(integer_number))-1)
ostatok_number=integer_number
while ostatok_number > 0:
    cifra_number=int(ostatok_number//k)
    ostatok_number=ostatok_number%k
    k = k / 10
    print(cifra_number)
'''

'''
*******************************************************************************************
Задача 6
Найти сумму цифр числа.
'''
'''
print('Задача 6. Данный скрипт определяет сумму цифр числа.')
integer_number = 2129
print('Исследуемое число:', integer_number)
print('Ответ, сумма цифр числа равна:')
k = 10**(len(str(integer_number))-1)
sum = 0
ostatok_number=integer_number
while ostatok_number > 0:
    cifra_number = int(ostatok_number // k)
    if ostatok_number > 10: print(cifra_number, end = ' + ')
    if ostatok_number < 10: print(cifra_number, end = ' = ')
    sum = sum + int(cifra_number)
    ostatok_number = ostatok_number % k
    k = k / 10
    if ostatok_number == 0: print(sum)
'''

'''
*******************************************************************************************
Задача 7
Найти произведение цифр числа.
'''
'''
print('Задача 7. Данный скрипт определяет произведение цифр числа.')
integer_number = 2129
print('Исследуемое число:', integer_number)
print('Ответ, произведение цифр числа равна:')
k = 10**(len(str(integer_number))-1)
sum = 1
ostatok_number=integer_number
while ostatok_number > 0:
    cifra_number = int(ostatok_number // k)
    if ostatok_number > 10: print(cifra_number, end = ' * ')
    if ostatok_number < 10: print(cifra_number, end = ' = ')
    sum = sum * int(cifra_number)
    ostatok_number = ostatok_number % k
    k = k / 10
    if ostatok_number == 0: print(sum)
'''

'''
*******************************************************************************************
Задача 8
Дать ответ на вопрос: есть ли среди цифр числа 5?
'''
'''
print('Задача 8. Данный скрипт определяет: есть ли среди цифр числа 5.')
integer_number = 213413
print('Исследуемое число:', integer_number)
while integer_number>0:
    if integer_number%10 == 5:
        print('Ответ, среди цифр число 5 - есть')
        break
    integer_number = integer_number//10
else: print('Ответ, среди цифр числа 5 - нет')
'''

'''
*******************************************************************************************
Задача 9
Найти максимальную цифру в числе
'''
'''
print('Задача 9. Данный скрипт определяет: максимальную цифру в числе.')
integer_number = 213413
print('исследуемое число: ', integer_number)
max = 0
while integer_number>0:
    if integer_number%10 > max: max = integer_number%10
    integer_number = integer_number//10
    if integer_number == 0:  print('Ответ, максимальная цифра в числе = ', max)
'''

'''
*******************************************************************************************
Задача 10
Найти количество цифр 5 в числе
'''
'''
print('Задача 10. Данный скрипт определяет количество цифр 5 в числе.')
integer_number = 2535154345
print('исследуемое число: ', integer_number)
n5=0
while integer_number>0:
    if integer_number%10 == 5: n5+=1
    integer_number = integer_number//10
    if integer_number == 0:  print('Ответ, количество цифр 5 в числе = ', n5)
'''