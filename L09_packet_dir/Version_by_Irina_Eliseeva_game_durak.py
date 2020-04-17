#Ирина Елисеева • Ср 12 Фев 01:55 • Ответ создан Вт 11 Фев 17:46
#https://github.com/EliseevaIN/python_lesson_9/blob/master/play_durak.py
#
import copy
import random


class Durak:
    def __init__(self):
        self.bito = []
        self.koloda = []

    def all_cards(self):
        self.card_type = [['6', 1], ['7', 2], ['8', 3], ['9', 4], ['10', 5], ['J', 6], ['Q', 7], ['K', 8], ['A', 9]]

        self.spades = copy.deepcopy(self.card_type)
        for i in range(len(self.spades)):
            self.spades[i][0] = self.spades[i][0] + '_\u2660'

        self.club = copy.deepcopy(self.card_type)
        for i in range(len(self.club)):
            self.club[i][0] = self.club[i][0] + '_\u2663'

        self.hearts = copy.deepcopy(self.card_type)
        for i in range(len(self.hearts)):
            self.hearts[i][0] = self.hearts[i][0] + '_\u2665'

        self.diamonds = copy.deepcopy(self.card_type)
        for i in range(len(self.diamonds)):
            self.diamonds[i][0] = self.diamonds[i][0] + '_\u2666'

        self.cards = self.spades + self.club + self.hearts + self.diamonds
        random.shuffle(self.cards)
        return self.cards

    def gen_cards(self):

        self.player_cards = []
        for card in range(6):
            player_card = random.choice(self.cards)
            self.player_cards.append(player_card)
            self.cards.remove(player_card)

        self.comp_cards = []
        for card in range(6):
            comp_card = random.choice(self.cards)
            self.comp_cards.append(comp_card)
            self.cards.remove(comp_card)

        return print('Ваши карты: ', list((item[0] for item in self.player_cards))), print('Карты компьютера: ', list(
            (item[0] for item in self.comp_cards))), print('Козырь: ', self.get_mast(Durak, self.kozyr[0]))

    def gen_kozyr_list(self):
        kozyr_card = random.choice(self.cards)
        self.kozyr = kozyr_card
        new_list = self.kozyr[0].rsplit('_')
        self.mast_kozyr = new_list[1]
        for card in self.cards:
            if self.mast_kozyr in card[0]:
                card[1] = card[1] + 9
        return self.cards

    def get_mast(self, card):
        new_list = card.rsplit('_')
        self.mast = new_list[1]
        return self.mast

    def whos_first_turn(self):
        player_smallest_card = min(item[1] for item in self.player_cards)
        comp_smallest_card = min(item[1] for item in self.comp_cards)
        if player_smallest_card < comp_smallest_card:
            self.turn = True
            self.player_turn(Durak)
        else:
            self.turn = False
            self.comp_turn(Durak)

    def game_start(self):
        self.table = []
        self.gen_kozyr_list(Durak)
        self.gen_cards(Durak)
        self.whos_first_turn(Durak)

    def comp_turn(self, comp_cards_to_win=None):
        if len(self.comp_cards) > 0 and len(self.player_cards) > 0 and self.turn == False and len(self.table) == 0:
            print('_____________ Ход компьютера _____________')
            tmp_card = random.choice(self.comp_cards)
            self.table.append(tmp_card)
            self.comp_cards.remove(tmp_card)
            print('На столе: ', self.table[0][0])
            self.player_turn(Durak)

        else:
            comp_cards_to_win = []
            changed_table = copy.deepcopy(self.table)
            for i in range(len(changed_table)):
                changed_table[i][0] = self.get_mast(Durak, changed_table[i][0])

            for i in range(len(self.comp_cards)):
                if (self.get_mast(Durak, self.comp_cards[i][0]) == changed_table[0][0] or self.get_mast(Durak,
                                                                                                        self.comp_cards[i][0]) == self.mast_kozyr) and \
                        self.comp_cards[i][1] > changed_table[0][1] and len(self.table) == 1:
                    comp_cards_to_win.append(self.comp_cards[i])

            if len(comp_cards_to_win) > 0:
                self.beat_cards = []
                card_to_beat = random.choice(comp_cards_to_win)
                self.beat_cards.append(card_to_beat)
                self.comp_cards.remove(card_to_beat)
                print('Отбито картой:  ', self.beat_cards[0][0])
                self.table.clear()
                self.turn = False
                self.comp_turn(Durak)

            else:
                print('Компьютер берет карту ')
                self.comp_cards.append(self.table[0])
                self.table.remove(self.table[0])
                self.turn = True
                self.player_turn(Durak)

    def player_turn(self):
        if len(self.comp_cards) > 0 and len(self.player_cards) > 0 and self.turn and len(self.table) == 0:
            print('_____________ Ваш ход _____________')
            print('Ваши карты:', list((item[0] for item in self.player_cards)))
            bool_card = ""
            while not bool_card:
                tmp_card = str(input('Сделайте ход: '))
                for card in self.player_cards:
                    if tmp_card == card[0]:
                        tmp_card = card
                        bool_card = tmp_card
                        self.table.append(tmp_card)
                        self.player_cards.remove(card)
                        print('Карты на столе: ', self.table[0][0])
                        print('Ваши карты: ', list((item[0] for item in self.player_cards))), \
                        print('Карты компьютера: ', list((item[0] for item in self.comp_cards)))
            self.turn = False
            self.comp_turn(Durak)

        elif len(self.player_cards) > 0 and self.turn == False and len(self.table) != 0:
            cards_to_win = []
            changed_table = copy.deepcopy(self.table)
            for i in range(len(changed_table)):
                changed_table[i][0] = self.get_mast(Durak, changed_table[i][0])

            for i in range(len(self.player_cards)):
                if (self.get_mast(Durak, self.player_cards[i][0]) == changed_table[0][0] or self.get_mast(Durak,
                                                                                                          self.player_cards[i][0]) == self.mast_kozyr) and \
                        self.player_cards[i][1] > changed_table[0][1] and len(self.table) == 1:
                    cards_to_win.append(self.player_cards[i])
            print('Карты в доступе: ', list((item[0] for item in cards_to_win)))

            if not cards_to_win and self.turn == False:
                self.beat_cards = []
                print('Вы берете карту')
                self.player_cards.append(self.table[0])
                self.table.clear()
                print('Ваши карты:', list((item[0] for item in self.player_cards)))
                self.comp_turn(Durak)
            else:
                bool_card = ""
                self.beat_cards = []
                while not bool_card:
                    input_data = input('Отбейте доступной картой:  ')
                    for i in range(len(cards_to_win)):
                        if input_data == cards_to_win[i][0]:
                            bool_card = cards_to_win[i]
                            self.beat_cards.append(cards_to_win[i])
                            self.player_cards.remove(cards_to_win[i])
                            print('Отбито картой:  ', self.beat_cards[0][0])
                            self.table.clear()
                            cards_to_win.clear()
                            break
                self.turn = True
                self.player_turn(Durak)

Durak.all_cards(Durak)
Durak.game_start(Durak)