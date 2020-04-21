#!python3.7
#coding: utf-8
# Желательно настроить шрифт (File-Settings-Editor-Font) - Consolas, size:13, Line spacing:0.8
# Сафиуллин Ильфат, к домашнему заданию урока №9 (Python)

class Game_fool_card_desc:
    #------------------------------------------------------------------------------------------------------------------
    Label='\033[47m   -=СТОЛ КАРТОЧНОЙ ИГРЫ "В ДУРАКА"=-   \033[0m'
    for i in range(70): print('\033[31m*', end='')
    print(Label, end='')
    for i in range(70): print('\033[31m*', end='')
    print('*\033[0m')
    #------------------------------------------------------------------------------------------------------------------
    def __init__(self, name1, gmr1c, gmr1s, name2, gmr2c, gmr2s, dsc_c, dsc_s, cld_n):
        self.card=[' ','§',' 6',' 7',' 8',' 9','10',' V',' D',' K',' T']
        self.suit=[' ','§','♣','\033[31m♦\033[0m','\033[31m♥\033[0m','♠']
        #self.suit=[' ','§','♣','♦','♥','♠']
        self.cld = cld_n
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
                    self.ds.insert(0,1) # флаг включения режима -- правильно!
                    #self.ds.insert(0,0) # флаг включения режима --------------- не правильно!

                self.nc=len(self.dc) # количество карт компьютера для отображения len(tcard)=len(tsuit)
                self.tc=self.dc # num_card:[0,1,2,,,10] список иерархического имени козыря, изображение колоды, боя и биты
                self.ts=self.ds # num_suit:[0,1,2,,,5] список масти козыря, изображение колоды, боя и биты
                if self.cld==0:
                    del self.dc[1]
                    del self.ds[1]
                    self.dc.insert(1,0)
                    self.ds.insert(1,0)
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
                        elif d==1 and n==1 and i==8:
                            self.img.insert(l+8,'\033[47m"Колода" \033[0m')
                        elif d==1 and n==(len(self.ds)-1) and i==8:
                                self.img.insert(l+8,'\033[47m "Бито"  \033[0m')
                        else:
                            self.img.insert(l+8,'         ')
                    l+=9

                # все закрытые карты
                if self.cn==1:
                    if n==1:
                        self.img.insert(l+0,f'\033[47m   {(self.cld):>3}   \033[0m')
                    else:
                        self.img.insert(l+0,'         ')
                    self.img.insert(l+1,'┌───────┐')

                    if n==3 and d==1: s = (self.suit[self.ds[3]])
                    for i in range(2,7): self.img.insert(l+i,f'|{s+s+s+s+s+s+s}|')
                    self.img.insert(l+7,'└───────┘')

                    if n==1:
                        self.img.insert(l+8,'\033[47m"Колода" \033[0m')
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
gmr1c = [0,0,0,0,0,0,0,0,0 возможно увеличение ] #──── ранг карты, игрока 1
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
#          |   ┌─ место "Козыря              (с 5 по 15,все нечётные, если ходит, dsc_c адреса списка карт игрока 1)
#          |   |                             (с 6 по 16, все чётные, если отбивается, dsc_c адреса списка карт игрока 1) 
#          |   |     наличие ходов игроками       
#          |   |   ┌───────────────────────┐ ┌─ место "Биты"
dsc_c = [0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0] #──── ранг карты, для позиций с 1 по 4 и 18
dsc_s = [0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0] #──── масть карты, для позиций с 1 по 4 и 18 
#        0,1,2,3,4,5,6,7,8,9,1,1,1,1,1,1,1,1,1,1 
#        |   |   |           0,1,2,3,4,5,6,7,8,9
#        |   |   |                             └── свободное картоместо
#        |   └───└── свободное картоместо    (с 5 по 15,все нечётные, если ходит, dsc_s адреса списка карт игрока 2)
#        └─── dsc_s=[0]флаг вкл.налож карт   (с 6 по 16, все чётные, если отбивается, dsc_s адреса списка карт игрока 2)
                        
# id num_card: [' ','§','6','7','8','9','10','V','D','K','T'] (''-'Т')
# id num_card: [ 0 , 1 , 2 , 3 , 4 , 5 ,  6 , 7 , 8 , 9 , 10] (0 - 10)
# id num_suit: [' ','§','♣','♦','♥','♠'] (''-'♠')
# id num_suit: [ 0 , 1 , 2 , 3 , 4 , 5 ] (0 - 5 )
gmr2c = [0,0,0,0,0,0,0,0,0 возможно увеличение ] #──── ранг карты, игрока 2
gmr2s = [0,0,0,0,0,0,0,0,0 занимаемых картомест] #──── масть карты, игрока 2
#        0,1,2,3,4,5,6,7,8
#        | | |
#        | └─└── свободное картоместо    (с 1 по 3, список картомест игрока 2)
#        | 
#        └─ 'надпись "2 ИГРОК:"'
#        └─ '           "имя"'
#        └─ '         "действие"'

x=Game_fool_card_desc(name1, gmr1c, gmr1s, name2, gmr2c, gmr2s, dsc_c, dsc_s, cld_n))
x.blk_chk()
x.Dsc_img()
'''