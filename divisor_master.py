# 1 Взаимствованная функция - генератор простых чисел (числа делящиеся на 1 и само на себя) в множестве от 1 до 1000,
# из статьи: "Алгоритм нахождения простых чисел" https://habr.com/ru/post/122538/
# Листинг 7
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
print(type(lst_prime_num), lst_prime_num)

# 2 Взаимствованная функция - генератор простых чисел (числа делящиеся на 1 и само на себя) в множестве от 1 до 1000,
# https://github.com/windn19/neuraluniversity/blob/master/Lessen5/divisor_master.py
def prime_numbers():
    # Присвоение исследуемого множиства чисел (1 до 1000) переменной set_prime_num
    set_prime_num = set(range(1, 1001))
    for i in range(2, 101):
        if i in set_prime_num:
            # Вычитание из исследуемого множиства "сложных чисел" с целью приведения к множиству "простых чисел"
            set_prime_num -= set(range(2 * i, 1001, i))
    return set_prime_num
print(type(prime_numbers()),prime_numbers())

'''
def is_prime_num(num):
    global set_prime_num
    if not set_prime_num:
        set_prime_num = prime_numbers()
    return num in set_prime_num


def dividers_num(num):
    result = []
    for i in range(1, num // 2 + 1):
        if num % i == 0:
            result.append(i)
    print(result)
    return result+[num]


def prepare_prime_set(num):
    global PRIME_SET
    if not PRIME_SET:
        PRIME_SET = prime_numbers()
    prime_list = sorted(list(PRIME_SET))
    prime_list = [i for i in prime_list if i <= num]
    return prime_list


def biggest_simple_divider(num):
    prime_list = prepare_prime_set(num)
    for i in reversed(prime_list):
        if num % i == 0:
            return i


def list_simple_divider(num):
    prime_list = prepare_prime_set(num)
    result = []
    for i in reversed(prime_list):
        while num % i == 0:
            num //= i
            result.append(i)
        if num == 1:
            break
    return result


def max_divider(num):
    result = dividers_num(num)
    return result[-2]

'''
PRIME_SET = set()
# print(biggest_simple_divider(1335))
# listt = list_simple_divider(609840)
# print(*[f'{i}^{listt.count(i)}' if listt.count(i) > 1 else i for i in set(listt)], sep=', ')
# print(max_divider(144))
# 2	3	5	7	11	13	17	19	23	29	31	37
# 41	43	47	53	59	61	67	71	73	79	83	89
# 97