import random

class Dice_inc:
    def __init__(self, N):
        self.throw_num = N
        self.current_throw = 0

    def set_hidden_numbers(self):
        self.__hidden_num_1 = random.randint(1,6)
        self.__hidden_num_2 = random.randint(1,6)


    def change_dices(self):
        self.__hidden_num_1 = random.randint(1,6)
        self.__hidden_num_2 = random.randint(1,6)

    @property
    def hidden_num_1(self):
        return self.__hidden_num_1

    @hidden_num_1.setter
    def hidden_num_1(self, dice):
        if (dice > 0) & (dice < 7):
            self.__hidden_num_1 = dice
        else:
            raise ValueError('Числа должны быть от 1 до 6 !!!')

    @property
    def hidden_num_2(self):
        return self.__hidden_num_2

    @hidden_num_2.setter
    def hidden_num_2(self, dice):
        if (dice > 0) & (dice < 7):
            self.__hidden_num_2 = dice
        else:
            raise ValueError('Числа должны быть от 1 до 6 !!!')

    def throw_dices(self):
        dice_1 = random.randint(1,6)
        dice_2 = random.randint(1,6)
        self.current_throw+=1
        if self.current_throw > self.throw_num:
            raise Exception('Вы превысили количество попыток!')

        if {dice_1,dice_2} == {self.__hidden_num_1, self.__hidden_num_2}:
            return True
        else:
            return False


if __name__ == '__main__':
    dice_game = Dice_inc(2)
    dice_game.set_hidden_numbers()
    print(dir(dice_game))

    print(dice_game.hidden_num_1, dice_game.hidden_num_2)

    dice_game.hidden_num_1 = 7

    dice_game.hidden_num_2 = 4

    print(dice_game.hidden_num_1, dice_game.hidden_num_2)

    for i in range(4):
        try:
            print(dice_game.throw_dices())
        except:
            print('Игра закончена!')

