fib_num_l = lambda n: fib_num_l(n-1)+ fib_num_l(n-2) if n > 2 else 1

def power(a,b):
    return a**b