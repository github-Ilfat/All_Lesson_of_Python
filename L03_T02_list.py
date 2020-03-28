# Тема 2. Тип данных СПИСОК (list)------------------------
# ------------------------------------------
print('--------------------------------------Тема 2. Тип данных СПИСОК (list)----------------------------------------')
print('--------------------------------------------------------------------------------------------------------------')
print('')
# Раздел. Базовые ПРАВИЛА по СПИСКАМ:
print('----------------------------------------------Правила:--------------------------------------------------------')
print('ЕСЛИ СПИСОК: List_test1 = [0,1,2,3,4,"F5"], элементы списка разделяются запятыми')
print('Элементами списка могут быть любые объекты, в том числе и сами листы')
print('Выборку из листа можно выполнить так: [x**2|for x in num|if x>0]')
print('Выборку из листа можно выполнить так: [Операция с найденными(x)| Переменная(x) и множиство|Условие выбора(x)]')
print('ТО АДРЕСАЦИЯ ОБЪЕКТОВ ЛИСТА ВЫГЛЯДИТ ТАК:')
print('--------------------------------')
print('[  0][  1][  2][  3][  4][ "F5"]')
print(' 0 :  1 :  2 :  3 :  4 :  5     ')
print('--------------------------------')
List_test1 = [0, 1, 2, 3, 4, "F5"]
print(type(List_test1), List_test1)
for x1 in range(6):
    x2 = 6 - x1
    sp1 = '   '
    sp2 = '  '
    if (x1 == 0 or x1 == 5): sp2 = ''
    if x1 == 5: sp1 = '  '
    if x1 == 5: sp2 = sp2 + '  '
    for i in range(6 - len(List_test1[0:x1])): sp2 = sp2 + "   "
    print('List_test1[', x1, '] =', List_test1[x1], sp1 + 'List_test1[', 0, ':', x1, '] =', List_test1[0:x1],
          sp2 + '  List_test1[', x2, ':', 6, '] =', List_test1[x2:6])
print('                       List_test1[ 0 : 6 ] =', List_test1[0:6], ' List_test1[ 0 : 6 ] =', List_test1[0:6])
print('**************************************************************************************************************')
print('')
# Раздел. Инициализация СПИСКА
print('Раздел. Инициализация СПИСКА,')
print('')
# 1 Инициализация СПИСКА квадратными скобками [] - пустой список
print('----------------------------------------------Описание:-------------------------------------------------------')
print('1 Инициализация СПИСКА квадратными скобками [] - пустой список')
print('--------------------------------------------Python Script:----------------------------------------------------')
print('пустой список : list_temp = []')
print('print(type(list_temp))')
print('----------------------------------------------Результат:------------------------------------------------------')
list_temp = []  # пустой список
print(type(list_temp), list_temp)
print('**************************************************************************************************************')
print('')
# 1 Инициализация СПИСКА квадратными скобками - не пустой список
print('----------------------------------------------Описание:-------------------------------------------------------')
print('1 Инициализация СПИСКА квадратными скобками - не пустой список')
print('Обращение и вывод значений и типа объектов СПИСКА.')
print('--------------------------------------------Python Script:----------------------------------------------------')
print('не пустой список: list_temp = [1.2, 123, \'Volvo\', [1,2,3]]')
print('for el in list_temp:')
print('print(el, type(el))')
print('----------------------------------------------Результат:------------------------------------------------------')
list_temp = [1.2, 123, 'Volvo', [1, 2, 3]]  # не пустой список
for el in list_temp:
    print(el, type(el))
print('**************************************************************************************************************')
print('')
# 2 Инициализация СПИСКА командой list
print('----------------------------------------------Описание:-------------------------------------------------------')
print('2 Инициализация СПИСКА командой list')
print('Обращение и вывод значений и типа объектов СПИСКА.')
print('--------------------------------------------Python Script:----------------------------------------------------')
print('list_str = list(\'Volvo\')')
print('print(list_str)')
print('----------------------------------------------Результат:------------------------------------------------------')
list_str = list('Volvo')
print(list_str)
print('**************************************************************************************************************')
print('')
# Обращения к элементам списка, подсписки
print('----------------------------------------------Описание:-------------------------------------------------------')
print('1 Вариант обращения к элементам списка')
print('--------------------------------------------Python Script:----------------------------------------------------')
print('for i in range(len(list_temp)):')
print('print(i, \':\', list_temp[i])')
print('----------------------------------------------Результат:------------------------------------------------------')
for i in range(len(list_temp)):
    print(i, ':', list_temp[i])
print('**************************************************************************************************************')
print('')

print('----------------------------------------------Описание:-------------------------------------------------------')
print('2 Вариант обращения к элементам списка')
print('--------------------------------------------Python Script:----------------------------------------------------')
print('for i in range(len(list_temp)):')
print('print(i, \':\', list_temp[i:])')
print('----------------------------------------------Результат:------------------------------------------------------')
for i in range(len(list_temp)):
    print(i, ':', list_temp[i:])
print('**************************************************************************************************************')
print('')

print('----------------------------------------------Описание:-------------------------------------------------------')
print('3 Вариант обращения к элементам списка')
print('--------------------------------------------Python Script:----------------------------------------------------')
print('for i in range(len(list_temp)):')
print('print(i, \':\', list_temp[:i])')
print('----------------------------------------------Результат:------------------------------------------------------')
for i in range(len(list_temp)):
    print(i, ':', list_temp[:i])
print('**************************************************************************************************************')
print('')
# Функции со списками
print('----------------------------------------------Описание:-------------------------------------------------------')
print('Определение и вывод длины списка на экран')
print('--------------------------------------------Python Script:----------------------------------------------------')
print('print(len(list_temp))')
print('----------------------------------------------Результат:------------------------------------------------------')
print(len(list_temp))
print('**************************************************************************************************************')
print('')
# Операции со списками
print('----------------------------------------------Описание:-------------------------------------------------------')
print('Сложение списков и умножение на целое число')
print('--------------------------------------------Python Script:----------------------------------------------------')
print('print(list_temp + list_str)')
print('print(list_temp*2)')
print('----------------------------------------------Результат:------------------------------------------------------')
print(list_temp + list_str)
print(list_temp * 2)
print('**************************************************************************************************************')
print('')
# Методы
print('---------------------------------------------Описание:-------------------------------------------------------')
print('аppend - дополнение в конец списка, с генерацией значений')
print('--------------------------------------------Python Script:----------------------------------------------------')
print('integer_list = []')
print('for i in range(5):')
print('    integer_list.append(i)')
print('print(integer_list)')
print('----------------------------------------------Результат:------------------------------------------------------')
integer_list = []
for i in range(5):
    integer_list.append(i)
print(integer_list)
print('**************************************************************************************************************')
print('')
print('----------------------------------------------Описание:-------------------------------------------------------')
print('аppend - дополнение в конец списка, одиночная константа')
print('--------------------------------------------Python Script:----------------------------------------------------')
print('integer_list.append(0)')
print('print(integer_list)')
print('----------------------------------------------Результат:------------------------------------------------------')
integer_list.append(0)
print(integer_list)
print('**************************************************************************************************************')
print('')
# remove
print('----------------------------------------------Описание:-------------------------------------------------------')
print('remove - одиночное удаление')
print('--------------------------------------------Python Script:----------------------------------------------------')
print('integer_list.remove(0)')
print('print(integer_list)')
print('----------------------------------------------Результат:------------------------------------------------------')
integer_list.remove(0)
print(integer_list)
print('**************************************************************************************************************')
print('')
# del
print('----------------------------------------------Описание:-------------------------------------------------------')
print('del - одиночное удаление')
print('--------------------------------------------Python Script:----------------------------------------------------')
print('del integer_list[4]')
print('print(integer_list)')
print('----------------------------------------------Результат:------------------------------------------------------')
del integer_list[4]
print(integer_list)
print('**************************************************************************************************************')
print('')
# reverse
print('----------------------------------------------Описание:-------------------------------------------------------')
print('reverse - реверс индексов по отношению к значениям списка')
print('--------------------------------------------Python Script:----------------------------------------------------')
print('integer_list.reverse()')
print('print(integer_list)')
print('----------------------------------------------Результат:------------------------------------------------------')
integer_list.reverse()
print(integer_list)
print('**************************************************************************************************************')
print('')
# sort
print('----------------------------------------------Описание:-------------------------------------------------------')
print('sort - сортировка списка по целочисленным значениям списка')
print('--------------------------------------------Python Script:----------------------------------------------------')
print('integer_list = [9,3,6,2,4]')
print('integer_list.sort()')
print('print(integer_list)')
print('----------------------------------------------Результат:------------------------------------------------------')
integer_list = [9, 3, 6, 2, 4]
integer_list.sort()
print(integer_list)
print('**************************************************************************************************************')
print('')
# insert
print('----------------------------------------------Описание:-------------------------------------------------------')
print('insert - вставка в список значений')
print('--------------------------------------------Python Script:----------------------------------------------------')
print('integer_list.insert(2, 100)')
print('print(integer_list)')
print('----------------------------------------------Результат:------------------------------------------------------')
integer_list.insert(2, 100)
print(integer_list)
print('**************************************************************************************************************')
print('')
# Раздел. Обработка списков (map, filter, reduce)
print('')
# map
# map(function, list) ----> map -----> list(map)
# new_integer_list = list(map(str, integer_list))
print('----------------------------------------------Описание:-------------------------------------------------------')
print('map -------------------------------------------')
print('map(function, list) ----> map -----> list(map)')
print('new_integer_list = list(map(str, integer_list))')
print('--------------------------------------------Python Script:----------------------------------------------------')
print('integer_list = [9,3,6,2,4]')
print('new_integer_list = list(map(lambda x: x**2, integer_list))')
print('print(new_integer_list)')
print('----------------------------------------------Результат:------------------------------------------------------')
integer_list = [9, 3, 6, 2, 4]
new_integer_list = list(map(lambda x: x ** 2, integer_list))
print(new_integer_list)
print('**************************************************************************************************************')
print('')
# filter
print('----------------------------------------------Описание:-------------------------------------------------------')
print('filter - фильтрация списка')
print('--------------------------------------------Python Script:----------------------------------------------------')
print('integer_list = [9,3,6,2,4]')
print('new_integer_list = list(filter(lambda x: x<5, integer_list))')
print('print(new_integer_list)')
print('----------------------------------------------Результат:------------------------------------------------------')
integer_list = [9, 3, 6, 2, 4]
new_integer_list = list(filter(lambda x: x < 5, integer_list))
print(new_integer_list)
print('**************************************************************************************************************')
print('')
# reduce
print('----------------------------------------------Описание:-------------------------------------------------------')
print('filter - фильтрация списка')
print('--------------------------------------------Python Script:----------------------------------------------------')
print('from functools import reduce')
print('integer_list = [1,2,3,4]')
print('sum = reduce(lambda x,y: x+y, integer_list)')
print('product = reduce(lambda x,y: x*y, integer_list)')
print('print(sum, product)')
print('----------------------------------------------Результат:------------------------------------------------------')
from functools import reduce
integer_list = [1, 2, 3, 4]
sum = reduce(lambda x, y: x + y, integer_list)
product = reduce(lambda x, y: x * y, integer_list)
print(sum, product)
print('**************************************************************************************************************')
print('')