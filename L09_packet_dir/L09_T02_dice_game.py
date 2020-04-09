# *************************************************"ИГРА В КОСТИ"******************************************************
# Комп загадывает пару чисел, генератор имитирующий бросков 2 кубиков, количество бросков, совпадение по условию
# ПЛАН создания КЛАССА ("чертёж объекта") в Python:
#
# ОБЪЕКТ
# ---------------------------------------------------------------------------------------------------------------------
# АТРИБУТЫ                                      МЕТОДЫ
# (ПЕРЕМЕННЫЕ КЛАССА)                           (ФУНКЦИИ КЛАССА, могут быть "грязными", т.е. могут изм. зн. атрибутов)
# -------------------------------------         -----------------------------------------------------------------------
# Количество попыток.                           # Инициализация параметров игры.
# Числа, загаданные компьютером (random).       # Бросание костей:
#                                                   условие совпадения брошенных костей
#                                                   и загаданных компьютером.
#                                               Выбор режима игры:ыми
#                                                   ----свпали--------
#                                                   1.   2 числа,
#                                                   2.   1 число,
#                                                   3.   совпала сумма чисел
#----------------------------------------------------------------------------------------------------------------------

import random

# по соглашению программистов, имена классов пишутся с Большой буквы - Dice (Кости)
class Dice:
    # Инициалицирующий МЕТОД (специальный метод с "__")
    # Инициализация атрибутов игры (N - количество бросков "throw_num" )
    def __init__(self):
        self.id_return = 0 # Поля читаются и записываются через "self" - указывает на текущий экземпляр класса

    # Обычный метод объекта(метод экземпляра класса),
    # имеет те же правила наименования, что и обычные функции:
    def set_hidden_numbers(self):
        # Числа, загаданные компьютером (random от 1 до 6).
        self._hidden_num_1 = random.randint(1,6) # инкапсуляция(скрытие значений параметра "_hidden_num_1", "_земля")
        self._hidden_num_2 = random.randint(1,6) # инкапсуляция(скрытие значений параметра "_hidden_num_2", "_земля")

    # имитация бросания костей (кубиков со сторанами указывающими на цифры от 1 до 6).
    def throw_dices(self):
        self.dice_1 = random.randint(1,6)
        self.dice_2 = random.randint(1,6)
#----------------------------------------------------------------------------------------------------------------------

# Проверка класса (посмотрим, что получилось):
print('# **************"ИГРА В КОСТИ"******************')
if __name__ == '__main__':
    # Инициализация бросков
    N=8
    for i in range(1):
        dice_game = Dice() # запуск с указанием количества попыток
        dice_game.set_hidden_numbers()
        dice_game.throw_dices()
        chk=0
        print('#', i, '- бросок игрока:', dice_game.dice_1, dice_game.dice_2)
        print('# - числа компьютера:', dice_game._hidden_num_1,dice_game._hidden_num_2) # вывод
        # условия совпадения брошенных костей и загаданных компьютером, индексация результата:
        if dice_game.dice_1 == dice_game._hidden_num_1 or dice_game.dice_1 == dice_game._hidden_num_2 \
        or dice_game.dice_2 == dice_game._hidden_num_1 or dice_game.dice_2 == dice_game._hidden_num_2:
            print('# результат: есть совпадение цифр (1-6)')
            chk=1
        if (dice_game.dice_1 + dice_game.dice_2) == (dice_game._hidden_num_1 + dice_game._hidden_num_2):
            print('# результат: совпадение сумм!!!!!!')
            chk=1
        if chk==0:
            print('# результат: нет ни одного совпадения.')
    print('# **********************************************')
    print('# **************Игра закончена!*****************')
#----------------------------------------------------------------------------------------------------------------------

# **************"ИГРА В КОСТИ"******************
# 1 - бросок игрока: 3 4
# - числа компьютера: 2 1
# результат: нет ни одного совпадения.
# 2 - бросок игрока: 5 5
# - числа компьютера: 3 5
# результат: есть совпадение цифр (1-6)
# 3 - бросок игрока: 6 1
# - числа компьютера: 2 5
# результат: совпадение сумм!!!!!!
# 4 - бросок игрока: 3 5
# - числа компьютера: 6 5
# результат: есть совпадение цифр (1-6)
# 5 - бросок игрока: 6 6
# - числа компьютера: 1 1
# результат: нет ни одного совпадения.
# 6 - бросок игрока: 3 1
# - числа компьютера: 5 5
# результат: нет ни одного совпадения.
# 7 - бросок игрока: 3 4
# - числа компьютера: 5 2
# результат: совпадение сумм!!!!!!
# **********************************************
# **************Игра закончена!*****************

# Process finished with exit code 0