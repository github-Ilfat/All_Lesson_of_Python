# factorial

def fact(num):
    if num == 0:
        return 1
    else:
        return num*fact(num-1)

print(fact(10))

factorial = 1
for i in range(1,11):
    factorial*=i # +=
print(factorial)

# a^b

def degree(a,b):
    if b == 0:
        return 1
    else:
        return a* degree(a,b-1)

print(degree(2,10))

deg = 1
for i in range(1,11):  # b = 10+1 = 11
    deg*=2 # a
print(deg)