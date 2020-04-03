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
def get_context(company, result_sku_list):
    return {
        'name_of_info': company,
        'date_of_info': result_sku_list,
    }

# здесь происходит вставка в шаблон (signature - картинка)
def from_template(company, result_sku_list, template, signature):
    template = DocxTemplate(template)
    context = get_context(company, result_sku_list)  # gets the context used to render the document

    img_size = Cm(15)  # sets the size of the image
    Jobs_from_L07_image1 = InlineImage(template, signature, img_size)
    context['Jobs_from_L07_image1'] = Jobs_from_L07_image1  # adds the InlineImage object to the context
    template.render(context)
    Jobs_from_L07_image2 = InlineImage(template, signature, img_size)
    context['Jobs_from_L07_image2'] = Jobs_from_L07_image2  # adds the InlineImage object to the context
    template.render(context)
    Jobs_from_L07_image3 = InlineImage(template, signature, img_size)
    context['Jobs_from_L07_image3'] = Jobs_from_L07_image3  # adds the InlineImage object to the context
    template.render(context)

    template.save(company + '_' + str(datetime.datetime.now().date()) + '_report.docx')


def generate_report(company, result_sku_list):
    template = 'Jobs_from_L07_format_doc_report.docx'
    signature1 = 'Jobs_from_L07_image1.PNG'
    signature2 = 'Jobs_from_L07_image2.PNG'
    signature3 = 'Jobs_from_L07_image3.PNG'
    document = from_template(company, result_sku_list, template, signature1,signature2,signature3)

# вспомагательная функция
def toFixed(numObj, digits=0):
    return f"{numObj:.{digits}f}"

generate_report('CORONAVIRUS', [0.78, 0.12, 0.05, 0.01, 0.01])