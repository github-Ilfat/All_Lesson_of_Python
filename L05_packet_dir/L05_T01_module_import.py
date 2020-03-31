import os # импорт всего модуля

from os import mkdir # импортирование отдельный функций

from os import rmdir as remover

from os import * # импортирование модуля целиком

#remover('test')

mkdir('test')

remover('test')

print(getcwd())

# получение название содержимых файлов каталога

print(list(walk(getcwd())))