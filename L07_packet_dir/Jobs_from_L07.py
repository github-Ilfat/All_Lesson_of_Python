'''
LIGHT:
1) Вручную создал текстовый файл "Jobs_from_L07_data_text_file" с данными по
CORONAVIRUS (COVID-19) from (https://coronavirus-monitor.ru/)
Мировая статистика случаев заражения коронавирусом на 03.04.2020
2) Создал doc шаблон, где использовал данные параметры.
3) Автоматически генерируется отчет о CORONAVIRUS (COVID-19) в формате doc (как в видео 7.2).
4) Создал csv файл с данными о CORONAVIRUS (COVID-19).
5) Создал json файл с данными о CORONAVIRUS (COVID-19).
'''

# Решение по пункту задания 1

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