# LIGHT:
# Необходимо реализовать модуль divisor_master.
# Все функции модуля принимают на вход натуральные числа от 1 до 1000. Модуль содержит функции:
# ******************************************************************************************************************
def check_nuber(num):
    #-----------------------------------------------------------------------------------------------------------------
    # Блок:
    # 1) проверка числа на простоту (простые числа - это те числа у которых делители единица и они сами);
    lst_numbers=[2]
    lst_prime_num=[1, 2]
    for i in range(3, 1000, 2):
        if (i>10) and (i%10==5): continue
        for j in lst_numbers:
            if j*j-1>i:
                lst_numbers.append(i)
                lst_prime_num.append(i)
                break
            if (i%j == 0): break
        else:
            lst_numbers.append(i)
            lst_prime_num.append(i)
    if num in (set(lst_prime_num)): print("Исследуемое число простое :", num)
    else: print("Исследуемое число не простое :", num)
    #-----------------------------------------------------------------------------------------------------------------
    # Блок:
    # 2) выводит список всех делителей числа;
    list_all_dividers_numb = []
    for i in range(1, num+1):
        if num % i == 0:
            list_all_dividers_numb.append(i)
    print("Cписок всех делителей исследуемого числа -", num, ", без разбора на простые:")
    print(list_all_dividers_numb)
    print("Количество делителей =", len(list_all_dividers_numb))
    #-----------------------------------------------------------------------------------------------------------------
    # вспомагательный подблок определяет множество простых чисел, каждое из которых меньше чем исследуемое число
    dividers_num = []
    lst_simple_dividers_num = []
    n=0
    while n<=(len(lst_prime_num)+1):
        if lst_prime_num[n] <= num and (num < lst_prime_num[n+1] or (num > 996 and n >= 150)):
            if num==1 or lst_prime_num[n] < num: dividers_num.append(lst_prime_num[n])
            n=(len(lst_prime_num)+1)
        else:
            dividers_num.append(lst_prime_num[n])
            lst_simple_dividers_num = dividers_num
        n+=1
    print("Cписок простых чисел, меньших исследуемого числа -", num, ":")
    print(dividers_num)
    print("Количество простых чисел для определения максимального делителя =", len(dividers_num))
    #-----------------------------------------------------------------------------------------------------------------
    # Блок:
    # 3) выводит самый большой простой делитель числа.
    if num>1:
        ad = len(list_all_dividers_numb)
        list_all_dividers_numb=(list_all_dividers_numb)
        asd = len(lst_simple_dividers_num)
        #print(type(lst_simple_dividers_num),lst_simple_dividers_num)
        for i in range(ad):
            ad_num=list_all_dividers_numb[i]
            #print(ad_num)
            for j in range(asd):
                asd_num=lst_simple_dividers_num[j]
                if ad_num > asd_num: j = 1
                if ad_num==asd_num:
                    if ad_num==1: result=num
                    else: result=ad_num
                    break
        #print("Максимальный простой делитель исследуемого числа =", result)
    else: result=1
        #-----------------------------------------------------------------------------------------------------------------
    return result

# Исследуемое число:
num = 997
print("Максимальный простой делитель исследуемого числа =", check_nuber(num))
