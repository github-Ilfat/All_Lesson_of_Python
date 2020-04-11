print('# *************************************************************************************************************')
#!python3.6
#coding: utf8
class Card:
    def __init__(self,value,suit):
        self.value = value
        self.suit = '♥♦♣♠'[suit-1] # 1,2,3,4 = ♥♦♣♠

    def print(self):
        print('┌───────┐')
        print(f'| {self.value:<2}    |')
        print('|       |')
        print(f'|   {self.suit}   |')
        print('|       |')
        print(f'|    {self.value:>2} |')
        print('└───────┘')

x=Card('10',2)
x.print()
print('# *************************************************************************************************************')
print()
print()
print('# *************************************************************************************************************')
Card_deck=[]
card=['6','7','8','9','10','V','D','K','T']
#крести chr(167), буби chr(168), черви chr(169), пики chr(170)
#suit=[chr(167),chr(168),chr(169),chr(170)]
#suit=['-крст', '-буби','-чрв', '-пики']
suit=['♣','♦','♥','♠']
# заполнение списка - колоды карт
for c in range(9):
    for m in range(4):
        Card_deck.append(str(card[c]) + str(suit[m]))
print(Card_deck)
#Crd_dck = set_Card_deck()
#random.shuffle(Crd_dck)
#print(Crd_dck)
#random_number = random.choice(Crd_dck)
#print(Crd_dck)
print('# *************************************************************************************************************')
print()
print()
print('# *************************************************************************************************************')
'''
for i in range(32,255):
    print("%4d-%s" % (i,chr(i)), end='')
    if i%10 == 0:
        print()

print()
'''
print('# *************************************************************************************************************')
import random

class Game_Fool:
    # Инициалицирующий МЕТОД (специальный метод с "__")
    # Инициализация атрибутов игры (N - количество бросков "throw_num" )
    def __init__(self):
        # Поля читаются и записываются через "self" - указывает на текущий экземпляр класса
        # крести chr(167), буби chr(168), черви chr(169), пики chr(170)
        self.suit=['♣','♦','♥','♠']
        self.card=['6','7','8','9','10','V','D','K','T']
        self.Card_deck = [] # Колода карт
        self.Trump_card = '' # козырная карта
#        self.Gamer_deck = Gmr_dck # карты игрока
#        self.Comp_desk = Cmp_dsk # карты компьютера
#        self.Broken_cards = Brkn_crds # битые карты

    # Обычный метод объекта(метод экземпляра класса),
    # имеет те же правила наименования, что и обычные функции:
    def set_Card_deck(self):
        # заполнение списка - колоды карт
        for c in range(0,9):
            self.card_tmp=self.card[c]
            for m in range(0,4):
                self.Card_deck.append(self.card_tmp + self.suit[m])
        random.shuffle(self.Card_deck)
        #print(self.Card_deck)
        self.Trump_card = random.choice(self.Card_deck)
        #print(self.Card_deck)

fool_game = Game_Fool() # запуск с указанием количества попыток
fool_game.set_Card_deck()
print(fool_game.Card_deck)
print(fool_game.Trump_card)
print('# *************************************************************************************************************')
print()
print()
print('# *************************************************************************************************************')
