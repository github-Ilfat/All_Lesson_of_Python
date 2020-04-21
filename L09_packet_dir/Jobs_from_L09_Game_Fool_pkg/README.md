# ***************************************   КАРТОЧНАЯ ИГРА "В ДУРАКА"  ************************************************
# Колода карт из 36 карт, перемешивается и раздаётся игрокам (компьютер1 и компьютер2), (6,7,8,9,10,V,D,K,T) 9x4 масти.
# ПЛАН создания КЛАССА ("чертёж объекта") в Python:
#
# ОБЪЕКТ
# ---------------------------------------------------------------------------------------------------------------------
# АТРИБУТЫ                                      МЕТОДЫ
# (ПЕРЕМЕННЫЕ КЛАССА)                           (ФУНКЦИИ КЛАССА, могут быть "грязными", т.е. могут изм. зн. атрибутов)
# -------------------------------------         -----------------------------------------------------------------------
# результат.                                    # 1 Инициализация параметров игры.
# Раздача по 6 карт, смешанных "компьютером",   # 2 Подключение генератора случайных чисел random для колоды карт.
# игроку и компьютеру, сохранение колоды        # 3 Подключение правил игры.
#                                               # 4 Организация идентификации результата и вывода сообщений
#                                               #
#----------------------------------------------------------------------------------------------------------------------


# Данную задачу начал выполнять с "конца", т.е. с интерфейса карточной игры, т.к. сокурсниками уже были выполнены 
# работы по созданию логики игры "движка", но у них не было интерфейса приближённого к оригиналу игры,
# выполнил подключение своего интерфейса к логике одного из сокурсников (с исправлением ошибки, прерывающей игру):
#
# Алексей Ведяшкин • Вс 02 Фев 12:57 • Ответ создан Сб 01 Фев 01:00
# https://github.com/sdfxisme/lesson9/blob/master/cards.py
 




'''
#!python3.7
#coding: utf-8
# Желательно настроить шрифт (File-Settings-Editor-Font) - Consolas, size:13, Line spacing:0.8

Ильфат Сафиуллин: "class Game_fool_card_desc:"


# Пример вызова класса "Game_fool_card_desc"
'''
name1='' #──── имя игрока 1
name2='' #──── имя игрока 2

# id num_card: [' ','§','6','7','8','9','10','V','D','K','T'] (''-'Т')
# id num_card: [ 0 , 1 , 2 , 3 , 4 , 5 ,  6 , 7 , 8 , 9 , 10] (0 - 10)
# id num_suit: [' ','§','♣','♦','♥','♠'] (''-'♠')
# id num_suit: [ 0 , 1 , 2 , 3 , 4 , 5 ] (0 - 5 )
gmr1c = [0,0,0,0,0,0,0,0,0 возможно увеличение ] #──── ранг карты, игрока 1
gmr1s = [0,0,0,0,0,0,0,0,0 занимаемых картомест] #──── масть карты, игрока 1
#        | | |
#        | └─└── свободное картоместо    (с 1 по 3, список картомест игрока 1)
#        | 
#        └─ 'надпись "1 ИГРОК:"'
#        └─ '           "имя"'
#        └─ '         "действие"'

# [0,,,5] and [len-2,len-1] id num_card: [' ','§','6','7','8','9','10','V','D','K','T'] (''-'Т')
# [0,,,5] and [len-2,len-1] id num_card: [ 0 , 1 , 2 , 3 , 4 , 5 ,  6 , 7 , 8 , 9 , 10] (0 - 10)
# [0,,,5] and [len-2,len-1] id num_suit: [' ','§','♣','♦','♥','♠'] (''-'♠')
# [0,,,5] and [len-2,len-1] id num_suit: [ 0 , 1 , 2 , 3 , 4 , 5 ] (0 - 5 )
# [5,,,len-3] flaf_gamer_1 and address id num_card in gmr1c: ['0','1',,,,len(gmr1c)]
# [5,,,len-3] flaf_gamer_2 and address id num_card in gmr2c: ['0','1',,,,len(gmr2c)]

#          ┌─ место "Колоды" 
#          |   ┌─ место "Козыря              (с 5 по 15,все нечётные, если ходит, dsc_c адреса списка карт игрока 1)
#          |   |                             (с 6 по 16, все чётные, если отбивается, dsc_c адреса списка карт игрока 1) 
#          |   |     наличие ходов игроками       
#          |   |   ┌───────────────────────┐ ┌─ место "Биты"
dsc_c = [0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0] #──── ранг карты, для позиций с 1 по 4 и 18
dsc_s = [0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0] #──── масть карты, для позиций с 1 по 4 и 18 
#        0,1,2,3,4,5,6,7,8,9,1,1,1,1,1,1,1,1,1,1 
#        |   |   |           0,1,2,3,4,5,6,7,8,9
#        |   |   |                             └── свободное картоместо
#        |   └───└── свободное картоместо    (с 5 по 15,все нечётные, если ходит, dsc_s адреса списка карт игрока 2)
#        └─── dsc_s=[0]флаг вкл.налож карт   (с 6 по 16, все чётные, если отбивается, dsc_s адреса списка карт игрока 2)
                        
# id num_card: [' ','§','6','7','8','9','10','V','D','K','T'] (''-'Т')
# id num_card: [ 0 , 1 , 2 , 3 , 4 , 5 ,  6 , 7 , 8 , 9 , 10] (0 - 10)
# id num_suit: [' ','§','♣','♦','♥','♠'] (''-'♠')
# id num_suit: [ 0 , 1 , 2 , 3 , 4 , 5 ] (0 - 5 )
gmr2c = [0,0,0,0,0,0,0,0,0 возможно увеличение ] #──── ранг карты, игрока 2
gmr2s = [0,0,0,0,0,0,0,0,0 занимаемых картомест] #──── масть карты, игрока 2
#        0,1,2,3,4,5,6,7,8
#        | | |
#        | └─└── свободное картоместо    (с 1 по 3, список картомест игрока 2)
#        | 
#        └─ 'надпись "2 ИГРОК:"'
#        └─ '           "имя"'
#        └─ '         "действие"'

x=Game_fool_card_desc(name1, gmr1c, gmr1s, name2, gmr2c, gmr2s, dsc_c, dsc_s, cld_n))
x.blk_chk()
x.Dsc_img()
'''
'''
from L09_packet_dir.Jobs_from_L09_Game_Fool_pkg import Game_fool_card_desc

name1='' #──── имя игрока 1
name2='' #──── имя игрока 1

gmr1c = [0,0,0,2,3,4,5,6,7] #──── ранг карты, игрока 1
gmr1s = [0,0,0,3,4,5,2,3,4] #──── масть карты, игрока 1

dsc_c = [0,1,0,9,0,4,0,5,0,6,0,7,0,8,0,3,0,0,1] #──── ранг карты, для позиций с 1 по 4 и 18
dsc_s = [0,1,0,3,0,0,4,0,5,0,6,0,7,0,8,0,3,0,1] #──── масть карты, для позиций с 1 по 4 и 18

gmr2c = [0,0,0,3,4,5,6,7,8] #──── ранг карты, игрока 2
gmr2s = [0,0,0,3,4,5,2,3,4] #──── масть карты, игрока 2


x=Game_fool_card_desc(name1, gmr1c, gmr1s, name2, gmr2c, gmr2s, dsc_c, dsc_s, cld_n))
x.blk_chk()
x.Dsc_img()
'''