'''
Работа с текстовыми файлами
'''

# Простой считывание/ открытие файла в режиме чтения
# f = open('L07_T01_data')
# content  = f.read()
# print(content)
# f.close()

# Открыли файл в режими записи (содержимое удалилось)
# f = open('L07_T01_data', 'w')
# content  = f.read()
# print(content)
# f.close()

# Считывание файла построчно
# f = open('L07_T01_data')
# for line in f:
#     print(line)
# f.close()


# Менеджер контекста
with open('L07_T01_data') as f:
    line = f.readline() # считывание одной строки
    print(line)
  # for line in f:
  #     print(line)

# Считывание побайтно

with open('L07_T01_data', 'r') as f:
    data = f.read(10) # считывание одной строки
    print(data, type(data))


# Запись в файл

# with open('data_new', 'w') as f:
#   f.writeline('This is new file!')


# Запись в списком
data = ['1\n','2 \n','3 \n'] # '\n' - перенос строки

with open('data_new', 'w') as f:
  f.writelines(data)


