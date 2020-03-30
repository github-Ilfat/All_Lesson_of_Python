# Полуавтоматические тесты ("наивные тесты")

def test_function(list_in):
    '''
    вход: list
    выход: list, содержащий только числа из list
    :return:
    '''
    list_temp = []
    for i in range(len(list_in)):
        if type(list_in[i]) == int:
            list_temp.append(list_in[i])
        elif type(list_in[i]) == str:
            if list_in[i].isdigit(): list_temp.append(int(list_in[i]))
    return list_temp
# list_temp = [1,2,3,'abc']
#
#
# print(test_function(list_temp))

def function_test():
    list_temp = [1, 2, 3, 'abc'] # [1,2,3]
    list_out = test_function(list_temp)
    if list_out == [1,2,3]:
        print('Test 1 is OK')
    else:
        print('Test 1 is failed!')

    list_temp = [1, 2, 3, 'abc', 4] # [1,2,3,4]
    list_out = test_function(list_temp)
    if list_out == [1,2,3,4]:
        print('Test 2 is OK')
    else:
        print('Test 2 is failed!')

    list_temp = [1, 2, 3,'5','abc', 4] # [1,2,3,5,4]
    list_out = test_function(list_temp)
    if list_out == [1,2,3,5,4]:
        print('Test 3 is OK')
    else:
        print('Test 3 is failed!')
function_test()