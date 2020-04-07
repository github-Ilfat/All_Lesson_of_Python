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

    def set_dice1(self, dice):
        #if (dice > 0) & (dice < 7)
        self.__hidden_num_1 = dice

    def get_dice1(self):
        #if (dice > 0) & (dice < 7)
        return self.__hidden_num_1

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

    def set_dice2(self, dice):
        self.__hidden_num_2 = dice

    def get_dice2(self):
        #if (dice > 0) & (dice < 7)
        return self.__hidden_num_2

    def throw_dices(self):
        dice_1 = random.randint(1,6)
        dice_2 = random.randint(1,6)
        self.current_throw+=1
        if self.current_throw > self.throw_num:
            raise Exception('Вы превысили количество попыток!')

        if {dice_1,dice_2} == {self._hidden_num_1, self._hidden_num_2}:
            return True
        else:
            return False

    def __throw_dices(self):
        pass

if __name__ == '__main__':
    dice_game = Dice_inc(2)
    dice_game.set_hidden_numbers()
    print(dir(dice_game))
    #dice_game.__throw_dices()

#    print(dice_game.__hidden_num_1,dice_game.__hidden_num_2 )
#    print(dice_game.get_dice1(), dice_game.get_dice2())

    print(dice_game.hidden_num_1, dice_game.hidden_num_2)

    #dice_game.set_dice1(5)
    dice_game.hidden_num_1 = 5
    #dice_game.set_dice2(4)
    dice_game.hidden_num_2 = 4

   # print(dice_game.get_dice1(), dice_game.get_dice2())
    print(dice_game.hidden_num_1, dice_game.hidden_num_2)

    for i in range(4):
        try:
            print(dice_game.throw_dices())
        except:
            print('Игра закончена!')

