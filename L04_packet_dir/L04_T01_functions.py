#Простейшая функция и описание
print('--------------------------------------Тема 1. Тип кода ФУНКЦИЯ------------------------------------------------')
print('--------------------------------------------------------------------------------------------------------------')
print('')
# Раздел. Тело функции - синтаксис
print('Раздел. Инициализация, тело функции, синтаксис')
print('----------------------------------------------Описание:-------------------------------------------------------')
print(' #начало ')
print('def add(x,y):')
print('    \'\'\'')
print(' #описание параметров')
print('    :param x:')
print(' #описание параметров')
print('    :param y:')
print('#конец')
print('    :return:')
print('    \'\'\'')
print(' #возврат результата')
print('    return x+y')
print('# просмотр описания функции')
print('help(add)')
print('# Вызов функции')
print('print(add(100,101))')
print('print(add(\'Dima\',\'+Kate\'))')
print('--------------------------------------------Python Script:----------------------------------------------------')
print('def add(x,y):')
print('    \'\'\'')
print('    :param x:')
print('    :param y:')
print('    :return:')
print('    \'\'\'')
print('    return x+y')
print('----------------------------------------------Результат:------------------------------------------------------')
def add(x,y):
    '''
    :param x:
    :param y:
    :return:
    '''
    return x+y
# просмотр описания функции
help(add)
# Вызов функции
print(add(100,101))
print(add('Dima','+Kate'))
print('**************************************************************************************************************')
print('')


# Функция возвращает функцию
def f1(n):
    def f2(m):
        return n+m
    return f2
new_f = f1(100)
print(type(new_f))
new_f = f1(100)
print(new_f(250))

#Даже без return функция вернет None
def f():
    pass

print(f())


#Аргументы функций-------------
#-------------------------------

# Обязательные аргументы и не обязательные
def add(x,y, z = 10):
    '''
    :param x:
    :param y:
    :return:
    '''
    return x+y+z

print(add(1,2))
print(add(1,2,3))


# args

def func(*args):
    print(type(args), args)
    return args

func(1,2,3,'Volvo')


# kwargs
def func(**kwargs):
    print(type(kwargs), kwargs)
    return kwargs

func(a = 1, b = 2, c = 'Volvo', d = 1.5)


# Все вместе
def func_difficult(x, y = 2, *args, **kwargs):
    print(type(x), x)
    print(type(y), y)
    print(type(args), args)
    print(type(kwargs), kwargs)
    return kwargs

func_difficult(1,3, (1,2,3), temp = 12, temp_1 = 13)