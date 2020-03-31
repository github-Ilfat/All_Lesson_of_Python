# import L05_T02_my_math_module
#
# print(__name__)
# print(L05_T02_my_math_module.my_add(3,8))
#
# # (f_n)^2 + (f_{n+1})^2 = f_{2n+1}
#
# n = 10
#
# print(L05_T02_my_math_module.fib_num_l(n)**2 + L05_T02_my_math_module.fib_num_l(n+1)**2)
#
# print(L05_T02_my_math_module.fib_num_l(2*n+1))

# 1
# from packet import math_op
#
# print(math_op.my_add(1,2))

# 2
# from  packet.math_op import my_add
#
# print(my_add(1, 2))

# Используем __init__.py
# from packet import my_sub
#
# print(my_sub(1, 2))

import sys

print(sys.path)

list_temp = [1,2,3,1,2,3,9,8,7]
max = list_temp[0]
for i in range(len(list_temp)):
    if max < list_temp[i]:
        max = list_temp[i]
print(max)