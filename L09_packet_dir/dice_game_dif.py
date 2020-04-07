from dice_game import Dice
import random

class Dice_dif(Dice):
    '''
    Допишем режимы игры в кости
    type 1: совпали как неупорядоченная пара
    type 2: совпало хотябы одно значение
    type 3: совпала сумма
    '''
    def __init__(self, N, type):
        super().__init__(N)
        self.type_game = type

    def throw_dices(self):
        dice_1 = random.randint(1,6)
        dice_2 = random.randint(1,6)
        self.current_throw+=1

        if self.current_throw > self.throw_num:
            raise Exception('Вы превысили количество попыток!')

        if self.type_game == 1:
            if {dice_1,dice_2} == {self._hidden_num_1, self._hidden_num_2}:
                return True
            else:
                return False
        elif self.type_game == 2:
            if (dice_1 in {self._hidden_num_1, self._hidden_num_2}) or (dice_2 in {self._hidden_num_1, self._hidden_num_2}):
                print('Attemp:', dice_1, dice_2)
                return True
            else:
                return False
        elif self.type_game == 3:
            if dice_1 + dice_2 == self._hidden_num_1 + self._hidden_num_2:
                print('Attemp:', dice_1, dice_2)
                return True
            else:
                return False

if __name__ == '__main__':
    dice_game = Dice_dif(3,3)
    dice_game.set_hidden_numbers()
    print(dice_game._hidden_num_1,dice_game._hidden_num_2)
    for i in range(4):
        try:
            print(dice_game.throw_dices())
        except:
            print('Игра закончена!')


