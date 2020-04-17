#Дмитрий Шангин • Вс 26 Янв 12:30 • Ответ создан Сб 25 Янв 16:39
#https://github.com/ProgrammistMiddle/lesson_9/blob/master/Lesson_9

import random
class Durak:
    def __init__(self,igrok):
        self.igrok = igrok
        self.all_cards_on_table=[]
        self.con=[]
        self.otbivka=[]
        self.igrokCard = []
        self.compCard = []
        self.genCard = Durak.gen(self)
        self.counts=0
        self.kozyr = []
        self.nextCardComp=[]

    def card(self):
        self.d = ['06','07','08','09','10','avalet','dama','korol','tuz']
        self.masty_p=list(map(lambda x: x+'_p', self.d))
        self.masty_k = list(map(lambda x: x+'_k',self.d))
        self.masty_ch = list(map(lambda x: x+'_c',self.d))
        self.masty_b = list(map(lambda x: x+'_b',self.d))
        self.allCard= self.masty_k+ self.masty_p+ self.masty_ch+ self.masty_b
        random.shuffle(self.allCard)
        return self.allCard

    def gen(self):
        for i in Durak.card(self):
            yield i

    def kozCart(self):
        self.kozyr=next(self.genCard)

    def playersCard(self):
        while len(self.igrokCard)<6 or len(self.compCard)<6 and self.counts<36:
            if len(self.igrokCard)<6 and len(self.compCard)<6:
                self.igrokCard.append(next(self.genCard))
                self.counts +=1
                self.compCard.append(next(self.genCard))
                self.counts +=1
            elif len(self.compCard)<6:
                self.compCard.append(next(self.genCard))
                self.counts +=1
            elif len(self.igrokCard)<6:
                self.igrokCard.append(next(self.genCard))
                self.counts +=1




myIgrok= Durak('dima')
myIgrok.playersCard()
myIgrok.kozCart()
print('козырь: ',myIgrok.kozyr)
#myIgrok.playersCard()
#myIgrok.gen()
#myIgrok.playersCard(myIgrok.igrokCard, myIgrok.compCard)
#cart=myIgrok.igrokCard
myIgrok.igrokCard.sort(key=lambda x:x[-1])
print ('начальные карты',myIgrok.igrokCard)

#cartComp = myIgrok.compCard
myIgrok.compCard.sort(key=lambda x:x[2])
print (myIgrok.compCard )


def takeCard(name):
    for i in myIgrok.all_cards_on_table:
        myIgrok.compCard.append(i)
        myIgrok.igrokCard.remove(name) #del u igroka
        myIgrok.playersCard()
        print ('компьтер взял')
        print() #need
        print('ваши карты',myIgrok.igrokCard)
        print(myIgrok.compCard)
        myIgrok.all_cards_on_table.clear()
        myIgrok.con.clear()
        myIgrok.otbivka.clear()
        print() # need
        start(input('1введите любую вашу карту:'))







def find(names, name):
    myIgrok.all_cards_on_table.append(name)
    #count =[] # карты которыми иожет отбиться компьютер
    print('con',myIgrok.con)
    print ('otbivka',myIgrok.otbivka)
    print('all_cards_on_table',myIgrok.all_cards_on_table)




    for i in names :
        if i in myIgrok.compCard:
            if i > name:
                myIgrok.otbivka.append(i)


    # комп не может отбить первую карту
    if len(myIgrok.otbivka) == 0 and len(myIgrok.con)==0:
        for i in myIgrok.all_cards_on_table:
            myIgrok.compCard.append(i)
            myIgrok.igrokCard.remove(name) #del u igroka
            myIgrok.playersCard()
            print ('компьтер взял')
            print() #need
            print('ваши карты',myIgrok.igrokCard)
            print(myIgrok.compCard)
            myIgrok.all_cards_on_table.clear()
            myIgrok.con.clear()
            myIgrok.otbivka.clear()
            print() # need
            start(input('5введите любую вашу карту:'))

        # комп не может отбить вторую карту
    elif len(myIgrok.otbivka)==0 and len(myIgrok.con)>0:
        takeCard(name)


    # комп может отбить карту
    elif len(myIgrok.otbivka) > 0:
        # "con" карты без мастей
        myIgrok.con.append(name[:-2])
        myIgrok.con.append(myIgrok.otbivka[0][:-2])
        myIgrok.all_cards_on_table.append(myIgrok.otbivka[0])
        print('Ход компьютера',myIgrok.otbivka[0])
        myIgrok.igrokCard.remove(name)
        myIgrok.compCard.remove(myIgrok.otbivka[0])
        myIgrok.otbivka.clear()
    print() #need
    print ('Ваши карты',myIgrok.igrokCard)
    print (myIgrok.compCard)
    print ('con',myIgrok.con)
    print ('Карты на столе', myIgrok.all_cards_on_table)
    print()#need
    hod(input('Введите next карту или bito: '))




#////////////////////////////////
def checkCardIgrok(vvod, hodComp):
    if vvod not in myIgrok.igrokCard:
        if vvod =='beru':
            findMyHod(vvod,hodComp)
        elif vvod != 'beru':
            print('3У Вас нет этой карты')
            vvod= input('введите карту: ')
    else: findMyHod(vvod,hodComp)



def computer():
    print(myIgrok.compCard)
    print('мои карты',myIgrok.igrokCard)
    print('Компьютер ходит',myIgrok.compCard[0])
    hodComp=myIgrok.compCard[0]
    myIgrok.all_cards_on_table.append(myIgrok.compCard[0])
    myIgrok.con.append(myIgrok.compCard[0][:-2])
    myIgrok.compCard.remove(myIgrok.compCard[0])
    myIgrok.igrokCard
    vvod= input('введите карту или напишите: beru: ')
    checkCardIgrok(vvod,hodComp)










#///////////////////////////////////
def igrok():
    print ('игрок',myIgrok.igrokCard,)
    print('комп',myIgrok.compCard)
    print('кон',myIgrok.con)
    print ('стол',myIgrok.all_cards_on_table)
def addDell(vvod):
    myIgrok.con.append(vvod[:-2])
    myIgrok.igrokCard.remove(vvod)
    myIgrok.all_cards_on_table.append(vvod)
#забирает карты
def takeTable(nameplayer):
    for i in myIgrok.all_cards_on_table:
        nameplayer.append(i)
    if len(myIgrok.nextCardComp)!=0:
        for i in myIgrok.nextCardComp:
            nameplayer.append(i)
    myIgrok.all_cards_on_table.clear()
    myIgrok.con.clear()
    myIgrok.playersCard()
    computer()
#/////////////////////////////////
#отбивание карт
def otbivkaCart(vvod,findMyHod=0,hodComp=0):
    bita=[]
    count=0
    #определяем масть карты компьютера и определяем какими картами можно ее отбить
    for i in findMyHod:
        if hodComp<i:
            bita.append(i)
    #если есть у нас карты которыми мы можем отбить карту компа ставим 1
    for i in bita:
        if i == vvod:
            count+=1
    if count==0:
        print('отбейте карту правильно или введите: beru')
        vvod=input('введите заново или напишите: beru: ')
    addDell(vvod)
    igrok()
    nextHodComp()

def nextHodComp():
    cardComp=[]  #карта которую может подкинуть комп
    for i in myIgrok.con:
        for a in myIgrok.compCard:
            if i in a:
                cardComp.append(a)
    print('cardComp',cardComp)
    if len(cardComp) > 0:
        print('компьютер подкидывает',cardComp[0])
        myIgrok.con.append(cardComp[0][:-2])
        myIgrok.compCard.remove(cardComp[0])
        myIgrok.all_cards_on_table.append(cardComp[0])
        vvod=input('отбейте карту или напишите: beru ')
        #проверка могу ли я отбить карту
        checkCardIgrok(vvod,cardComp[0])
        #конец проверки


    elif len(cardComp) <1:
        print('настала бита')
        myIgrok.all_cards_on_table.clear()
        myIgrok.con.clear()
        myIgrok.playersCard()
        igrok()
        print ('со старта')
        start(input('снова ваш ход: '))


#ищет правильную масть
def findMyHod(vvod,hodComp ):
    if '_p' in vvod:
        otbivkaCart(vvod,myIgrok.masty_p,hodComp )
    elif '_b' in vvod:
        otbivkaCart(vvod,myIgrok.masty_b,hodComp )
    elif '_c' in vvod:
        otbivkaCart(vvod,myIgrok.masty_ch,hodComp  )
    elif '_k' in vvod:
        otbivkaCart(vvod,myIgrok.masty_k,hodComp )
    elif vvod=='beru':
        takeTable(myIgrok.igrokCard)
        igrok()
    else: print('нет такой масти')







def hod(name):
    if name in myIgrok.igrokCard  and name[:-2] in  myIgrok.con:
        hod1(name)
    elif name in myIgrok.igrokCard and name[:-2] not in myIgrok.con:
        print('этой карты нет на столе')
        hod(input('2введите любую вашу карту: '))
    elif name=='bito':
        myIgrok.playersCard()
        print('Ваши карты',myIgrok.igrokCard)
        myIgrok.con.clear()
        myIgrok.all_cards_on_table.clear()
        computer()
    elif name not in myIgrok.igrokCard:
        print ('2У Вас нет такой карты')
        hod(input('4введите любую вашу карту: '))



def hod1(name):
    if '_p' in name:
        find( myIgrok.masty_p,name)
    elif '_b' in name:
        find( myIgrok.masty_b,name)
    elif '_c' in name:
        find(myIgrok.masty_ch,name)
    elif '_k' in name:
        find( myIgrok.masty_k,name)

print() #need
def start(start):
    if start not in myIgrok.igrokCard:
        print('1У вас нет этой карты')
    else: hod1(start)
start(input('5введите любую вашу карту: '))