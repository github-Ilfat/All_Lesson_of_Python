from dice_game import Dice


class Dice_type_1(Dice):
    def throw_dices(self):
        dice_1 = random.randint(1,6)
        dice_2 = random.randint(1,6)
        self.current_throw+=1
        if self.current_throw > self.throw_num:
            raise Exception('Вы превысили количество попыток!')

        if dice_1+dice_2 == self._hidden_num_1 + self._hidden_num_2:
            return True
        else:
            return False

class Dice_type_2(Dice):
    def throw_dices(self):
        dice_1 = random.randint(1,6)
        dice_2 = random.randint(1,6)
        self.current_throw+=1
        if self.current_throw > self.throw_num:
            raise Exception('Вы превысили количество попыток!')

        if (dice_1 in {self._hidden_num_1, self._hidden_num_2}) or (dice_2 in {self._hidden_num_1, self._hidden_num_2}):
            return True
        else:
            return False



if __name__ == '__main__':
    game = Dice(3)
    print(type(game))
    game_type_1 = Dice_type_1(5)
    print(type(game_type_1))
    game_type_2 = Dice_type_2(5)
    print(type(game_type_2))