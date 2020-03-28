global_var = 10

def function_example(local_var_1, local_var_2):
    print(local_var_1, local_var_2, global_var)

function_example(11, 12)


def function_example_1(local_var_1, local_var_2):
    global global_var
    global_var = 20
    print(local_var_1, local_var_2, global_var, id(global_var))


function_example_1(11, 12)
print(global_var, id(global_var))

# nonlocal

def counter():
    num = 0
    def plus_one():
        nonlocal num
        num+=1
        return num
    return plus_one

count = counter()

print(count)
print(count())
print(count())