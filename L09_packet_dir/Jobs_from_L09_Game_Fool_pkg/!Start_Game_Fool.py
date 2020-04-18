#!python3.7
#coding: utf-8
# Желательно настроить шрифт (File-Settings-Editor-Font) - Consolas, size:13, Line spacing:0.8

#
# START GAME                                 START GAME                                     START GAME
#                    START GAME                                      START GAME
#
# START GAME                                 START GAME                                     START GAME
#

from L09_packet_dir.Jobs_from_L09_Game_Fool_pkg.by_Aleksey_Vedyashkin_game_logic1_durak import Game_logic1_durak

r=''
mode=0
print('Демонстрационная игра в карточную игру "Дурак"')
print('Доступны 2 режим демонтстрации: с комментариями автора "y" логики или без "n" ')
while mode==0:
    user_change = input('\rПрошу выбрать режим демонтстрации:')
    if user_change=='y':
        mode=2
    if user_change=='n':
        mode=1

cards_game = Game_logic1_durak(25,mode)
cards_game.set_players_cards()
cards_game.turn_cards()