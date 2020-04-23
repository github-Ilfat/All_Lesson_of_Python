#!python3.7
#coding: utf-8
# Желательно настроить шрифт (File-Settings-Editor-Font) - Consolas, size:13, Line spacing:0.8

class Game_fool_card_desc:
    #------------------------------------------------------------------------------------------------------------------
    Label='\033[47m   -=СТОЛ КАРТОЧНОЙ ИГРЫ "В ДУРАКА"=-   \033[0m'
    for i in range(70): print('\033[31m*', end='')
    print(Label, end='')
    for i in range(70): print('\033[31m*', end='')
    print('*\033[0m')
    #------------------------------------------------------------------------------------------------------------------
    def __init__(self, name1, gmr1c, gmr1s, name2, gmr2c, gmr2s, dsc_c, dsc_s):
        self.card=[' ','§',' 6',' 7',' 8',' 9','10',' V',' D',' K',' T']
        self.suit=[' ','§','♣','\033[31m♦\033[0m','\033[31m♥\033[0m','♠']
        #self.suit=[' ','§','♣','♦','♥','♠']
        self.g1c = gmr1c
        self.g1s = gmr1s
        self.dc = dsc_c
        self.ds = dsc_s
        self.g2c = gmr2c
        self.g2s = gmr2s
        self.fg1=0
        self.fg2=0
        self.gmr_name1=name1
        self.gmr_name2=name2

    def blk_chk(self):
        if len(self.g1c)==len(self.g1s) and len(self.g2c)==len(self.g2s) and len(self.dc)==len(self.ds):
            self.chk_error = 0
        else: self.chk_error = 1
        self.action1=' '
        self.action2=' '
        if self.dc[5]!=0:
            self.action1='ходит!'
            self.action2='отбивает!'
        if self.ds[5]!=0:
            self.action1='отбивает!'
            self.action2='ходит!'

        if len(self.gmr_name1)>9:self.gmr_name1=self.gmr_name1[0:9]
        if len(self.gmr_name2)>9:self.gmr_name2=self.gmr_name2[0:9]

    def Dsc_img(self):
        # 3-ряда карт на столе,1-верхний(закрытые карты),2-средний(колода, козырь, бой, бита),3-нижний(открытые карты)
        for d in range(3):
            if d==0:
                self.nc=len(self.g1c) # количество карт игрока1 для отображения len(tcard)=len(tsuit)
                self.tc=self.g1c # num_card:[0,1,2,,,10] список иерархического имени карты игрока1
                self.ts=self.g1s # num_suit:[0,1,2,,,10] список масти карты игрока1
            if d==1:
                # включение режима наложения карт - "карточный бой"
                if (self.dc[5]!=0 and self.ds[6]!=0) or (self.ds[5]!=0 and self.dc[6]!=0):
                    del self.ds[0]
                    self.ds.insert(0,1) # флаг включения режима
                self.nc=len(self.dc) # количество карт компьютера для отображения len(tcard)=len(tsuit)
                self.tc=self.dc # num_card:[0,1,2,,,10] список иерархического имени козыря, изображение колоды, боя и биты
                self.ts=self.ds # num_suit:[0,1,2,,,5] список масти козыря, изображение колоды, боя и биты
            if d==2:
                self.nc=len(self.g2c) # количество карт игрока2 для отображения len(tcard)=len(tsuit)
                self.tc=self.g2c # num_card:[0,1,2,,,10] список иерархического имени карты игрока2
                self.ts=self.g2s # num_suit:[0,1,2,,,5] список масти карты игрока2
            self.img=[]
            self.line_img=[]
            self.line_img_buffer=''
            l=0
            # здесь n - номер по счёту, включая пустые позиции изображения карт, в одном ряду
            for n in range(0, self.nc):
                if d==1:
                    if n>5:
                        n>5
                    self.fg1=0
                    self.fg2=0
                    self.cn =0
                    self.sn =0
                    if n>4 and n<(len(self.dc)-2):
                        if self.dc[n]!=0:
                            self.fg1=1
                            self.nc=len(self.g1c) # количество карт игрока1 для отображения len(tcard)=len(tsuit)
                            self.tc=self.g1c # num_card:[0,1,2,,,10]lst иерархического имени карты игрока1
                            self.ts=self.g1s # num_suit:[0,1,2,,,10]lst масти карты игрока1
                            self.cn = self.tc[self.dc[n]] # изъятие указателя на порядковый № в списке имён
                            self.sn = self.ts[self.dc[n]] # изъятие указателя на порядковый № в списке матей
                            c = self.card[self.cn] # получение символа имени карты из текстового списка имён
                            s = self.suit[self.sn] # получение символа масти карты из текстового списка мастей
                        if self.ds[n]!=0:
                            self.fg2=1
                            self.nc=len(self.g2c) # количество карт игрока2 для отображения len(tcard)=len(tsuit)
                            self.tc=self.g2c # num_card:[0,1,2,,,10]lst иерархического имени карты игрока2
                            self.ts=self.g2s # num_suit:[0,1,2,,,5]lst масти карты игрока2
                            self.cn = self.tc[self.ds[n]] # изъятие указателя на порядковый № в списке имён
                            self.sn = self.ts[self.ds[n]] # изъятие указателя на порядковый № в списке матей
                            c = self.card[self.cn] # получение символа имени карты из текстового списка имён
                            s = self.suit[self.sn] # получение символа масти карты из текстового списка мастей
                    if (n<=4 or n>=(len(self.dc)-2)):
                        self.nc=len(self.dc) # количество карт компьютера для отображения len(tcard)=len(tsuit)
                        self.tc=self.dc # num_card:[0,1,,,10]lst иерархического имени козыря, изобр. колоды, боя и биты
                        self.ts=self.ds # num_suit:[0,1,,,5]lst масти козыря, изображение колоды, боя и биты
                        self.cn = self.tc[n] # изъятие указателя на порядковый № в списке имён
                        self.sn = self.ts[n] # изъятие указателя на порядковый № в списке матей
                        if self.cn==1: self.sn=1
                        c = self.card[self.cn] # получение символа имени карты из текстового списка имён
                        s = self.suit[self.sn] # получение символа масти карты из текстового списка мастей
                if d!=1:
                    self.cn = self.tc[n] # изъятие указателя на порядковый № в списке имён
                    self.sn = self.ts[n] # изъятие указателя на порядковый № в списке матей
                    if self.cn==1: self.sn=1
                    c = self.card[self.cn] # получение символа имени карты из текстового списка имён
                    s = self.suit[self.sn] # получение символа масти карты из текстового списка мастей
                # все свободные позиции карт на столе
                if self.cn==0:
                    for i in range(9):
                        if n==0 and (i==3 or i==4 or i==5):
                            if d==0:
                                if i==3: self.img.insert(l+3,'\033[46m1 ИГРОК: \033[0m')
                                if i==4: self.img.insert(l+4,f'\033[46m{self.gmr_name1:<9}\033[0m')
                                if i==5: self.img.insert(l+5,f'\033[46m{self.action1:<9}\033[0m')
                            elif d==2:
                                if i==3: self.img.insert(l+3,'\033[42m2 ИГРОК: \033[0m')
                                if i==4: self.img.insert(l+4,f'\033[42m{self.gmr_name2:<9}\033[0m')
                                if i==5: self.img.insert(l+5,f'\033[42m{self.action2:<9}\033[0m')
                            else: self.img.insert(l+i,'         ')
                        elif d==1 and n==(len(self.ds)-1) and i==8:
                            self.img.insert(l+8,'\033[47m "Бито"  \033[0m')
                        else:
                            self.img.insert(l+8,'         ')
                    l+=9

                # все закрытые карты
                if self.cn==1:
                    self.img.insert(l+0,'         ')
                    self.img.insert(l+1,'┌───────┐')

                    if n==3 and d==1: s = (self.suit[self.ds[3]])
                    for i in range(2,7): self.img.insert(l+i,f'|{s+s+s+s+s+s+s}|')
                    self.img.insert(l+7,'└───────┘')

                    if n==1:
                        self.img.insert(l+8,'\033[47m"Калода" \033[0m')
                    elif n==(len(self.ds)-1):
                        self.img.insert(l+8,'\033[47m "Бито"  \033[0m')
                    else:
                        self.img.insert(l+8,'         ')
                    l+=9

                # все открытые карты
                #if self.cn in {2,3,4,5,6,7,8,9,10}:
                # все раздельно открытые карты
                if self.cn in {2,3,4,5,6,7,8,9,10} and (d!=1 \
                                                        or (d==1 and (n in {5,7,9,11,13,15}) and ((self.fg1==1 and self.ds[n+1]==0) or (self.fg2==1 and self.dc[n+1]==0))) \
                                                        or (d==1 and (n<=4 or n>=(len(self.dc)-2)))):
                    sh=0
                    if d==0:
                        self.fight=self.dc[5:len(self.dc)-2]
                    if d==2:
                        self.fight=self.ds[5:len(self.ds)-2]
                    if (d==0 or d==2) and n in self.fight[0:]:
                        sh=1
                    if sh==0:
                        if d==1 and n!=3:
                            if self.fg1==1:
                                self.img.insert(l+0,f'  \033[46m({(c + s)}\033[46m)\033[0m  ')
                            else:
                                self.img.insert(l+0,'         ')
                        else:
                            self.img.insert(l+0,'         ')
                        self.img.insert(l+1,'┌───────┐')
                        self.img.insert(l+2,f'| {s}     |')
                        self.img.insert(l+3,f'|{c}     |')
                        self.img.insert(l+4,'|       |')
                        self.img.insert(l+5,f'|     {c}|')
                        self.img.insert(l+6,f'|      {s}|')
                        self.img.insert(l+7,'└───────┘')
                        if d==1 and n==3: self.img.insert(l+8,f'\033[47m"Козырь{s}"\033[0m')
                        else:
                            if d==1 and n>4 and n<(len(self.dc)-2):
                                if self.fg2==1: self.img.insert(l+8,f'  \033[42m({(c + s)}\033[42m)\033[0m  ')
                                if self.fg2==0: self.img.insert(l+8,'         ')
                            elif d==0: self.img.insert(l+8,f'  \033[46m({(c + s)}\033[46m)\033[0m  ')
                            else:
                                self.img.insert(l+8,f'  \033[42m({(c + s)}\033[42m)\033[0m  ')

                    if sh==1:
                        if d==1 and n!=3:
                            if self.fg1==1:
                                self.img.insert(l+0,f'  \033[46m({(c + s)}\033[46m)\033[0m  ')
                            else:
                                self.img.insert(l+0,'         ')
                        else:
                            self.img.insert(l+0,'         ')
                        self.img.insert(l+1,'\033[36m┌───────┐\033[0m')
                        self.img.insert(l+2,f'\033[36m| {s}     \033[36m|\033[0m')
                        self.img.insert(l+3,f'\033[36m|{c}     \033[36m|\033[0m')
                        self.img.insert(l+4,'\033[36m|       |\033[0m')
                        self.img.insert(l+5,f'\033[36m|     {c}\033[36m|\033[0m')
                        self.img.insert(l+6,f'\033[36m|      {s}\033[36m|\033[0m')
                        self.img.insert(l+7,'\033[36m└───────┘\033[0m')
                        if d==1 and n==3: self.img.insert(l+8,f'\033[47m"Козырь!{s}"\033[0m')
                        else:
                            if d==1 and n>4 and n<(len(self.dc)-2):
                                if self.fg2==1: self.img.insert(l+8,f'  \033[42m({(c + s)}\033[42m)\033[0m  ')
                                if self.fg2==0: self.img.insert(l+8,'         ')
                            elif d==0: self.img.insert(l+8,f'  \033[46m({(c + s)}\033[46m)\033[0m  ')
                            else:
                                self.img.insert(l+8,f'  \033[42m({(c + s)}\033[42m)\033[0m  ')

                    l+=9

                # наложение открытых карт - "карточный бой"
                if d==1 and self.ds[0]==1 and n>4 and n<(len(self.dc)-2) and self.cn in {2,3,4,5,6,7,8,9,10}:
                    if n in {5,7,9,11,13,15}:
                        if (self.fg1==1 and self.ds[n+1]!=0) or (self.fg2==1 and self.dc[n+1]!=0):
                            self.img.insert(l+0,'     ┌───')
                            self.img.insert(l+1,f'     | {s} ')
                            self.img.insert(l+2,f'     |{c}┌')
                            self.img.insert(l+3,'     |  |')
                            self.img.insert(l+4,'     |  |')
                            self.img.insert(l+5,'     |  |')
                            self.img.insert(l+6,'     └──|')
                            self.img.insert(l+7,'        |')
                            self.img.insert(l+8,'        └')
                    if n in {6,8,10,12,14,16}:
                        if (self.fg1==1 and self.ds[n-1]!=0) or (self.fg2==1 and self.dc[n-1]!=0):
                            self.img.insert(l+0,'────┐    ')
                            self.img.insert(l+1,'    |    ')
                            self.img.insert(l+2,'───────┐ ')
                            self.img.insert(l+3,f'{c}     | ')
                            self.img.insert(l+4,f' {s}     | ')
                            self.img.insert(l+5,'       | ')
                            self.img.insert(l+6,f'      {s}| ')
                            self.img.insert(l+7,f'     {c}| ')
                            self.img.insert(l+8,'───────┘ ')
                    l+=9

            #---------------------------------------
            # Блок горизонтального вывода на экран
            for i in range(9):
                self.line_img_buffer=''
                for n in range(0, len(self.img), 9):
                    self.line_img_buffer+= self.img[i+n]
                    self.line_img.insert(i, self.line_img_buffer)
            if self.chk_error == 0:
                for i in range(9):
                    print(self.line_img[i])
        #--------------------------------------------------------------------------------------------------------------
        for i in range(179): print('\033[31m*', end='')
        print('*\033[0m')
        #--------------------------------------------------------------------------------------------------------------

#----------------------------------------------------------------------------------------------------------------------

# Пример вызова класса "Game_fool_card_desc"
'''
name1='' #──── имя игрока 1
name2='' #──── имя игрока 2

# id num_card: [' ','§','6','7','8','9','10','V','D','K','T'] (''-'Т')
# id num_card: [ 0 , 1 , 2 , 3 , 4 , 5 ,  6 , 7 , 8 , 9 , 10] (0 - 10)
# id num_suit: [' ','§','♣','♦','♥','♠'] (''-'♠')
# id num_suit: [ 0 , 1 , 2 , 3 , 4 , 5 ] (0 - 5 )
gmr1c = [0,0,0,0,0,0,0,0,0 возможно увеличеие  ] #──── ранг карты, игрока 1
gmr1s = [0,0,0,0,0,0,0,0,0 занимаемых картомест] #──── масть карты, игрока 1
#        | | |
#        | └─└── свободное картоместо    (с 1 по 3, список картомест игрока 1)
#        | 
#        └─ 'надпись "1 ИГРОК:"'
#        └─ '           "имя"'
#        └─ '         "действие"'

# [0,,,5] and [len-2,len-1] id num_card: [' ','§','6','7','8','9','10','V','D','K','T'] (''-'Т')
# [0,,,5] and [len-2,len-1] id num_card: [ 0 , 1 , 2 , 3 , 4 , 5 ,  6 , 7 , 8 , 9 , 10] (0 - 10)
# [0,,,5] and [len-2,len-1] id num_suit: [' ','§','♣','♦','♥','♠'] (''-'♠')
# [0,,,5] and [len-2,len-1] id num_suit: [ 0 , 1 , 2 , 3 , 4 , 5 ] (0 - 5 )
# [5,,,len-3] flaf_gamer_1 and address id num_card in gmr1c: ['0','1',,,,len(gmr1c)]
# [5,,,len-3] flaf_gamer_2 and address id num_card in gmr2c: ['0','1',,,,len(gmr2c)]

#          ┌─ место "Колоды" 
#          |   ┌─ место "Козыря             (с 5 по 15,все нечётные, если ходит, dsc_c адреса списка карт игрока 1)
#          |   |                            (с 6 по 16, все чётные, еслт отбивается, dsc_c адреса списка карт игрока 1) 
#          |   |     наличие ходов игроками       
#          |   |   ┌───────────────────────┐ ┌─ место "Биты"
dsc_c = [0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0] #──── ранг карты, для позиций с 1 по 4 и 18
dsc_s = [0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0] #──── масть карты, для позиций с 1 по 4 и 18 
#        0,1,2,3,4,5,6,7,8,9,1,1,1,1,1,1,1,1,1
#            |   |           0,1,2,3,4,5,6,7,8
#            |   |
#            └───└── свободное картоместо    (с 5 по 15,все нечётные, если ходит, dsc_s адреса списка карт игрока 2)
#                                            (с 6 по 16, все чётные, еслт отбивается, dsc_s адреса списка карт игрока 2)
                        
# id num_card: [' ','§','6','7','8','9','10','V','D','K','T'] (''-'Т')
# id num_card: [ 0 , 1 , 2 , 3 , 4 , 5 ,  6 , 7 , 8 , 9 , 10] (0 - 10)
# id num_suit: [' ','§','♣','♦','♥','♠'] (''-'♠')
# id num_suit: [ 0 , 1 , 2 , 3 , 4 , 5 ] (0 - 5 )
gmr2c = [0,0,0,0,0,0,0,0,0 возможно увеличеие  ] #──── ранг карты, игрока 2
gmr2s = [0,0,0,0,0,0,0,0,0 занимаемых картомест] #──── масть карты, игрока 2
#        0,1,2,3,4,5,6,7,8
#        | | |
#        | └─└── свободное картоместо    (с 1 по 3, список картомест игрока 2)
#        | 
#        └─ 'надпись "2 ИГРОК:"'
#        └─ '           "имя"'
#        └─ '         "действие"'

x=Game_fool_card_desc(name1, gmr1c, gmr1s, name2, gmr2c, gmr2s, dsc_c, dsc_s)
x.blk_chk()
x.Dsc_img()
'''



'''
from L09_packet_dir.Jobs_from_L09_Game_Fool_pkg import Game_fool_card_desc
#
#Алексей Ведяшкин • Вс 02 Фев 12:57 • Ответ создан Сб 01 Фев 01:00
#https://github.com/sdfxisme/lesson9/blob/master/cards.py
import random
class Game_logic1_durak:
    def __init__(self,N):
        self.turn_num = N

    def set_players_cards(self):
        self.list_coloda = [(6, 'c'), (7, 'c'), (8, 'c'), (9, 'c'), (10, 'c'), (11, 'c'), (12, 'c'), (13, 'c'), (14, 'c'),
                            (6, 'b'), (7, 'b'), (8, 'b'), (9, 'b'), (10, 'b'), (11, 'b'), (12, 'b'), (13, 'b'), (14, 'b'),
                            (6, 'k'), (7, 'k'), (8, 'k'), (9, 'k'), (10, 'k'), (11, 'k'), (12, 'k'), (13, 'k'), (14, 'k'),
                            (6, 'p'), (7, 'p'), (8, 'p'), (9, 'p'), (10, 'p'), (11, 'p'), (12, 'p'), (13, 'p'), (14, 'p')]
        list_cards_player_1 = []
        list_cards_player_2 = []
        for i in range(6):
            player_1_card = random.choice(self.list_coloda)
            list_cards_player_1.append(player_1_card)
            self.list_coloda.remove(player_1_card)
            player_2_card = random.choice(self.list_coloda)
            list_cards_player_2.append(player_2_card)
            self.list_coloda.remove(player_2_card)
        self.player_1_cards = list_cards_player_1
        self.player_2_cards = list_cards_player_2
        self.player_1_cards.sort()
        self.player_2_cards.sort()
        kozir_card = random.choice(self.list_coloda)
        self.kozir = kozir_card[1]
        random.shuffle(self.list_coloda)
        self.list_bito = []

        #--------------------------------------------------------------------------------------------------------------
        self.n1='Компьютер' #──── имя игрока 1
        self.n2='Компьютер' #──── имя игрока 2

        self.g1c = [0,0,0] #──── ранг карты, игрока 1
        self.g1s = [0,0,0] #──── масть карты, игрока 1
        self.d_c = [0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0] #──── ранг карты, для позиций с 1 по 4 и 18
        self.d_s = [0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0] #──── масть карты, для позиций с 1 по 4 и 18
        self.g2c = [0,0,0] #──── ранг карты, игрока 2
        self.g2s = [0,0,0] #──── масть карты, игрока 2
        for i in range(len(self.player_1_cards)):
            tuple_g1 = self.player_1_cards[i]
            tuple_g2 = self.player_2_cards[i]

            self.g1c.append(tuple_g1[0]-4)
            if tuple_g1[1] == 'c': self.g1s.append(4)
            if tuple_g1[1] == 'b': self.g1s.append(3)
            if tuple_g1[1] == 'k': self.g1s.append(2)
            if tuple_g1[1] == 'p': self.g1s.append(5)
            self.g2c.append(tuple_g2[0]-4)
            if tuple_g2[1] == 'c': self.g2s.append(4)
            if tuple_g2[1] == 'b': self.g2s.append(3)
            if tuple_g2[1] == 'k': self.g2s.append(2)
            if tuple_g2[1] == 'p': self.g2s.append(5)

        self.d_c.insert(3, 1) # козырь только масть
        if self.kozir == 'c': self.d_s.insert(3,4)
        if self.kozir == 'b': self.d_s.insert(3,3)
        if self.kozir == 'k': self.d_s.insert(3,2)
        if self.kozir == 'p': self.d_s.insert(3,5)
        name1=self.n1
        gmr1c=self.g1c
        gmr1s=self.g1s
        name2=self.n2
        gmr2c=self.g2c
        gmr2s=self.g2s
        dsc_c=self.d_c
        dsc_s=self.d_s
        cld_n=len(self.list_coloda)
        x=Game_fool_card_desc(name1, gmr1c, gmr1s, name2, gmr2c, gmr2s, dsc_c, dsc_s, cld_n)
        x.blk_chk()
        x.Dsc_img()
        #--------------------------------------------------------------------------------------------------------------
        print('карты 1-го игрока:', len(self.player_1_cards), self.player_1_cards,',')
        print('карты 2-го игрока:', len(self.player_2_cards), self.player_2_cards,',')
        print('карт в колоде:', len(self.list_coloda), 'козыри:', self.kozir)
        #--------------------------------------------------------------------------------------------------------------
        for i in range(179): print('\033[31m*', end='')
        print('*\033[0m')
        #--------------------------------------------------------------------------------------------------------------

    def bito(self,x,y):
        self.list_bito.append(x)
        self.list_bito.append(y)
        self.list_bito.sort()

    def dobor(self):
        if len(self.list_coloda) > 0 and len(self.player_1_cards) < 6:
            self.next_card = self.list_coloda[0]
            self.list_coloda.remove(self.next_card)
            self.player_1_cards.append(self.next_card)

            #----------------------------------------------------------------------------------------------------------
            tuple_g1 = self.next_card
            self.g1c.append(tuple_g1[0]-4)
            if tuple_g1[1] == 'c': self.g1s.append(4)
            if tuple_g1[1] == 'b': self.g1s.append(3)
            if tuple_g1[1] == 'k': self.g1s.append(2)
            if tuple_g1[1] == 'p': self.g1s.append(5)
            #----------------------------------------------------------------------------------------------------------
            name1=self.n1
            gmr1c=self.g1c
            gmr1s=self.g1s
            name2=self.n2
            gmr2c=self.g2c
            gmr2s=self.g2s
            dsc_c=self.d_c
            dsc_s=self.d_s
            cld_n=len(self.list_coloda)
            x=Game_fool_card_desc(name1, gmr1c, gmr1s, name2, gmr2c, gmr2s, dsc_c, dsc_s, cld_n)
            x.blk_chk()
            x.Dsc_img()
            #----------------------------------------------------------------------------------------------------------

            #------------------------------------------------------------------------------------------------------------
            print('первый игрок взял карту из колоды {}, в колоде {} карт'.format(self.next_card, len(self.list_coloda)))
            #----------------------------------------------------------------------------------------------------------
            for i in range(179): print('\033[31m*', end='')
            print('*\033[0m')
            #----------------------------------------------------------------------------------------------------------


        if len(self.list_coloda) > 0 and len(self.player_2_cards) < 6:
            self.next_card = self.list_coloda[0]
            self.list_coloda.remove(self.next_card)
            self.player_2_cards.append(self.next_card)

            #----------------------------------------------------------------------------------------------------------
            tuple_g2 = self.next_card
            self.g2c.append(tuple_g2[0]-4)
            if tuple_g2[1] == 'c': self.g2s.append(4)
            if tuple_g2[1] == 'b': self.g2s.append(3)
            if tuple_g2[1] == 'k': self.g2s.append(2)
            if tuple_g2[1] == 'p': self.g2s.append(5)
            #----------------------------------------------------------------------------------------------------------
            name1=self.n1
            gmr1c=self.g1c
            gmr1s=self.g1s
            name2=self.n2
            gmr2c=self.g2c
            gmr2s=self.g2s
            dsc_c=self.d_c
            dsc_s=self.d_s
            cld_n=len(self.list_coloda)
            x=Game_fool_card_desc(name1, gmr1c, gmr1s, name2, gmr2c, gmr2s, dsc_c, dsc_s, cld_n)
            x.blk_chk()
            x.Dsc_img()
            #----------------------------------------------------------------------------------------------------------

            #------------------------------------------------------------------------------------------------------------
            print('второй игрок взял карту из колоды {}, в колоде {} карт'.format(self.next_card, len(self.list_coloda)))
            #------------------------------------------------------------------------------------------------------------
            for i in range(179): print('\033[31m*', end='')
            print('*\033[0m')
            #----------------------------------------------------------------------------------------------------------


        self.player_1_cards.sort()
        self.player_2_cards.sort()
        self.turn_cards_player_1_not_kozir = [x for x in self.player_1_cards if x[1] != self.kozir]
        self.turn_cards_player_1_not_kozir.sort()
        self.turn_cards_player_1_kozir = [x for x in self.player_1_cards if x[1] == self.kozir]
        self.turn_cards_player_1_kozir.sort()
        self.turn_cards_player_2_not_kozir = [x for x in self.player_2_cards if x[1] != self.kozir]
        self.turn_cards_player_2_not_kozir.sort()
        self.turn_cards_player_2_kozir = [x for x in self.player_2_cards if x[1] == self.kozir]
        self.turn_cards_player_2_kozir.sort()

    def turn_cards(self):
        w = 0
        for i in range(1,self.turn_num):
            if w == 0:
                self.dobor()
                if len(self.turn_cards_player_1_not_kozir)>0 :
                    turn_cards_player_1 = self.turn_cards_player_1_not_kozir[0]
                else:
                    turn_cards_player_1 = self.turn_cards_player_1_kozir[0]
                turn_cards_player_1_suit = turn_cards_player_1[1]
                turn_cards_player_1_digit = turn_cards_player_1[0]


                #------------------------------------------------------------------------------------------------------
                tuple_g1=()
                for m in range(len(self.g1c)):
                    if self.g1s[m]==4: tuple_g1 =(self.g1c[m]+4, 'c')
                    if self.g1s[m]==3: tuple_g1 =(self.g1c[m]+4, 'b')
                    if self.g1s[m]==2: tuple_g1 =(self.g1c[m]+4, 'k')
                    if self.g1s[m]==5: tuple_g1 =(self.g1c[m]+4, 'p')
                    if  tuple_g1 == turn_cards_player_1:
                        self.ln_d=len(self.d_c)-2
                        for p in range(5,self.ln_d):
                            if self.d_c[p] ==0 and self.d_s[p] ==0:
                                del self.d_c[p]
                                self.d_c.insert(p,m)
                                name1=self.n1
                                gmr1c=self.g1c
                                gmr1s=self.g1s
                                name2=self.n2
                                gmr2c=self.g2c
                                gmr2s=self.g2s
                                dsc_c=self.d_c
                                dsc_s=self.d_s
                                cld_n=len(self.list_coloda)
                                x=Game_fool_card_desc(name1, gmr1c, gmr1s, name2, gmr2c, gmr2s, dsc_c, dsc_s, cld_n)
                                x.blk_chk()
                                x.Dsc_img()
                                break
                        break
                #------------------------------------------------------------------------------------------------------

                #------------------------------------------------------------------------------------------------------
                print('ход первого игрока:', turn_cards_player_1)
                #------------------------------------------------------------------------------------------------------
                for i in range(179): print('\033[31m*', end='')
                print('*\033[0m')
                #------------------------------------------------------------------------------------------------------


                list_cards_player_2_suit = [x for x in self.player_2_cards if x[1] == turn_cards_player_1_suit]
                list_cards_player_2_suit_higher = [x for x in list_cards_player_2_suit if x[0] > turn_cards_player_1_digit]
                if len(list_cards_player_2_suit_higher) + len(self.turn_cards_player_2_kozir) == 0:
                    self.player_2_cards.append(turn_cards_player_1)



                #------------------------------------------------------------------------------------------------------
                    self.ln_d=len(self.d_s)-1
                    for m in range(5,self.ln_d):
                        if self.d_c[m]!=0:
                            self.g2c.append(self.g1c[self.d_c[m]])
                            self.g2s.append(self.g1s[self.d_c[m]])
                            del self.g1c[self.d_c[m]]
                            del self.g1s[self.d_c[m]]
                            del self.d_c[m]
                            del self.d_s[m]
                            self.d_c.insert(m,0)
                            self.d_s.insert(m,0)
                            m=5
                    name1=self.n1
                    gmr1c=self.g1c
                    gmr1s=self.g1s
                    name2=self.n2
                    gmr2c=self.g2c
                    gmr2s=self.g2s
                    dsc_c=self.d_c
                    dsc_s=self.d_s
                    cld_n=len(self.list_coloda)
                    x=Game_fool_card_desc(name1, gmr1c, gmr1s, name2, gmr2c, gmr2s, dsc_c, dsc_s, cld_n)
                    x.blk_chk()
                    x.Dsc_img()
                    #--------------------------------------------------------------------------------------------------

                    #--------------------------------------------------------------------------------------------------
                    print('второй игрок взял')
                    #--------------------------------------------------------------------------------------------------
                    for i in range(179): print('\033[31m*', end='')
                    print('*\033[0m')
                    #--------------------------------------------------------------------------------------------------


                    self.player_1_cards.remove(turn_cards_player_1)
                    self.dobor()
                    w = 0
                elif turn_cards_player_1_suit == self.kozir and turn_cards_player_1[0] > self.turn_cards_player_2_kozir[-1][0]:
                    self.player_2_cards.append(turn_cards_player_1)


                    #--------------------------------------------------------------------------------------------------
                    self.ln_d=len(self.d_s)-1
                    for m in range(5,self.ln_d):
                        if self.d_c[m]!=0:
                            self.g2c.append(self.g1c[self.d_c[m]])
                            self.g2s.append(self.g1s[self.d_c[m]])
                            del self.g1c[self.d_c[m]]
                            del self.g1s[self.d_c[m]]
                            del self.d_c[m]
                            del self.d_s[m]
                            self.d_c.insert(m,0)
                            self.d_s.insert(m,0)
                            m=5
                    name1=self.n1
                    gmr1c=self.g1c
                    gmr1s=self.g1s
                    name2=self.n2
                    gmr2c=self.g2c
                    gmr2s=self.g2s
                    dsc_c=self.d_c
                    dsc_s=self.d_s
                    cld_n=len(self.list_coloda)
                    x=Game_fool_card_desc(name1, gmr1c, gmr1s, name2, gmr2c, gmr2s, dsc_c, dsc_s, cld_n)
                    x.blk_chk()
                    x.Dsc_img()
                    #--------------------------------------------------------------------------------------------------

                    #--------------------------------------------------------------------------------------------------
                    print('второй игрок взял')
                    print()

                    self.player_1_cards.remove(turn_cards_player_1)
                    self.dobor()
                    w = 0
                elif turn_cards_player_1_suit == self.kozir and turn_cards_player_1[0] < self.turn_cards_player_2_kozir[-1][0]:
                    #print('ход второго игрока:', self.turn_cards_player_2_kozir[-1])


                    #---2020_04_17-----------------------------------------------
                    print('введите номер козырной карты: 0,1,2,3,4....')  # self.turn_cards_player_2_kozir[-1]
                    print()
                    #self.m = 7
                    self.m = len(self.turn_cards_player_2_kozir)-1
                    if self.m > (len(self.turn_cards_player_2_kozir)):
                        #turn_cards_player_2 = self.turn_cards_player_2_kozir[self.m]
                        turn_cards_player_2 = self.turn_cards_player_2_kozir[-1]
                        #raise Exception (ValueError)
                    elif self.m <= (len(self.turn_cards_player_2_kozir) - 1):
                        print('ok, играем без смены козырей')
                        #----------------------------------------------------------------------------------------------
                        for i in range(179): print('\033[31m*', end='')
                        print('*\033[0m')
                        #----------------------------------------------------------------------------------------------
                        turn_cards_player_2 = self.turn_cards_player_2_kozir[self.m]
                    #---2020_04_17-----------------------------------------------

                    #--------------------------------------------------------------------------------------------------
                    tuple_g2=()
                    for m in range(len(self.g2c)):
                        if self.g2s[m]==4: tuple_g2 =(self.g2c[m]+4, 'c')
                        if self.g2s[m]==3: tuple_g2 =(self.g2c[m]+4, 'b')
                        if self.g2s[m]==2: tuple_g2 =(self.g2c[m]+4, 'k')
                        if self.g2s[m]==5: tuple_g2 =(self.g2c[m]+4, 'p')
                        if turn_cards_player_2 == tuple_g2:
                            for p in range(5,len(self.d_s)-1):
                                if self.d_c[p] ==0 and self.d_s[p] ==0:
                                    del self.d_s[p]
                                    self.d_s.insert(p,m)
                                    name1=self.n1
                                    gmr1c=self.g1c
                                    gmr1s=self.g1s
                                    name2=self.n2
                                    gmr2c=self.g2c
                                    gmr2s=self.g2s
                                    dsc_c=self.d_c
                                    dsc_s=self.d_s
                                    cld_n=len(self.list_coloda)
                                    x=Game_fool_card_desc(name1, gmr1c, gmr1s, name2, gmr2c, gmr2s, dsc_c, dsc_s, cld_n)
                                    x.blk_chk()
                                    x.Dsc_img()
                                    break
                            break
                    #--------------------------------------------------------------------------------------------------
                    print('ход второго игрока:', turn_cards_player_2)
                    #--------------------------------------------------------------------------------------------------
                    for i in range(179): print('\033[31m*', end='')
                    print('*\033[0m')
                    #--------------------------------------------------------------------------------------------------

                    self.player_1_cards.remove(turn_cards_player_1)
                    self.player_2_cards.remove(turn_cards_player_2)
                    self.bito(turn_cards_player_1,turn_cards_player_2)

                    #--------------------------------------------------------------------------------------------------
                    bito_g1=[]
                    bito_g2=[]
                    self.ln_d=len(self.d_c)-2
                    for m in range(self.ln_d,4,-1):
                        if self.d_c[m]!=0:
                            bito_g1.append(self.d_c[m])
                            del self.d_c[m]
                            self.d_c.insert(m,0)
                        if self.d_s[m]!=0:
                            bito_g2.append(self.d_s[m])
                            del self.d_s[m]
                            self.d_s.insert(m,0)
                    self.ln_d=len(bito_g1)
                    for m in range(self.ln_d):
                        del self.g1c[bito_g1[m]]
                        del self.g1s[bito_g1[m]]
                        if bito_g1[m]==2:
                            self.g1c.insert(2,0)
                            self.g1s.insert(2,0)
                    self.ln_d=len(bito_g2)
                    for m in range(self.ln_d):
                        del self.g2c[bito_g2[m]]
                        del self.g2s[bito_g2[m]]
                        if bito_g2[m]==2:
                            self.g2c.insert(2,0)
                            self.g2s.insert(2,0)
    
                    self.ln_d=(len(self.d_c)-1)
                    del self.d_c[self.ln_d]
                    del self.d_s[self.ln_d]
                    self.d_c.append(1)
                    self.d_s.append(1)
    
                    name1=self.n1
                    gmr1c=self.g1c
                    gmr1s=self.g1s
                    name2=self.n2
                    gmr2c=self.g2c
                    gmr2s=self.g2s
                    dsc_c=self.d_c
                    dsc_s=self.d_s
                    cld_n=len(self.list_coloda)
                    x=Game_fool_card_desc(name1, gmr1c, gmr1s, name2, gmr2c, gmr2s, dsc_c, dsc_s, cld_n)
                    x.blk_chk()
                    x.Dsc_img()
                    #--------------------------------------------------------------------------------------------------
                    print('бито')
                    #--------------------------------------------------------------------------------------------------
                    for i in range(179): print('\033[31m*', end='')
                    print('*\033[0m')
                    #--------------------------------------------------------------------------------------------------
                    self.dobor()
                    w = 1
                elif len(list_cards_player_2_suit_higher) == 0 and len(self.turn_cards_player_2_kozir) > 0:


                    #--------------------------------------------------------------------------------------------------
                    tuple_g2=()
                    for m in range(len(self.g2c)):
                        if self.g2s[m]==4: tuple_g2 =(self.g2c[m]+4, 'c')
                        if self.g2s[m]==3: tuple_g2 =(self.g2c[m]+4, 'b')
                        if self.g2s[m]==2: tuple_g2 =(self.g2c[m]+4, 'k')
                        if self.g2s[m]==5: tuple_g2 =(self.g2c[m]+4, 'p')
                        if self.turn_cards_player_2_kozir[0] == tuple_g2:
                            for p in range(5,len(self.d_s)-1):
                                if self.d_c[p] ==0 and self.d_s[p] ==0:
                                    del self.d_s[p]
                                    self.d_s.insert(p,m)
                                    name1=self.n1
                                    gmr1c=self.g1c
                                    gmr1s=self.g1s
                                    name2=self.n2
                                    gmr2c=self.g2c
                                    gmr2s=self.g2s
                                    dsc_c=self.d_c
                                    dsc_s=self.d_s
                                    cld_n=len(self.list_coloda)
                                    x=Game_fool_card_desc(name1, gmr1c, gmr1s, name2, gmr2c, gmr2s, dsc_c, dsc_s, cld_n)
                                    x.blk_chk()
                                    x.Dsc_img()
                                    break
                            break
                    #--------------------------------------------------------------------------------------------------
                    print('ход второго игрока:', self.turn_cards_player_2_kozir[0])
                    #--------------------------------------------------------------------------------------------------
                    for i in range(179): print('\033[31m*', end='')
                    print('*\033[0m')
                    #--------------------------------------------------------------------------------------------------

                    turn_cards_player_2 = self.turn_cards_player_2_kozir[0]
                    self.player_1_cards.remove(turn_cards_player_1)
                    self.player_2_cards.remove(turn_cards_player_2)
                    self.bito(turn_cards_player_1, turn_cards_player_2)


                    #--------------------------------------------------------------------------------------------------
                    bito_g1=[]
                    bito_g2=[]
                    self.ln_d=len(self.d_c)-2
                    # удаляется метка картоместа изображения "боя"
                    for m in range(self.ln_d,4,-1):
                        if self.d_c[m]!=0:
                            bito_g1.append(self.d_c[m])
                            del self.d_c[m]
                            self.d_c.insert(m,0)
                        if self.d_s[m]!=0:
                            bito_g2.append(self.d_s[m])
                            del self.d_s[m]
                            self.d_s.insert(m,0)
                    #---------------------------------------------
                    self.ln_d=len(bito_g1)
                    if self.ln_d!=0:
                        for m in range(self.ln_d):
                            del self.g1c[bito_g1[m]]
                            del self.g1s[bito_g1[m]]
                            if bito_g1[m]==2:
                                self.g1c.insert(2,0)
                                self.g1s.insert(2,0)
                    self.ln_d=len(bito_g2)
                    for m in range(self.ln_d):
                        del self.g2c[bito_g2[m]]
                        del self.g2s[bito_g2[m]]
                        if bito_g2[m]==2:
                            self.g2c.insert(2,0)
                            self.g2s.insert(2,0)

                    # ---- удаляется и устанавливается метка картоместа изображения "бито"
                    self.ln_d=(len(self.d_c)-1)
                    del self.d_c[self.ln_d]
                    del self.d_s[self.ln_d]
                    self.d_c.append(1)
                    self.d_s.append(1)
                    #---------------------------------------------------------------------
                    name1=self.n1
                    gmr1c=self.g1c
                    gmr1s=self.g1s
                    name2=self.n2
                    gmr2c=self.g2c
                    gmr2s=self.g2s
                    dsc_c=self.d_c
                    dsc_s=self.d_s
                    cld_n=len(self.list_coloda)
                    x=Game_fool_card_desc(name1, gmr1c, gmr1s, name2, gmr2c, gmr2s, dsc_c, dsc_s, cld_n)
                    x.blk_chk()
                    x.Dsc_img()
                    #--------------------------------------------------------------------------------------------------
                    print('бито')
                    #--------------------------------------------------------------------------------------------------
                    for i in range(179): print('\033[31m*', end='')
                    print('*\033[0m')
                    #--------------------------------------------------------------------------------------------------


                    self.dobor()
                    w = 1
                else:


                    #--------------------------------------------------------------------------------------------------
                    tuple_g2=()
                    for m in range(len(self.g2c)):
                        if self.g2s[m]==4: tuple_g2 =(self.g2c[m]+4, 'c')
                        if self.g2s[m]==3: tuple_g2 =(self.g2c[m]+4, 'b')
                        if self.g2s[m]==2: tuple_g2 =(self.g2c[m]+4, 'k')
                        if self.g2s[m]==5: tuple_g2 =(self.g2c[m]+4, 'p')
                        if list_cards_player_2_suit_higher[0] == tuple_g2:
                            for p in range(5,len(self.d_s)-1):
                                if self.d_c[p] ==0 and self.d_s[p] ==0:
                                    del self.d_s[p]
                                    self.d_s.insert(p,m)
                                    name1=self.n1
                                    gmr1c=self.g1c
                                    gmr1s=self.g1s
                                    name2=self.n2
                                    gmr2c=self.g2c
                                    gmr2s=self.g2s
                                    dsc_c=self.d_c
                                    dsc_s=self.d_s
                                    cld_n=len(self.list_coloda)
                                    x=Game_fool_card_desc(name1, gmr1c, gmr1s, name2, gmr2c, gmr2s, dsc_c, dsc_s, cld_n)
                                    x.blk_chk()
                                    x.Dsc_img()
                                    break
                            break
                    #--------------------------------------------------------------------------------------------------
                    print('ход второго игрока:', list_cards_player_2_suit_higher[0])
                    #--------------------------------------------------------------------------------------------------
                    for i in range(179): print('\033[31m*', end='')
                    print('*\033[0m')
                    #--------------------------------------------------------------------------------------------------




                    turn_cards_player_2 = list_cards_player_2_suit_higher[0]
                    self.player_1_cards.remove(turn_cards_player_1)
                    self.player_2_cards.remove(turn_cards_player_2)
                    self.bito(turn_cards_player_1, turn_cards_player_2)



                    #--------------------------------------------------------------------------------------------------
                    bito_g1=[]
                    bito_g2=[]
                    self.ln_d=len(self.d_c)-2
                    for m in range(self.ln_d,4,-1):
                        if self.d_c[m]!=0:
                            bito_g1.append(self.d_c[m])
                            del self.d_c[m]
                            self.d_c.insert(m,0)
                        if self.d_s[m]!=0:
                            bito_g2.append(self.d_s[m])
                            del self.d_s[m]
                            self.d_s.insert(m,0)
                    self.ln_d=len(bito_g1)
                    if self.ln_d!=0:
                        for m in range(self.ln_d):
                            del self.g1c[bito_g1[m]]
                            del self.g1s[bito_g1[m]]
                            if bito_g1[m]==2:
                                self.g1c.insert(2,0)
                                self.g1s.insert(2,0)
                    self.ln_d=len(bito_g2)
                    for m in range(self.ln_d):
                        del self.g2c[bito_g2[m]]
                        del self.g2s[bito_g2[m]]
                        if bito_g2[m]==2:
                            self.g2c.insert(2,0)
                            self.g2s.insert(2,0)

                    self.ln_d=(len(self.d_c)-1)
                    del self.d_c[self.ln_d]
                    del self.d_s[self.ln_d]
                    self.d_c.append(1)
                    self.d_s.append(1)
        
                    name1=self.n1
                    gmr1c=self.g1c
                    gmr1s=self.g1s
                    name2=self.n2
                    gmr2c=self.g2c
                    gmr2s=self.g2s
                    dsc_c=self.d_c
                    dsc_s=self.d_s
                    cld_n=len(self.list_coloda)
                    x=Game_fool_card_desc(name1, gmr1c, gmr1s, name2, gmr2c, gmr2s, dsc_c, dsc_s, cld_n)
                    x.blk_chk()
                    x.Dsc_img()
                    #--------------------------------------------------------------------------------------------------
                    print('бито')
                    #--------------------------------------------------------------------------------------------------
                    for i in range(179): print('\033[31m*', end='')
                    print('*\033[0m')
                    #--------------------------------------------------------------------------------------------------



                    self.dobor()
                    w = 1



                print('карты 1-го игрока после {} хода:'.format(i), len(self.player_1_cards), self.player_1_cards)
                print('карты 2-го игрока после {} хода:'.format(i), len(self.player_2_cards), self.player_2_cards)
                #------------------------------------------------------------------------------------------------------
                for i in range(179): print('\033[31m*', end='')
                print('*\033[0m')
                #------------------------------------------------------------------------------------------------------

            if w == 1:
                self.dobor()
                if len(self.turn_cards_player_2_not_kozir)>0 :
                    turn_cards_player_2 = self.turn_cards_player_2_not_kozir[0]
                else:
                    turn_cards_player_2 = self.turn_cards_player_2_kozir[0]
                turn_cards_player_2_suit = turn_cards_player_2[1]
                turn_cards_player_2_digit = turn_cards_player_2[0]


                #------------------------------------------------------------------------------------------------------
                tuple_g2=()
                for m in range(len(self.g2c)):
                    if self.g2s[m]==4: tuple_g2 =(self.g2c[m]+4, 'c')
                    if self.g2s[m]==3: tuple_g2 =(self.g2c[m]+4, 'b')
                    if self.g2s[m]==2: tuple_g2 =(self.g2c[m]+4, 'k')
                    if self.g2s[m]==5: tuple_g2 =(self.g2c[m]+4, 'p')
                    if turn_cards_player_2 == tuple_g2:
                        for p in range(5,len(self.d_s)-1):
                            if self.d_c[p] ==0 and self.d_s[p] ==0:
                                del self.d_s[p]
                                self.d_s.insert(p,m)
                                name1=self.n1
                                gmr1c=self.g1c
                                gmr1s=self.g1s
                                name2=self.n2
                                gmr2c=self.g2c
                                gmr2s=self.g2s
                                dsc_c=self.d_c
                                dsc_s=self.d_s
                                cld_n=len(self.list_coloda)
                                x=Game_fool_card_desc(name1, gmr1c, gmr1s, name2, gmr2c, gmr2s, dsc_c, dsc_s, cld_n)
                                x.blk_chk()
                                x.Dsc_img()
                                break
                        break
                #------------------------------------------------------------------------------------------------------
                print('ход второго игрока:', turn_cards_player_2)
                #------------------------------------------------------------------------------------------------------
                for i in range(179): print('\033[31m*', end='')
                print('*\033[0m')
                #------------------------------------------------------------------------------------------------------


                list_cards_player_1_suit = [x for x in self.player_1_cards if x[1] == turn_cards_player_2_suit]
                list_cards_player_1_suit_higher = [x for x in list_cards_player_1_suit if x[0] > turn_cards_player_2_digit]
                if len(list_cards_player_1_suit_higher) + len(self.turn_cards_player_1_kozir) == 0:
                    self.player_1_cards.append(turn_cards_player_2)
                    self.player_2_cards.remove(turn_cards_player_2)


                    #--------------------------------------------------------------------------------------------------
                    self.ln_d=len(self.d_s)-1
                    for m in range(5,self.ln_d):
                        if self.d_s[m]!=0:
                            self.g1c.append(self.g2c[self.d_s[m]])
                            self.g1s.append(self.g2s[self.d_s[m]])
                            del self.g2c[self.d_s[m]]
                            del self.g2s[self.d_s[m]]
                            del self.d_c[m]
                            del self.d_s[m]
                            self.d_c.insert(m,0)
                            self.d_s.insert(m,0)
                            m=5
                    name1=self.n1
                    gmr1c=self.g1c
                    gmr1s=self.g1s
                    name2=self.n2
                    gmr2c=self.g2c
                    gmr2s=self.g2s
                    dsc_c=self.d_c
                    dsc_s=self.d_s
                    cld_n=len(self.list_coloda)
                    x=Game_fool_card_desc(name1, gmr1c, gmr1s, name2, gmr2c, gmr2s, dsc_c, dsc_s, cld_n)
                    x.blk_chk()
                    x.Dsc_img()
                    #--------------------------------------------------------------------------------------------------

                    #--------------------------------------------------------------------------------------------------
                    print('первый игрок взял')
                    #--------------------------------------------------------------------------------------------------
                    for i in range(179): print('\033[31m*', end='')
                    print('*\033[0m')
                    #--------------------------------------------------------------------------------------------------



                    self.dobor()
                    w = 1
                elif turn_cards_player_2_suit == self.kozir and turn_cards_player_2[0] > self.turn_cards_player_1_kozir[-1][0]:
                    self.player_1_cards.append(turn_cards_player_2)
                    self.player_2_cards.remove(turn_cards_player_2)


                    #--------------------------------------------------------------------------------------------------
                    self.ln_d=len(self.d_s)-1
                    for m in range(5,self.ln_d):
                        if self.d_s[m]!=0:
                            self.g1c.append(self.g2c[self.d_s[m]])
                            self.g1s.append(self.g2s[self.d_s[m]])
                            del self.g2c[self.d_s[m]]
                            del self.g2s[self.d_s[m]]
                            del self.d_c[m]
                            del self.d_s[m]
                            self.d_c.insert(m,0)
                            self.d_s.insert(m,0)
                            m=5
                    name1=self.n1
                    gmr1c=self.g1c
                    gmr1s=self.g1s
                    name2=self.n2
                    gmr2c=self.g2c
                    gmr2s=self.g2s
                    dsc_c=self.d_c
                    dsc_s=self.d_s
                    cld_n=len(self.list_coloda)
                    x=Game_fool_card_desc(name1, gmr1c, gmr1s, name2, gmr2c, gmr2s, dsc_c, dsc_s, cld_n)
                    x.blk_chk()
                    x.Dsc_img()
                    #--------------------------------------------------------------------------------------------------

                    #--------------------------------------------------------------------------------------------------
                    print('первый игрок взял')
                    #--------------------------------------------------------------------------------------------------
                    for i in range(179): print('\033[31m*', end='')
                    print('*\033[0m')
                    #--------------------------------------------------------------------------------------------------


                    self.dobor()
                    w = 1
                elif turn_cards_player_2_suit == self.kozir and turn_cards_player_2[0] < self.turn_cards_player_1_kozir[-1][0]:


                    #--------------------------------------------------------------------------------------------------
                    tuple_g1=()
                    for m in range(len(self.g1c)):
                        if self.g1s[m]==4: tuple_g1 =(self.g1c[m]+4, 'c')
                        if self.g1s[m]==3: tuple_g1 =(self.g1c[m]+4, 'b')
                        if self.g1s[m]==2: tuple_g1 =(self.g1c[m]+4, 'k')
                        if self.g1s[m]==5: tuple_g1 =(self.g1c[m]+4, 'p')
                        if tuple_g1==self.turn_cards_player_1_kozir[-1]:
                            self.ln_d=len(self.d_c)-2
                            for p in range(5,self.ln_d):
                                if self.d_c[p] ==0 and self.d_s[p] ==0:
                                    del self.d_c[p]
                                    self.d_c.insert(p,m)
                                    name1=self.n1
                                    gmr1c=self.g1c
                                    gmr1s=self.g1s
                                    name2=self.n2
                                    gmr2c=self.g2c
                                    gmr2s=self.g2s
                                    dsc_c=self.d_c
                                    dsc_s=self.d_s
                                    cld_n=len(self.list_coloda)
                                    x=Game_fool_card_desc(name1, gmr1c, gmr1s, name2, gmr2c, gmr2s, dsc_c, dsc_s, cld_n)
                                    x.blk_chk()
                                    x.Dsc_img()
                                    break
                            break
                        #----------------------------------------------------------------------------------------------

                    #--------------------------------------------------------------------------------------------------
                    print('ход первого игрока:', self.turn_cards_player_1_kozir[-1])
                    #--------------------------------------------------------------------------------------------------
                    for i in range(179): print('\033[31m*', end='')
                    print('*\033[0m')
                    #--------------------------------------------------------------------------------------------------


                    turn_cards_player_1 = self.turn_cards_player_1_kozir[-1]
                    self.player_1_cards.remove(turn_cards_player_1)
                    self.player_2_cards.remove(turn_cards_player_2)
                    self.bito(turn_cards_player_1, turn_cards_player_2)


                    #--------------------------------------------------------------------------------------------------
                    bito_g1=[]
                    bito_g2=[]
                    self.ln_d=len(self.d_c)-2
                    for m in range(self.ln_d,4,-1):
                        if self.d_c[m]!=0:
                            bito_g1.append(self.d_c[m])
                            del self.d_c[m]
                            self.d_c.insert(m,0)
                        if self.d_s[m]!=0:
                            bito_g2.append(self.d_s[m])
                            del self.d_s[m]
                            self.d_s.insert(m,0)
                    self.ln_d=len(bito_g1)
                    if self.ln_d!=0:
                        for m in range(self.ln_d):
                            del self.g1c[bito_g1[m]]
                            del self.g1s[bito_g1[m]]
                            if bito_g1[m]==2:
                                self.g1c.insert(2,0)
                                self.g1s.insert(2,0)
                    self.ln_d=len(bito_g2)
                    for m in range(self.ln_d):
                        del self.g2c[bito_g2[m]]
                        del self.g2s[bito_g2[m]]
                        if bito_g2[m]==2:
                            self.g2c.insert(2,0)
                            self.g2s.insert(2,0)

                    self.ln_d=(len(self.d_c)-1)
                    del self.d_c[self.ln_d]
                    del self.d_s[self.ln_d]
                    self.d_c.append(1)
                    self.d_s.append(1)

                    name1=self.n1
                    gmr1c=self.g1c
                    gmr1s=self.g1s
                    name2=self.n2
                    gmr2c=self.g2c
                    gmr2s=self.g2s
                    dsc_c=self.d_c
                    dsc_s=self.d_s
                    cld_n=len(self.list_coloda)
                    x=Game_fool_card_desc(name1, gmr1c, gmr1s, name2, gmr2c, gmr2s, dsc_c, dsc_s, cld_n)
                    x.blk_chk()
                    x.Dsc_img()
                    #--------------------------------------------------------------------------------------------------
                    print('бито')
                    #--------------------------------------------------------------------------------------------------
                    for i in range(179): print('\033[31m*', end='')
                    print('*\033[0m')
                    #--------------------------------------------------------------------------------------------------

                    self.dobor()
                    w = 0
                elif len(list_cards_player_1_suit_higher) == 0 and len(self.turn_cards_player_1_kozir) > 0:

                    #--------------------------------------------------------------------------------------------------
                    tuple_g1=()
                    for m in range(len(self.g1c)):
                        if self.g1s[m]==4: tuple_g1 =(self.g1c[m]+4, 'c')
                        if self.g1s[m]==3: tuple_g1 =(self.g1c[m]+4, 'b')
                        if self.g1s[m]==2: tuple_g1 =(self.g1c[m]+4, 'k')
                        if self.g1s[m]==5: tuple_g1 =(self.g1c[m]+4, 'p')
                        if tuple_g1 == self.turn_cards_player_1_kozir[0]:
                            self.ln_d=len(self.d_c)-2
                            for p in range(5,self.ln_d):
                                if self.d_c[p] ==0 and self.d_s[p] ==0:
                                    del self.d_c[p]
                                    self.d_c.insert(p,m)
                                    name1=self.n1
                                    gmr1c=self.g1c
                                    gmr1s=self.g1s
                                    name2=self.n2
                                    gmr2c=self.g2c
                                    gmr2s=self.g2s
                                    dsc_c=self.d_c
                                    dsc_s=self.d_s
                                    cld_n=len(self.list_coloda)
                                    x=Game_fool_card_desc(name1, gmr1c, gmr1s, name2, gmr2c, gmr2s, dsc_c, dsc_s, cld_n)
                                    x.blk_chk()
                                    x.Dsc_img()
                                    break
                            break
                        #----------------------------------------------------------------------------------------------

                    #--------------------------------------------------------------------------------------------------
                    print('ход первого игрока:', self.turn_cards_player_1_kozir[0])
                    #--------------------------------------------------------------------------------------------------
                    for i in range(179): print('\033[31m*', end='')
                    print('*\033[0m')
                    #--------------------------------------------------------------------------------------------------

                    turn_cards_player_1 = self.turn_cards_player_1_kozir[0]
                    self.player_1_cards.remove(turn_cards_player_1)
                    self.player_2_cards.remove(turn_cards_player_2)
                    self.bito(turn_cards_player_1, turn_cards_player_2)


                    #--------------------------------------------------------------------------------------------------
                    bito_g1=[]
                    bito_g2=[]
                    self.ln_d=len(self.d_c)-2
                    for m in range(self.ln_d,4,-1):
                        if self.d_c[m]!=0:
                            bito_g1.append(self.d_c[m])
                            del self.d_c[m]
                            self.d_c.insert(m,0)
                        if self.d_s[m]!=0:
                            bito_g2.append(self.d_s[m])
                            del self.d_s[m]
                            self.d_s.insert(m,0)
                    self.ln_d=len(bito_g1)
                    if self.ln_d!=0:
                        for m in range(self.ln_d):
                            del self.g1c[bito_g1[m]]
                            del self.g1s[bito_g1[m]]
                            if bito_g1[m]==2:
                                self.g1c.insert(2,0)
                                self.g1s.insert(2,0)
                    self.ln_d=len(bito_g2)
                    for m in range(self.ln_d):
                        del self.g2c[bito_g2[m]]
                        del self.g2s[bito_g2[m]]
                        if bito_g2[m]==2:
                            self.g2c.insert(2,0)
                            self.g2s.insert(2,0)

                    self.ln_d=(len(self.d_c)-1)
                    del self.d_c[self.ln_d]
                    del self.d_s[self.ln_d]
                    self.d_c.append(1)
                    self.d_s.append(1)

                    name1=self.n1
                    gmr1c=self.g1c
                    gmr1s=self.g1s
                    name2=self.n2
                    gmr2c=self.g2c
                    gmr2s=self.g2s
                    dsc_c=self.d_c
                    dsc_s=self.d_s
                    cld_n=len(self.list_coloda)
                    x=Game_fool_card_desc(name1, gmr1c, gmr1s, name2, gmr2c, gmr2s, dsc_c, dsc_s, cld_n)
                    x.blk_chk()
                    x.Dsc_img()
                    #--------------------------------------------------------------------------------------------------
                    print('бито')
                    #--------------------------------------------------------------------------------------------------
                    for i in range(179): print('\033[31m*', end='')
                    print('*\033[0m')
                    #--------------------------------------------------------------------------------------------------


                    self.dobor()
                    w = 0
                else:



                    #--------------------------------------------------------------------------------------------------
                    tuple_g1=()
                    for m in range(len(self.g1c)):
                        if self.g1s[m]==4: tuple_g1 =(self.g1c[m]+4, 'c')
                        if self.g1s[m]==3: tuple_g1 =(self.g1c[m]+4, 'b')
                        if self.g1s[m]==2: tuple_g1 =(self.g1c[m]+4, 'k')
                        if self.g1s[m]==5: tuple_g1 =(self.g1c[m]+4, 'p')
                        if  tuple_g1 == list_cards_player_1_suit_higher[0]:
                            self.ln_d=len(self.d_c)-2
                            for p in range(5,self.ln_d):
                                if self.d_c[p] ==0 and self.d_s[p] ==0:
                                    del self.d_c[p]
                                    self.d_c.insert(p,m)
                                    name1=self.n1
                                    gmr1c=self.g1c
                                    gmr1s=self.g1s
                                    name2=self.n2
                                    gmr2c=self.g2c
                                    gmr2s=self.g2s
                                    dsc_c=self.d_c
                                    dsc_s=self.d_s
                                    cld_n=len(self.list_coloda)
                                    x=Game_fool_card_desc(name1, gmr1c, gmr1s, name2, gmr2c, gmr2s, dsc_c, dsc_s, cld_n)
                                    x.blk_chk()
                                    x.Dsc_img()
                                    break
                            break
                        #----------------------------------------------------------------------------------------------

                    #--------------------------------------------------------------------------------------------------
                    print('ход первого игрока:', list_cards_player_1_suit_higher[0])
                    #--------------------------------------------------------------------------------------------------
                    for i in range(179): print('\033[31m*', end='')
                    print('*\033[0m')
                    #--------------------------------------------------------------------------------------------------


                    turn_cards_player_1 = list_cards_player_1_suit_higher[0]
                    self.player_1_cards.remove(turn_cards_player_1)
                    self.player_2_cards.remove(turn_cards_player_2)
                    self.bito(turn_cards_player_1, turn_cards_player_2)


                    #--------------------------------------------------------------------------------------------------
                    bito_g1=[]
                    bito_g2=[]
                    self.ln_d=len(self.d_c)-2
                    for m in range(self.ln_d,4,-1):
                        if self.d_c[m]!=0:
                            bito_g1.append(self.d_c[m])
                            del self.d_c[m]
                            self.d_c.insert(m,0)
                        if self.d_s[m]!=0:
                            bito_g2.append(self.d_s[m])
                            del self.d_s[m]
                            self.d_s.insert(m,0)
                    self.ln_d=len(bito_g1)
                    if self.ln_d!=0:
                        for m in range(self.ln_d):
                            del self.g1c[bito_g1[m]]
                            del self.g1s[bito_g1[m]]
                            if bito_g1[m]==2:
                                self.g1c.insert(2,0)
                                self.g1s.insert(2,0)
                    self.ln_d=len(bito_g2)
                    for m in range(self.ln_d):
                        del self.g2c[bito_g2[m]]
                        del self.g2s[bito_g2[m]]
                        if bito_g2[m]==2:
                            self.g2c.insert(2,0)
                            self.g2s.insert(2,0)

                    self.ln_d=(len(self.d_c)-1)
                    del self.d_c[self.ln_d]
                    del self.d_s[self.ln_d]
                    self.d_c.append(1)
                    self.d_s.append(1)

                    name1=self.n1
                    gmr1c=self.g1c
                    gmr1s=self.g1s
                    name2=self.n2
                    gmr2c=self.g2c
                    gmr2s=self.g2s
                    dsc_c=self.d_c
                    dsc_s=self.d_s
                    cld_n=len(self.list_coloda)
                    x=Game_fool_card_desc(name1, gmr1c, gmr1s, name2, gmr2c, gmr2s, dsc_c, dsc_s, cld_n)
                    x.blk_chk()
                    x.Dsc_img()
                    #--------------------------------------------------------------------------------------------------
                    print('бито')
                    #--------------------------------------------------------------------------------------------------
                    for i in range(179): print('\033[31m*', end='')
                    print('*\033[0m')
                    #--------------------------------------------------------------------------------------------------

                    self.dobor()
                    w = 0


                print('карты 1-го игрока после {} хода:'.format(i), len(self.player_1_cards), self.player_1_cards)
                print('карты 2-го игрока после {} хода:'.format(i), len(self.player_2_cards), self.player_2_cards)
                #------------------------------------------------------------------------------------------------------
                for i in range(179): print('\033[31m*', end='')
                print('*\033[0m')
                #------------------------------------------------------------------------------------------------------



            if len(self.player_1_cards) == 0 and len(self.player_2_cards) == 0:

                First_lst=[]
                # Вывод изображений игроков - ничья! (совместное фото)
                f = open('Image_player_first', encoding="utf8")
                i=0
                for line in f:
                    line = f.readline(32)
                    First_lst.append(line)
                    i+=1
                f.close()

                Second_lst=[]
                f = open('Image_player_second', encoding="utf8")
                i=0
                for line in f:
                    line = f.readline(27)
                    Second_lst.append(line)
                    i+=1
                f.close()

                for ii in range(i-1):
                    print(First_lst[ii] + Second_lst[ii])
                #------------------------------------------------------------------------------------------------------
                for i in range(179): print('\033[31m*', end='')
                print('*\033[0m')
                #------------------------------------------------------------------------------------------------------
                print('ничья')
                #------------------------------------------------------------------------------------------------------
                for i in range(179): print('\033[31m*', end='')
                print('*\033[0m')
                #------------------------------------------------------------------------------------------------------


                break
            elif len(self.player_1_cards) == 0:

                # Вывод изображения игрока 1 - победителя!
                f = open('Image_player_first', encoding="utf8")
                i=1
                for line in f:
                    print(line, end='')
                    i+=1
                f.close()
                #------------------------------------------------------------------------------------------------------
                for i in range(179): print('\033[31m*', end='')
                print('*\033[0m')
                #------------------------------------------------------------------------------------------------------
                print('1-й игрок победил')
                #------------------------------------------------------------------------------------------------------
                for i in range(179): print('\033[31m*', end='')
                print('*\033[0m')
                #------------------------------------------------------------------------------------------------------

                break
            elif len(self.player_2_cards) == 0:


                # Вывод изображения игрока 2 - победителя!
                f = open('Image_player_second', encoding="utf8")
                for line in f:
                    print(line, end='')
                f.close()
                print()
                #------------------------------------------------------------------------------------------------------
                for i in range(179): print('\033[31m*', end='')
                print('*\033[0m')
                #------------------------------------------------------------------------------------------------------
                print('2-й игрок победил')
                #------------------------------------------------------------------------------------------------------
                for i in range(179): print('\033[31m*', end='')
                print('*\033[0m')
                #------------------------------------------------------------------------------------------------------

                break

if __name__ == '__main__':
    cards_game = Game_logic1_durak(25)
    cards_game.set_players_cards()
    cards_game.turn_cards()
'''