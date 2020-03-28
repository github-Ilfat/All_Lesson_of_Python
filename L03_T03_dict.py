# Тема 3. Тип данных СЛОВРИ (dict)------------------------
# -------------------------------------------------
print('---------------------------------------Тема 3. Тип данных СЛОВРИ (dict)---------------------------------------')
print('--------------------------------------------------------------------------------------------------------------')
print('')
# Раздел. Инициализация словаря
print('Раздел. Инициализация словаря.')
print('')
# 1 Вариант инициализации - фигурные скобки {}: name_dict = {}
print('----------------------------------------------Описание:-------------------------------------------------------')
print('1 Вариант инициализации - фигурные скобки {}:')
print('dict_temp = {}')
print('вывод на экран типа данных словаря и его содержимого:')
print('--------------------------------------------Python Script:----------------------------------------------------')
print('print(type(dict_temp), dict_temp)')
print('----------------------------------------------Результат:------------------------------------------------------')
dict_temp = {}
# вывод на экран типа данных словаря и его содержимого
print(type(dict_temp), dict_temp)
print('**************************************************************************************************************')
print('')
# наполненный словарь для практики:
print('----------------------------------------------Описание:-------------------------------------------------------')
print('наполненный словарь для практики:')
print('dict_temp = {\'dict1\': 1, \'dict2\': 2.1, \'dict3\': \'name\', \'dict4\':[1,2,3]}')
print('вывод на экран типа данных словаря и его содержимого:')
print('--------------------------------------------Python Script:----------------------------------------------------')
print('print(type(dict_temp), dict_temp)')
print('----------------------------------------------Результат:------------------------------------------------------')
dict_temp = {'dict1': 1, 'dict2': 2.1, 'dict3': 'name', 'dict4': [1, 2, 3]}
# вывод на экран типа данных словаря и его содержимого
print(type(dict_temp), dict_temp)
print('**************************************************************************************************************')
print('')
# 2 Вариант инициализации по ключам словаря fromkeys
print('----------------------------------------------Описание:-------------------------------------------------------')
print('2 Вариант инициализации по ключам словаря fromkeys:')
print('dict_temp = dict.fromkeys([\'a\', \'b\'], [12,\'2020\'])')
print('вывод на экран типа данных словаря и его содержимого:')
print('--------------------------------------------Python Script:----------------------------------------------------')
print('print(type(dict_temp), dict_temp)')
print('----------------------------------------------Результат:------------------------------------------------------')
dict_temp = dict.fromkeys(['a', 'b'], [12, '2020'])
print(type(dict_temp), dict_temp)
print('**************************************************************************************************************')
print('')
# 3 Вариант инициализации словаря - по команде dict:  name_dict = dict('keys1' = 'value1','keys2' = 'value2')
print('----------------------------------------------Описание:-------------------------------------------------------')
print('3 Вариант инициализации словаря - по команде dict:')
print('dict_temp = dict(brend = \'volvo\', volume_engine = 1.5)')
print('вывод на экран типа данных словаря и его содержимого:')
print('--------------------------------------------Python Script:----------------------------------------------------')
print('print(type(dict_temp), dict_temp)')
print('----------------------------------------------Результат:------------------------------------------------------')
dict_temp = dict(brend='volvo', volume_engine=1.5)
print(type(dict_temp), dict_temp)
print('**************************************************************************************************************')
print('')
# 4 Вариант инициализации словаря с авто заполнением по генерации значений:  name_dict = {a: a**2 for a in range(10)}
# в качестве имён ключей записывается цифра индекса от 0 до ...
print('----------------------------------------------Описание:-------------------------------------------------------')
print('4 Вариант инициализации словаря с авто заполнением по генерации значений,')
print('в качестве имён ключей записывается цифра индекса от 0 до ...:')
print('dict_temp = {a: a**2 for a in range(10)}')
print('вывод на экран типа данных словаря и его содержимого:')
print('--------------------------------------------Python Script:----------------------------------------------------')
print('print(type(dict_temp), dict_temp)')
print('----------------------------------------------Результат:------------------------------------------------------')
dict_temp = {a: a ** 2 for a in range(10)}
print(type(dict_temp), dict_temp)
print('**************************************************************************************************************')
print('')
# Раздел. Обращения к содержимому словаря
print('Раздел. Обращения к содержимому словаря.')
print('')
# Способ обращения по имени ключа (здесь 8 - это имя совпадающее с индексом, т.к. словарь взят из примера выше)
print('----------------------------------------------Описание:-------------------------------------------------------')
print('Способ обращения по имени ключа,')
print('здесь \'8\' - это имя совпадающее с индексом, т.к. словарь взят из примера выше:')
print('словарь - "dict_temp"')
print(type(dict_temp), dict_temp)
print('вывод на экран содержимого словаря по ключу \'8\':')
print('--------------------------------------------Python Script:----------------------------------------------------')
print('print(dict_temp[8])')
print('----------------------------------------------Результат:------------------------------------------------------')
print(dict_temp[8])
print('**************************************************************************************************************')
print('')
# Раздел. Функции со словарями
print('')
print('Раздел. Функции со словарями.')
print('')
# Возврат всех ключей словаря
print('----------------------------------------------Описание:-------------------------------------------------------')
print('вывод на экран только всех ключей словаря:')
print('словарь - "dict_temp"')
print(type(dict_temp), dict_temp)
print('--------------------------------------------Python Script:----------------------------------------------------')
print('print(list(dict_temp.keys()))')
print('----------------------------------------------Результат:------------------------------------------------------')
print(list(dict_temp.keys()))
print('**************************************************************************************************************')
print('')
# Возврат всех значений словаря
print('----------------------------------------------Описание:-------------------------------------------------------')
print('вывод на экран только всех значений словаря:')
print('словарь - "dict_temp"')
print(type(dict_temp), dict_temp)
print('--------------------------------------------Python Script:----------------------------------------------------')
print('print(list(dict_temp.values()))')
print('----------------------------------------------Результат:------------------------------------------------------')
print(list(dict_temp.values()))
print('**************************************************************************************************************')
print('')
# Возврат и всез ключей и всех значений словаря (возврат кортежей)
print('----------------------------------------------Описание:-------------------------------------------------------')
print('Возврат и всех ключей и всех значений словаря (возврат кортежей):')
print('словарь - "dict_temp"')
print(type(dict_temp), dict_temp)
print('--------------------------------------------Python Script:----------------------------------------------------')
print('print(list(dict_temp.items()))')
print('----------------------------------------------Результат:------------------------------------------------------')
print(list(dict_temp.items()))
print('**************************************************************************************************************')
print('')
# Раздел. Работа с элементами
print('')
print('Раздел. Работа с элементами.')
print('')
print('----------------------------------------------Описание:-------------------------------------------------------')
print('Изменение значения словаря по ключу:')
print('словарь - "dict_temp"')
print(type(dict_temp), dict_temp)
print('--------------------------------------------Python Script:----------------------------------------------------')
print('dict_temp[0] = 100')
print('print(type(dict_temp), dict_temp)')
print('----------------------------------------------Результат:------------------------------------------------------')
dict_temp[0] = 100
print(type(dict_temp), dict_temp)
print('**************************************************************************************************************')
print('')
print('----------------------------------------------Описание:-------------------------------------------------------')
print('Добавление нового ключа и значения в словарь:')
print('словарь - "dict_temp"')
print(type(dict_temp), dict_temp)
print('--------------------------------------------Python Script:----------------------------------------------------')
print('dict_temp[\'name\'] = \'Dima\'')
print('print(type(dict_temp), dict_temp)')
print('----------------------------------------------Результат:------------------------------------------------------')
dict_temp['name'] = 'Dima'
print(type(dict_temp), dict_temp)
print('**************************************************************************************************************')
print('')
# Раздел. Методы
# keys, values, items см выше
print('Раздел. Методы.')
print('')
#Удаление значения по ключу в словаре, метод - pop
print('----------------------------------------------Описание:-------------------------------------------------------')
print('Удаление значения по ключу в словаре, метод - pop')
print('словарь - "dict_temp"')
print(type(dict_temp), dict_temp)
print('--------------------------------------------Python Script:----------------------------------------------------')
print('dict_temp.pop(\'name\')')
print('print(type(dict_temp), dict_temp)')
print('----------------------------------------------Результат:------------------------------------------------------')
dict_temp.pop('name')
print(type(dict_temp), dict_temp)
print('**************************************************************************************************************')
print('')
#Одновременное удаление и возврат удалённого значения из словаря, метод - pop
print('----------------------------------------------Описание:-------------------------------------------------------')
print('Одновременное удаление и возврат удалённого значения из словаря, метод - pop')
print('словарь - "dict_temp"')
print(type(dict_temp), dict_temp)
print('--------------------------------------------Python Script:----------------------------------------------------')
print('print(\'удалено значение -\', dict_temp.pop(\'9\'))')
print('print(type(dict_temp), dict_temp)')
print('----------------------------------------------Результат:------------------------------------------------------')
print('удалено значение -', dict_temp.pop(9))
print(type(dict_temp), dict_temp)
print('**************************************************************************************************************')
print('')
# Раздел. Итерирование по словарю
print('')
print('Раздел. Итерирование по словарю.')
print('')
print('----------------------------------------------Описание:-------------------------------------------------------')
#1 Итерирование(проходить) по словарю, обращаясь к паре в списке (вариант 1)
print('1 Итерирование(проходить) по словарю, обращаясь к паре в списке (вариант 1)')
print('словарь - "dict_temp"')
print(type(dict_temp), dict_temp)
print('--------------------------------------------Python Script:----------------------------------------------------')
print('for pair in dict_temp.items():')
print('print(pair)')
print('----------------------------------------------Результат:------------------------------------------------------')
for pair in dict_temp.items():
    print(pair)
print('**************************************************************************************************************')
print('')
#1 Итерирование(проходить) по словарю, обращаясь к паре в списке (вариант 2)
print('----------------------------------------------Описание:-------------------------------------------------------')
print('1 Итерирование(проходить) по словарю, обращаясь к паре в списке (вариант 2)')
print('словарь - "dict_temp"')
print(type(dict_temp), dict_temp)
print('--------------------------------------------Python Script:----------------------------------------------------')
print('for pair in dict_temp.items():')
print('print(key, value)')
print('----------------------------------------------Результат:------------------------------------------------------')
for key, value in dict_temp.items():
    print(key, value)
print('**************************************************************************************************************')
print('')
#2 Итерирование(проходить) по словарю, обращаясь к ключу
print('----------------------------------------------Описание:-------------------------------------------------------')
print('2 Итерирование(проходить) по словарю, обращаясь к ключу')
print('словарь - "dict_temp"')
print(type(dict_temp), dict_temp)
print('--------------------------------------------Python Script:----------------------------------------------------')
print('for key in dict_temp.keys():')
print('print(key)')
print('----------------------------------------------Результат:------------------------------------------------------')
for key in dict_temp.keys():
    print(key)
print('**************************************************************************************************************')
print('')
#3 Итерирование(проходить) по словарю, обращаясь к значению
print('----------------------------------------------Описание:-------------------------------------------------------')
print('3 Итерирование(проходить) по словарю, обращаясь к значению')
print('словарь - "dict_temp"')
print(type(dict_temp), dict_temp)
print('--------------------------------------------Python Script:----------------------------------------------------')
print('for value in dict_temp.values():')
print('print(value)')
print('----------------------------------------------Результат:------------------------------------------------------')
for value in dict_temp.values():
    print(value)
print('**************************************************************************************************************')