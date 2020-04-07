'''
LIGHT:
1. Написал декоратор, замеряющий время выполнение декорируемой функции.
2. Сравнил время создания генератора и списка с элементами:
    натуральные числа от 1 до 1000000 (созданные объекты оформил в виде функций).
PRO
Light +
3. Написал декоратор, замеряющий объем оперативной памяти, потребляемый декорируемой функцией.
4. Сравнил объем оперативной памяти для функции создания генератора и функции создания списка с элементами:
    натуральные числа от 1 до 1000000.

Презентация вебинара:
https://drive.google.com/open?id=1O9tBDTRJ3NnSljk7RAPRBQCiB_YB8iMC
Репозиторий GitHub:
https://github.com/MachineLearningIsEasy/python_lesson_8
'''


from datetime import datetime
import psutil
import os

def timer(func):
    #--------------------------------------
    def wapper(*args, **kwargs):
        begin_time = datetime.now()
        #--------------------------------------
        result = func(*args, **kwargs)
        #--------------------------------------
        end_time = datetime.now()
        print('#test_num:', test_num, f'Время отработки функции {func.__name__}: \
                {end_time-begin_time} (ЧЧ:ММ:СС.милисекунд)')
        return result
    #--------------------------------------
    return wapper

def memory_used(func):
    #--------------------------------------
    def wapper(*args, **kwargs):
        proc = psutil.Process(os.getpid())
        begin_memory_used = proc.memory_info().rss
        #--------------------------------------
        result = func(*args, **kwargs)
        #--------------------------------------
        end_memory_used = proc.memory_info().rss
        print('#test_num:', test_num, f'Объём памяти, используемой функцией {func.__name__}: \
                {end_memory_used-begin_memory_used} (в байтах)')
        return result
    #--------------------------------------
    return wapper

#Тест 1.1.:
#--------------------------------------------------------------------------------------------------------
@timer
@memory_used
def gen_lst_nat_timer_mem(num, test_num):
    for i in range(num):
        yield i
#--------------------------------------------------------------------------------------------------------

#Тест 1.2.:
#--------------------------------------------------------------------------------------------------------
@memory_used
@timer
def gen_lst_nat_mem_timer(num, test_num):
    for i in range(num):
        yield i
#--------------------------------------------------------------------------------------------------------

#Тест 2.1.:
#--------------------------------------------------------------------------------------------------------
@timer
@memory_used
def list_nat_timer_mem(num, test_num):
    result = []
    for i in range(num):
        result.append(i)
    return result
#--------------------------------------------------------------------------------------------------------

#Тест 2.2.:
#--------------------------------------------------------------------------------------------------------
@memory_used
@timer
def list_nat_mem_timer(num, test_num):
    result = []
    for i in range(num):
        result.append(i)
    return result
#--------------------------------------------------------------------------------------------------------

print('#Тест 1.1. @timer, @memory_used:')
print('#--------------------------------------------------------------------------------------------------------')
test_num = 1.1
gen_lst_nat_timer_mem(10000000, test_num)
print('#--------------------------------------------------------------------------------------------------------')
print('#Тест 1.2. @memory_used, @timer:')
print('#--------------------------------------------------------------------------------------------------------')
test_num = 1.2
gen_lst_nat_mem_timer(10000000, test_num)
print('#--------------------------------------------------------------------------------------------------------')

print('#Тест 2.1. @timer, @memory_used:')
print('#--------------------------------------------------------------------------------------------------------')
test_num = 2.1
list_nat_timer_mem(10000000, test_num)
print('#--------------------------------------------------------------------------------------------------------')
print('#Тест 2.2. @memory_used, @timer:')
print('#--------------------------------------------------------------------------------------------------------')
test_num = 2.2
list_nat_mem_timer(10000000, test_num)
print('#--------------------------------------------------------------------------------------------------------')

#Тест 1.1. @timer, @memory_used:
#--------------------------------------------------------------------------------------------------------
#test_num: 1.1 Объём памяти, используемой функцией gen_lst_nat_timer_mem: 0 (в байтах)
#test_num: 1.1 Время отработки функции wapper: 0:00:00 (ЧЧ:ММ:СС.милисекунд)
#--------------------------------------------------------------------------------------------------------
#Тест 1.2. @memory_used, @timer:
#--------------------------------------------------------------------------------------------------------
#test_num: 1.2 Время отработки функции gen_lst_nat_mem_timer: 0:00:00 (ЧЧ:ММ:СС.милисекунд)
#test_num: 1.2 Объём памяти, используемой функцией wapper: 4096 (в байтах)
#--------------------------------------------------------------------------------------------------------
#Тест 2.1. @timer, @memory_used:
#--------------------------------------------------------------------------------------------------------
#test_num: 2.1 Объём памяти, используемой функцией list_nat_timer_mem: 405987328 (в байтах)
#test_num: 2.1 Время отработки функции wapper: 0:00:02.486142 (ЧЧ:ММ:СС.милисекунд)
#--------------------------------------------------------------------------------------------------------
#Тест 2.2. @memory_used, @timer:
#--------------------------------------------------------------------------------------------------------
#test_num: 2.2 Время отработки функции list_nat_mem_timer: 0:00:02.320132 (ЧЧ:ММ:СС.милисекунд)
#test_num: 2.2 Объём памяти, используемой функцией wapper: 405774336 (в байтах)
#--------------------------------------------------------------------------------------------------------