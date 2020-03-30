# try:
#     исполяем какой-то код
# except Exception as e:
#     обработка исключения
# else:
#     код, который будет исполнен в случае, когда не возникает исключения
# finally:
#     код, который гарантированно будет исполнен последним (всегда исполняется)
# try:
#     a = int(input('Введите первое число'))
#     b = int(input('Введите второе число'))
#
#     print(a/b)
# except ZeroDivisionError as e:
#     print('Так нельзя: ', e)
# else:
#     print('Все хорошо!')
# finally:
#     print('Это было не просто!')
#

f = open('data')
int_arr_list = []
try:
    for line in f:
        int_arr_list.append(int(line))
except ValueError:
    print('Я нашел не число!')
else: print('Все прошло хорошо!')
finally: f.close()

print(int_arr_list)