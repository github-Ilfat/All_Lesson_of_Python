import datetime

# необходимые модули и функции для работы с doc
from docxtpl import DocxTemplate
from docxtpl import InlineImage
from docx.shared import Cm
from docxtpl import DocxTemplate, InlineImage

# get_context - возвращает словарь аргуменов
def get_context(company, result_sku_list):
    return {
        'retailer': company,
        'sku_list': result_sku_list,
    }

# здесь происходит вставка в шаблон (signature - картинка)
def from_template(company, result_sku_list, template, signature):
    template = DocxTemplate(template)
    context = get_context(company, result_sku_list)  # gets the context used to render the document

    img_size = Cm(15)  # sets the size of the image
    acc = InlineImage(template, signature, img_size)

    context['acc'] = acc  # adds the InlineImage object to the context
    template.render(context)

    template.save(company + '_' + str(datetime.datetime.now().date()) + '_report.docx')


def generate_report(company, result_sku_list):
    template = 'L07_T02_format_doc_report.docx'
    signature = 'L07_T02_work_with_doc_image-acc.png'
    document = from_template(company, result_sku_list, template, signature)

# вспомагательная функция
def toFixed(numObj, digits=0):
    return f"{numObj:.{digits}f}"

generate_report('Ozon', [0.78, 0.12, 0.05, 0.01, 0.01])