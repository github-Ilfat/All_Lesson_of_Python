# ***************************************  "КАРТОЧНАЯ ИГРА В "ПОДКИДНОГО ДУРАКА" "*************************************
# Колода карт из 36 карт, перемешивается и раздаётся игрокам (компьютер и 1 игрок), (6,7,8,9,10,V,D,K,T) 9x4 масти.
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

# С возможностью отладки и тестирования

import random

# по соглашению программистов, имена классов пишутся с Большой буквы "Game_Fool" 
class Game_Fool:
    # Инициалицирующий МЕТОД (специальный метод с "__")
    # Инициализация атрибутов игры (N - количество бросков "throw_num" )
    def __init__(self,sw):
        # Поля читаются и записываются через "self" - указывает на текущий экземпляр класса
        # крести chr(167), буби chr(168), черви chr(169), пики chr(170)
        self.suit=['♣','♦','♥','♠']
        self.card=['6','7','8','9','10','V','D','K','T']
        self.Card_deck = [] # Колода карт
        self.Gamer_deck = Gmr_dck # карты игрока
        self.Comp_desk = Cmp_dsk # карты компьютера
        self.Trump_card = Trmp_crd # козырная карта
        self.Broken_cards = Brkn_crds # битые карты

    # Обычный метод объекта(метод экземпляра класса),
    # имеет те же правила наименования, что и обычные функции:
    def set_Card_deck(self):
        # заполнение списка - колоды карт
        for c in range(0,9):
            self.card_tmp=self.card[c]
            for m in range(0,4):
                self.Card_deck.append(self.card_tmp + self.suit[m])
        random.shuffle(self.Card_deck)
        print(self.Card_deck)
        random_number = random.choice(self.Card_deck)
        print(self.Card_deck)

        self.__Card_deck = random.randint(1,36) # инкапсуляция( двойная земля "__") скрытие
        self.__Gamer_deck = random.randint(1,6) # инкапсуляция( двойная земля "__") скрытие
        self.__Comp_desk = random.randint(1,6) # инкапсуляция( двойная земля "__") скрытие

    # Метод скрытого переприсваивания значений, может пригодится, например, при автоматическом тестировании.
    def change_dices(self):
        self.__hidden_num_1 = random.randint(1,6)
        self.__hidden_num_2 = random.randint(1,6)

    # set можем изменить без получения значения
    # Метод скрытого переприсваивания значений для I кости, может пригодится, например, при ручном тестировании.
    def set_dice1(self, dice):
        #if (dice > 0) & (dice < 7)
        self.__hidden_num_1 = dice
    # Метод скрытого переприсваивания значений для II кости, может пригодится, например, при ручном тестировании.
    def set_dice2(self, dice):
        #if (dice > 0) & (dice < 7)
        self.__hidden_num_2 = dice

    # get можем изменить c получением значения
    # Метод скрытого переприсваивания значений для I кости, может пригодится, например, при ручном тестировании.
    def get_dice1(self):
        #if (dice > 0) & (dice < 7)
        return self.__hidden_num_1
    # Метод скрытого переприсваивания значений для II кости, может пригодится, например, при ручном тестировании.
    def get_dice2(self):
        #if (dice > 0) & (dice < 7)
        return self.__hidden_num_2

    @property
    def hidden_num_1(self):
        #if (dice > 0) & (dice < 7)
        return self.__hidden_num_1

    @hidden_num_1.setter
    def hidden_num_1(self, dice):
        self.__hidden_num_1 = dice

    @property
    def hidden_num_2(self):
        #if (dice > 0) & (dice < 7)
        return self.__hidden_num_2

    @hidden_num_2.setter
    def hidden_num_2(self, dice):
        self.__hidden_num_2 = dice

    # имитация бросания костей (кубиков со сторанами указывающими на цифры от 1 до 6).
    def throw_dices(self):
        self.dice_1 = random.randint(1,6)
        self.dice_2 = random.randint(1,6)
        # условия совпадения брошенных костей и загаданных компьютером, индексация результата:
        # совпала первая кость
        if (sw==1 or sw==2) and (fool_game.dice_1 == fool_game.__hidden_num_1 and fool_game.dice_2 == fool_game.__hidden_num_2):
            self.id_return = 1
        if sw==2 and self.id_return == 0 \
                and (fool_game.dice_1 == fool_game.__hidden_num_1 or fool_game.dice_1 == fool_game.__hidden_num_2 \
                     or fool_game.dice_2 == fool_game.__hidden_num_1 or fool_game.dice_2 == fool_game.__hidden_num_2):
            self.id_return = 2
        if ((fool_game.dice_1 + fool_game.dice_2) == (fool_game.__hidden_num_1 + fool_game.__hidden_num_2)):
            self.id_return += 10
        if self.id_return == 0:
            return self.id_return
#----------------------------------------------------------------------------------------------------------------------

# Проверка класса (посмотрим, что получилось):
print('# ********************************** "ИГРА В КОСТИ" ************************************************')
if __name__ == '__main__':
    print('# Режим игры:')
    sw=2 # Указать режим игры: 1 полное, 2 раздельное, 3 только равенство сумм
    N=7 # Указать количество бросков
    if sw==1: print('# ', sw, '- только полное совпадение 2 костей "один в один", равенство сумм костей')
    if sw==2: print('# ', sw, '- раздельное совпадение по 1 кости (возможность равенством сумм и полного совпадения)')
    if sw==3: print('# ', sw, '- только равенство сумм костей')
    print('# количество бросков:', N)
    print('# **************************************************************************************************')
    # Инициализация бросков
    for i in range(1,N+1):
        fool_game = Game_Fool(sw) # запуск с указанием количества попыток
        fool_game.set_hidden_numbers()
        fool_game.throw_dices()
        chk=0
        sp=' '
        if i>9: sp=''
        print('#'+sp, i, '- бросок игрока:', fool_game.dice_1, fool_game.dice_2)
        print('# - числа компьютера:', fool_game.hidden_num_1,fool_game.hidden_num_2) # вывод
        # условия совпадения брошенных костей и загаданных компьютером, индексация результата:
        if fool_game.id_return == 11:
            print('# результат: есть полное совпадение цифр (1-6)!!!')
            chk=1
        if fool_game.id_return == 2 or fool_game.id_return == 12:
            print('# результат: есть раздельное совпадение цифр (1-6)')
            chk=1
        if  fool_game.id_return == 11 or fool_game.id_return == 12 or fool_game.id_return == 10:
            print('# результат: совпадение сумм!!!!!!')
            chk=1
        if chk==0:
            print('# результат: нет ни одного совпадения.')
    print('# **************************************************************************************************')
    print('# ************************************  Игра окончена!  ********************************************')
    #----------------------------------------------------------------------------------------------------------------------

    # ОТЛАДКА:

    print(dir(fool_game))

    #fool_game.__throw_dices()

    #print('Доступ нет: ', fool_game.__hidden_num_1,fool_game.__hidden_num_2 ) # эти скрыты

    print('Доступ есть через set: ', fool_game.hidden_num_1, fool_game.hidden_num_2)

    print('Доступ есть через get: ', fool_game.get_dice1(), fool_game.get_dice2())

    # в ручную задаём значения в set:
    fool_game.hidden_num_1 = 5
    fool_game.hidden_num_2 = 4

    # в ручную задаём значения в get:
    fool_game.set_dice1(5)
    fool_game.set_dice2(4)

    # print(fool_game.get_dice1(), fool_game.get_dice2())
    print(fool_game.hidden_num_1, fool_game.hidden_num_2)