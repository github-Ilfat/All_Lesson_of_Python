# 1) проверка числа на простоту (простые числа - это те числа у которых делители единица и они сами);
#if __name__ == '__lesson_5':

def is_prime(n):
    i = 2
    while n > i:
        if n % i == 0:
            break
        i += 1
    return i == n
print(is_prime(1000))

# 2) выводит список всех делителей числа;
def all_dividers(n):
    result = []
    i = 2
    while i * i <= n:
        if n % i == 0:
            n //= i
            result.append(i)
        else:
            i += 1
    if  n > 1:
        result.append(n)
    return result
print(all_dividers(1000))

# 3) выводит самый большой простой делитель числа.
def greatest_pr_div(n):
    prime_num = all_dividers(n)
    max_num = 0
    for i in prime_num:
        if i > max_num:
            max_num = i
    return(max_num)
print(greatest_pr_div(1000))