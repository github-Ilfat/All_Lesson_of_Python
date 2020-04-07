#Работа с текстовыми файлами
txt = """******************************************************************************************
:::::::O88888Oo:::::888o::::O8888888o...:O8888O:..oOOOOOOOOO::::OOOO::::::::::::oOOOOOo:..
:::::o:O88OO888o:::O8888::::O88OOOOOo:.o888OO888o.oOOO888OOO::::8888o::::::::::OOOOOOOO:..
:::::::O88::o88O::o88888o:::O88::::::::888:..:888:..::88O::::::O8OO8O:::::::::OOOo::::o:..
:::::::O88ooO88O::O88o888:::O888888O::o88o:...O88o...:88O...::o88oo88o::::::::OOO::.......
:::::::O888888O:::88O:O88o::O88OOO888:o88o:...O88o...:88O:::::O8O::O8O::::::::OOO::.......
:::::::O88oooo:::o8888888O::O88:::O88oo88O:..:O88:...:88O::::o88OOOO8O:::...::OOO::.......
....:::O88:::::::888OOOO88o:O88ooo888o:O88O::O88O....:88O::::O88OOOO8Oo......:OOOO:::oO:..
....:::O88::::::o88o::::88O:O8888888o:::O888888O:...:o88o:..o88O::::OOO:......:OOOOOOOO...
....::::::::::::::::::::::::::::::::...::ooooo::::::::oo:...:oo::...:oo:.......:ooOOoo:...
::::::.....::........::::::::::::::.......:::::..:::........:::::...............::..::....
::::::...............:::::::oo:::o::.......:::.....::.........:::..............:......:...
....::::...........::::::::o88o:O8O.........:......::..........................:..........
......:::......:::....::::::oO888O:.........:......:...........................:..........
.....:o88o::::....OOOo.:::oOO::::OOO:..:oooooooo..::.:oo:....:::::....:::...:::::....::...
...oO888888Oo....:8888:::.o88:.:O888:..:88888888:::::O888:...:OOOO...:OOO:..OOO.::oOOO....
..O88OO88OO88o...O8888o:..o88:.O8888:..o88o::O88:...o8888O...:OOOOo..OOOO:..OOO..oOOOO....
..888:o88::888:.:88oO88:..o88:o88O88:..o88:..O88:...O8OO8O::.:OOOOO.oOOOO:..OOO.:OOOOo....
..888:o88:.888:.O88::88o..o88o88oO88:..o88:..O88:..o88o:OOo:::OOoOOoOOoOO:..OOO:OOoOOo....
..o88Oo88oo88O:o88888888:.o8888o.O88:..O8O...O88:..OOOooOOO:.:OOooOOOooOO:..OOOOOo.OOo....
...oO8888888o..O88OOOO88o.o888O..O88::o88o...O88..oOOOOOOOOo.:OOo:OOO.oOO:..OOOOo..OOo....
.....:o88o::..:88O::::88O.o88O...o88.O88O....OOO..OOO::::OOO.:OOo..:::oOO:.:OOOo...OOo....
.......::......::::::::o:.:::....:oo.:oo.....ooo.:oo:....:OO::OOo.....oOO:.:OOO....OOo....
******************************************************************************************"""

# Открыли файл в режими записи (содержимое удалилось)
f = open('L07_T01_body_file_data', 'w')
content = f.write('') # очистка файла или запись '' - empty
#print(len(txt))
#print(content) # в данном случае, выводит integer длину str - аналогично print(len(txt))
f.close()

# Открыли файл в режими записи (содержимое удалилось)
f = open('L07_T01_body_file_data', 'w')
content = f.write(txt)
#f.truncate(1010) # -- срезает указанное количество символов сначала текста, оставшееся удаляет
#print(len(txt))
#print(content) # в данном случае, выводит integer длину str - аналогично print(len(txt))
f.close()

'''
# Простой считывание/ открытие файла в режиме чтения
f = open('L07_T01_body_file_data')
content  = f.read()
#print(txt)
#print(content) # в данном случае, выводит значение str - аналогично print(txt)
f.close()
'''

# Считывание файла построчно
f = open('L07_T01_body_file_data')
i=1
for line in f:
  space=' '
  if i<10: space='  '
  print('str N', i, space + '   ', line, end='')
  i+=1
f.close()
print()

# Менеджер контекста
with open('L07_T01_body_file_data') as f:
    line = f.readline() # считывание одной строки в память, а при следующем чтении идёт обращение к строке №2
#    line = f.readline(50) # либо 50 символов строки f.readline(50) уже со второй строки
    print('str N1       ', line)


  # for line in f:
  #     print(line)

# Считывание побайтно
with open('L07_T01_body_file_data', 'r') as f:
  for i in range(11):
      data = f.read(30) # считывание 30 символов из всего текста
      print(data, end='')
      #print(data, type(data))

'''
# Запись в файл

# with open('data_new', 'w') as f:
#   f.writeline('This is new file!')


# Запись в списком
data = ['1\n','2 \n','3 \n'] # '\n' - перенос строки

with open('data_new', 'w') as f:
  f.writelines(data)
'''

