from L09_packet_dir.L09_T02_dice_game_full import Dice

import random

class Dice_type_1(Dice):

    # имитация бросания костей (кубиков со сторанами указывающими на цифры от 1 до 6).
    def throw_dices(self):
        self.dice_1 = random.randint(1,6)
        self.dice_2 = random.randint(1,6)
        # условия совпадения брошенных костей и загаданных компьютером, индексация результата:
        # совпала первая кость
        if (sw==1 or sw==2) and (dice_game.dice_1 == dice_game._hidden_num_1 and dice_game.dice_2 == dice_game._hidden_num_2):
            self.id_return = 1
        if self.id_return == 0:
            return self.id_return

class Dice_type_2(Dice):
    # имитация бросания костей (кубиков со сторанами указывающими на цифры от 1 до 6).
    def throw_dices(self):
        self.dice_1 = random.randint(1,6)
        self.dice_2 = random.randint(1,6)
        # условия совпадения брошенных костей и загаданных компьютером, индексация результата:
        # совпала первая кость
        if sw==2 and self.id_return == 0 \
                and (dice_game.dice_1 == dice_game._hidden_num_1 or dice_game.dice_1 == dice_game._hidden_num_2 \
                     or dice_game.dice_2 == dice_game._hidden_num_1 or dice_game.dice_2 == dice_game._hidden_num_2):
            self.id_return = 2
        if ((dice_game.dice_1 + dice_game.dice_2) == (dice_game._hidden_num_1 + dice_game._hidden_num_2)):
            self.id_return += 10
        if self.id_return == 0:
            return self.id_return


if __name__ == '__main__':
    game = Dice(3)
    print(type(game),game)
    game_type_1 = Dice_type_1(1)
    print(type(game_type_1),game_type_1)
    game_type_2 = Dice_type_2(2)
    print(type(game_type_2),game_type_2)