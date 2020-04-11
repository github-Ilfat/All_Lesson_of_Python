# С возможностью отладки и тестирования
# С возможностью отладки и тестирования
# *************************************************"ИГРА В КОСТИ"******************************************************
# Комп загадывает пару чисел, генератор имитирующий бросков 2 кубиков, количество бросков, совпадение по условию
# ПЛАН создания КЛАССА ("чертёж объекта") в Python:
#
# ОБЪЕКТ
# ---------------------------------------------------------------------------------------------------------------------
# АТРИБУТЫ                                      МЕТОДЫ
# (ПЕРЕМЕННЫЕ КЛАССА)                           (ФУНКЦИИ КЛАССА, могут быть "грязными", т.е. могут изм. зн. атрибутов)
# -------------------------------------         -----------------------------------------------------------------------
# Переключатель режима игры, результат.         # 1 Инициализация параметров игры.
# 2 Числа, загаданные "компьютером".            # 2 Подключение генератора случайных чисел random для роли "компьютер".
# 2 Числа, загаданные "игроком".                # 3 Подключение генератора случайных чисел random для роли "игрок".
#                                               # Режимы игры: 1 полное, 2 раздельное, 3 только равенство сумм
#                                               # Выбор режима игры.
#----------------------------------------------------------------------------------------------------------------------
# С возможностью отладки и тестирования
# С возможностью отладки и тестирования

import random

class Dice_incopsulation:
    # Инициалицирующий МЕТОД (специальный метод с "__")
    # Инициализация атрибутов игры (N - количество бросков "throw_num" )
    def __init__(self,sw):
        # Поля читаются и записываются через "self" - указывает на текущий экземпляр класса
        self.id_return = 0
        # id результата: 11 - есть полное совпадение цифр (1-6)!!!
        # id результата: 2,12 - есть раздельное совпадение цифр (1-6)
        # id результата: 10,11,12 - результат: совпадение сумм!!!!!!
        self.switch = sw
        # Режимы игры: 1 полное,
        # Режимы игры: 2 раздельное,
        # Режимы игры: 3 только равенство сумм

    # Обычный метод объекта(метод экземпляра класса),
    # имеет те же правила наименования, что и обычные функции:
    def set_hidden_numbers(self):
        # Числа, загаданные компьютером (random от 1 до 6).
        self.__hidden_num_1 = random.randint(1,6) # инкапсуляция( двойная земля "__") скрытие
        self.__hidden_num_2 = random.randint(1,6) # инкапсуляция( двойная земля "__") скрытие

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
        if (sw==1 or sw==2) and (dice_game.dice_1 == dice_game.__hidden_num_1 and dice_game.dice_2 == dice_game.__hidden_num_2):
            self.id_return = 1
        if sw==2 and self.id_return == 0 \
                and (dice_game.dice_1 == dice_game.__hidden_num_1 or dice_game.dice_1 == dice_game.__hidden_num_2 \
                     or dice_game.dice_2 == dice_game.__hidden_num_1 or dice_game.dice_2 == dice_game.__hidden_num_2):
            self.id_return = 2
        if ((dice_game.dice_1 + dice_game.dice_2) == (dice_game.__hidden_num_1 + dice_game.__hidden_num_2)):
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
        dice_game = Dice_incopsulation(sw) # запуск с указанием количества попыток
        dice_game.set_hidden_numbers()
        dice_game.throw_dices()
        chk=0
        sp=' '
        if i>9: sp=''
        print('#'+sp, i, '- бросок игрока:', dice_game.dice_1, dice_game.dice_2)
        print('# - числа компьютера:', dice_game.hidden_num_1,dice_game.hidden_num_2) # вывод
        # условия совпадения брошенных костей и загаданных компьютером, индексация результата:
        if dice_game.id_return == 11:
            print('# результат: есть полное совпадение цифр (1-6)!!!')
            chk=1
        if dice_game.id_return == 2 or dice_game.id_return == 12:
            print('# результат: есть раздельное совпадение цифр (1-6)')
            chk=1
        if  dice_game.id_return == 11 or dice_game.id_return == 12 or dice_game.id_return == 10:
            print('# результат: совпадение сумм!!!!!!')
            chk=1
        if chk==0:
            print('# результат: нет ни одного совпадения.')
    print('# **************************************************************************************************')
    print('# ************************************  Игра окончена!  ********************************************')
#----------------------------------------------------------------------------------------------------------------------

# ОТЛАДКА:

    print(dir(dice_game))

    #dice_game.__throw_dices()

    #print('Доступ нет: ', dice_game.__hidden_num_1,dice_game.__hidden_num_2 ) # эти скрыты

    print('Доступ есть через set: ', dice_game.hidden_num_1, dice_game.hidden_num_2)

    print('Доступ есть через get: ', dice_game.get_dice1(), dice_game.get_dice2())

    # в ручную задаём значения в set:
    dice_game.hidden_num_1 = 5
    dice_game.hidden_num_2 = 4

    # в ручную задаём значения в get:
    dice_game.set_dice1(5)
    dice_game.set_dice2(4)

    # print(dice_game.get_dice1(), dice_game.get_dice2())
    print(dice_game.hidden_num_1, dice_game.hidden_num_2)