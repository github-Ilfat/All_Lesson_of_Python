'''
LIGHT:
1) Вручную создал текстовый файл "Jobs_from_L07_data_text_file" с данными по
CORONAVIRUS (COVID-19) from (https://coronavirus-monitor.ru/)
Мировая статистика случаев заражения коронавирусом на 03.04.2020
2) Создал doc шаблон "Jobs_from_L07_format_doc_report.docx", где использовал данные параметры.
3) Автоматически генерируется отчет CORONAVIRUS (COVID-19) в формате doc (как в видео 7.2).
4) Создал csv файл с данными CORONAVIRUS (COVID-19).
5) Создал json файл с данными CORONAVIRUS (COVID-19).
'''

print('------------------------------------------------------------------------------------------------------------')
# Решение по пункту задания 1,2,3:
# данные в файле: "Jobs_from_L07_data_text_file"
# шаблон в файле: "Jobs_from_L07_format_doc_report.docx"
# с помощью кода python ниже, генерируется файл "CORONAVIRUS_2020-04-03_report.docx"

import datetime

# необходимые модули и функции для работы с doc
from docxtpl import DocxTemplate
from docxtpl import InlineImage
from docx.shared import Cm
from docxtpl import DocxTemplate, InlineImage

# get_context - возвращает словарь аргуменов
def get_context(name_of, discr, date_of, signature1, signature2, signature3):
    return {
        'name_of_info': name_of,
        'discription': discr,
        'date_of_info': date_of,
        'image1': signature1,
        'image2': signature2,
        'image3': signature3,
    }

# здесь происходит вставка в шаблон (signature - картинка)
def from_template(name_of, discr, date_of, template, signature1, signature2, signature3):
    template = DocxTemplate(template)
    # gets the context used to render the document
    context = get_context(name_of, discr, date_of, signature1, signature2, signature3)

    img_size = Cm(15)  # sets the size of the image
    image = InlineImage(template, signature1, img_size)
    context['Jobs_from_L07_image1'] = image  # adds the InlineImage object to the context

    img_size = Cm(15)  # sets the size of the image
    image = InlineImage(template, signature2, img_size)
    context['Jobs_from_L07_image2'] = image  # adds the InlineImage object to the context

    img_size = Cm(15)  # sets the size of the image
    image = InlineImage(template, signature3, img_size)
    context['Jobs_from_L07_image3'] = image  # adds the InlineImage object to the context

    template.render(context)

    # запись файла doc
    template.save(name_of + '_' + str(datetime.datetime.now().date()) + '_report.docx')

def generate_report(name_of, discr, date_of):
    template = 'Jobs_from_L07_format_doc_report.docx'
    signature1 = 'Jobs_from_L07_image1.PNG'
    signature2 = 'Jobs_from_L07_image2.PNG'
    signature3 = 'Jobs_from_L07_image3.PNG'
    document = from_template(name_of, discr, date_of, template, signature1, signature2, signature3)

# вспомагательная функция
def toFixed(numObj, digits=0):
    return f"{numObj:.{digits}f}"

generate_report('CORONAVIRUS', 'Мировая статистика случаев заражения коронавирусом', '03.04.2020')




print('------------------------------------------------------------------------------------------------------------')
# Решение по пункту задания 4:
#
import csv
print('------------------------------------------------------------------------------------------------------------')
print('Блок чтения данных из текстового файла "Jobs_from_L07_data_text_file"')
print('для создания csv файла "Jobs_from_L07_data_csv_file" (конвертер "txt to csv").')
print('------------------------------------------------------------------------------------------------------------')

# 1  Страна        #   США      # ЛНР
# 2  Заражений     #   245373   # 1
# 3  (за сутки)    #   +4978
# 4  (%)           #   +3%
# 5  Смертей       #   6095     # 0
# 6  (за сутки)    #   +287
# 7  (%)           #   +5%
# 8  Выздоровлений #   10403    # 0
# 9  (за сутки)    #   +38
# 10 (%)           #   +1%
# 11 % Смертей     #   2.49%    # 0%

# 0 ln (сам текст), 1 first_sym, , 2 num (число в тексте), 3 tnum (тип числа), 4 end_sym
def chk_type_num(ln_txt):
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
from_country='США'
#from_country='Восточный Тимор'

# Создание csv файла и запись наименований полей
with open('Jobs_from_L07_csv_file.csv', 'w') as str_to_fcsv:
    str_to_fcsv.write('Страна,Заражений,(за сутки),(%),Смертей,(за сутки),(%),Выздоровлений,(за сутки),(%),% Смертей,\n')
filename = "Jobs_from_L07_data_text_file"
with open(filename, encoding="utf8") as f:
    for line in f:
        ln_txt[0]=line[0:-1]
        ln_txt[1]=line[0]
        chk_type_num(ln_txt)
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
                # наполнение csv файла - запись статистики по странам
                with open('Jobs_from_L07_csv_file.csv', 'a') as str_to_fcsv:
                    str_to_fcsv.write(csv_line + '\n')
                    csv_line=''
                    begin_str=2
                    clmn=0
print('------------------------------------------------------------------------------------------------------------')
