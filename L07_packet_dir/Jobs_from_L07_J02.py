# Решение по пункту задания 4:
#
import csv
print('------------------------------------------------------------------------------------------------------------')
print('Блок чтения данных из текстового файла "Jobs_from_L07_data_text_file"')
print('для создания csv файла "Jobs_from_L07_data_csv_file" (конвертер "txt to csv").')
print('------------------------------------------------------------------------------------------------------------')

# 1  Страна        #   США      # ЛНР
# 2  (за сутки)    #   245373   # 1
# 3  Заражений     #   +4978
# 4  (%)           #   +3%
# 5  (за сутки)    #   6095     # 0
# 6  Смертей       #   +287
# 7  (%)           #   +5%
# 8  (за сутки)    #   10403    # 0
# 9  Выздоровлений #   +38
# 10 (%)           #   +1%
# 11 % Смертей     #   2.49%    # 0%

# 0 ln (сам текст), 1 first_sym, , 2 num (число в тексте), 3 tnum (тип числа), 4 end_sym
def position_volue_num(ln_txt):
    ln=ln_txt[0]
    lln=len(ln)
    first_sym=ln_txt[1]
    end_sym=ln_txt[4]
    if lln>=1:
        if lln==1: end_sym=ln[0]
        if lln>1: end_sym=ln[-1]
        if lln>=1 and not ln.isdigit() and end_sym!='%':
            ln_txt[2] = 0 # num
            ln_txt[3] = 0 # tnum: ln=str
        if lln>=1 and ln.isdigit():
            ln_txt[2] = int(ln) # num
            ln_txt[3] = 1 # tnum: ln= 0...245373...
        if lln>1 and first_sym=='+' and end_sym.isdigit():
            ln_txt[2] = int(ln[1:]) # num
            ln_txt[3] = 2 # tnum: ln= +0...+4978...
        if lln>1 and first_sym=='+' and end_sym=='%':
            ln_txt[2] = int(ln[1:-1]) # num
            ln_txt[3] = 3 # tnum: ln= +0%...+100%
        if lln>1 and first_sym.isdigit() and end_sym=='%':
            ln_txt[2] = float(ln[:-1]) # num
            ln_txt[3] = 4 # tnum: ln= 1%...100%
    return ln_txt

# 0 ln (сам текст), 1 first_sym, , 2 num (число в тексте), 3 tnum (тип числа), 4 end_sym
ln_txt=['','',0,0,'']
clmn=0
begin_str=0
csv_line = ''
txt_list = []
#from_country='США'
from_country='Восточный Тимор'
with open('Jobs_from_L07_csv_file.csv', 'w') as str_to_fcsv:
    str_to_fcsv.write('Страна,Заражений,(за сутки),(%),Смертей,(за сутки),(%),Выздоровлений,(за сутки),(%),% Смертей,\n')
filename = "Jobs_from_L07_data_text_file"
with open(filename, encoding="utf8") as f:
    for line in f:
        ln_txt[0]=line[0:-1]
        ln_txt[1]=line[0]
        position_volue_num(ln_txt)
        ln=ln_txt[0]
        first_sym=ln_txt[1]
        num=ln_txt[2]
        tnum=ln_txt[3]
        end_sym=ln_txt[4]
        if tnum == 0 and ln==from_country: begin_str=1
        if (end_sym) == '%': begin_str=2
        if clmn==11: begin_str=3
        if begin_str > 0:
            clmn+=1
            if (clmn==3 and tnum==1) or (clmn==6 and tnum==1) or (clmn==9 and tnum==4):
                clmn+=2
                csv_line+=',,'
            if (clmn==3 and tnum!=2) or (clmn==4 and tnum!=3) \
                or (clmn==6 and tnum!=2) or (clmn==7 and tnum!=3) \
                or (clmn==9 and tnum!=2) or (clmn==10 and tnum!=3):
                clmn+=1
                if csv_line[-1]==',,':
                    csv_line+=',,'
                else:
                    csv_line+=','
            csv_line += ln + ','
            print(csv_line)
            if clmn==11:
                with open('Jobs_from_L07_csv_file.csv', 'a') as str_to_fcsv:
                    str_to_fcsv.write(csv_line + '\n')
                    csv_line=''
                    begin_str=2
                    clmn=0
print('------------------------------------------------------------------------------------------------------------')

'''
print('This is L06_branche_for_Job_L05_TEST01')

print('------------------------------------------------------------------------------------------------------------')
print('Блок проверки ввода значений из файл "L06_branche_for_Job_L05_TEST01_data",')
print('для тестирования модуля "Jobs_from_L05_divisor_master.py".')
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
    global ok,err
    ok=int(0)
    err=int(0)
    # только правильные значения ответов:
    #chk_list = [1,2,3,37,37,5,5,83,997,499,37,5]
    # для теста:
    chk_list = [1,5,3,37,37,5,7,82,997,499,37,5]
    for i in  range(len(int_arr_list)):
        num = int_arr_list[i]
        res_out = check_nuber(num)
        chk_num = chk_list[i]
        print('-------------------------------------------------------------------------------------------------------')
        print('результаты теста 1.',i,':', sep='')
        if res_out == chk_num:
            ok += 1
            print('- без ошибки, число :', num,'максимальный простой делитель =', chk_num)
        else:
            err += 1
            print(' - с ошибкой, число :', num,'максимальный простой делитель <>')
        print('-------------------------------------------------------------------------------------------------------')
function_test()

print('Общее количество тестируемых значений:',len(int_arr_list))
print('количество ошибок:', ok)
print('количество ошибок:', err)

'''