# fib_num = lambda n: fib_num(n-1)+ fib_num(n-2) if n > 2 else 1
#
#
# def test_1_fib_num():
#     assert fib_num(6) == 8
#
# def test_2_fib_num():
#     assert fib_num(5) == 8
#
# # f_{2n} = (f_{n+1})^2 - (f_{n-1})^2
# def test_3_fib_num():
#     n = 10
#     assert fib_num(2*n) == fib_num(n+1)**2 - fib_num(n-1)**2