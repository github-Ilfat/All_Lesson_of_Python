print('This is L06_branche_for_Job_L05_TEST01')

print('------------------------------------------------------------------------------------------------------------')
print('Блок проверки ввода значений из файл "L06_branche_for_Job_L05_TEST01_data",')
print('для тестирования модуля "Jobs_from_L05_divisor_master.py",')
f = open('L06_branche_for_Job_L05_TEST01_data')
int_arr_list = []
err_set=0
try:
    for line in f:
        if 0 < (int(line)) and (int(line)) < 1001:
            int_arr_list.append(int(line))
        else:
            int_arr_list = []
            int_arr_list.append(int(line))
            err_set=1
            break
except ValueError:
    int_arr_list = []
    int_arr_list.append(line)
    print('обнаружена ошибка ввода данных, не число:')
else:
    if err_set==0:
        print('ввод данных прошёл успешно, значения можно передать в функцию "check_nuber(num)",')
        print('для тестирования модуля "Jobs_from_L05_divisor_master.py" !')
    else:
        print('обнаружено число за пределами диапазона [1:1000], необходимо исправить:')
finally: f.close()

print(int_arr_list)
print('блок проверки ввода значений для тестирования модуля "Jobs_from_L05_divisor_master.py" завершён')
print('------------------------------------------------------------------------------------------------------------')
print('------------------------------------------------------------------------------------------------------------')
print('Блок тестирования модуля "Jobs_from_L05_divisor_master.py"')
print('полуавтоматический "наивный" тест:')

from L05_packet_dir.Jobs_from_L05_divisor_master import check_nuber

def function_test():
    chk_list = [1,2,3,37,37,5,5,83,997,499,37,5]
    for i in  range(len(int_arr_list)):
        num = int_arr_list[i]
        res_out = check_nuber(num)
        chk_num = chk_list[i]
        print('-------------------------------------------------------------------------------------------------------')
        print('результаты теста 1.',i,':', sep='')
        if res_out == chk_num: print('- без ошибки, число :', num,'максимальный простой делитель =', chk_num)
        else: print(' - с ошибкой, число :', num,'максимальный простой делитель <>')
        print('-------------------------------------------------------------------------------------------------------')
function_test()