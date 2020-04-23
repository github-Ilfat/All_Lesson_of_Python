import unittest

from For_Job_01_L10_Game_fool_card_desc import Game_fool_card_desc

class Test_Game_fool_card_desc_unittest(unittest.TestCase):

    def setUp(self):
        # Присвоение значений для параметров класса "-=СТОЛ КАРТОЧНОЙ ИГРЫ "В ДУРАКА"=-"
        name1='Комп1' #──── имя игрока 1
        name2='Комп2' #──── имя игрока 2
        gmr1c = [0,0,0,6,0,0,0,0,0] #──── ранг карты, игрока 1
        gmr1s = [0,0,0,3,0,0,0,0,0] #──── масть карты, игрока 1
        dsc_c = [0,1,0,9,0,3,0,0,0,0,0,0,0,0,0,0,0,0,0,0] #──── ранг карты, для позиций с 1 по 4 и 18
        dsc_s = [0,1,0,2,0,0,3,0,0,0,0,0,0,0,0,0,0,0,0,0] #──── масть карты, для позиций с 1 по 4 и 18
        gmr2c = [0,0,0,8,0,0,0,0,0] #──── ранг карты, игрока 2
        gmr2s = [0,0,0,3,0,0,0,0,0] #──── масть карты, игрока 2
        cld_n=36
        # Запуск класса "-=СТОЛ КАРТОЧНОЙ ИГРЫ "В ДУРАКА"=-"
        self.x=Game_fool_card_desc(name1, gmr1c, gmr1s, name2, gmr2c, gmr2s, dsc_c, dsc_s, cld_n)
        self.x.blk_chk()
        self.x.Dsc_img()

        # Присвоение атрибутов для этого класса, с целью тестирования целевого класса
        self.card=[' ','§',' 6',' 7',' 8',' 9','10',' V',' D',' K',' T']
        self.suit=[' ','§','♣','\033[31m♦\033[0m','\033[31m♥\033[0m','♠']
        self.name1=name1
        self.name2=name1
        self.gmr1c=gmr1c
        self.gmr1s=gmr1s
        self.dsc_c=dsc_c
        self.dsc_s=dsc_s
        self.gmr2c=gmr2c
        self.gmr2s=gmr2s
        self.cld_n=cld_n

        print('Sets for start test completed!')


    def test_blk_chk(self):
        if len(self.gmr1c)==len(self.gmr1s) and len(self.gmr2c)==len(self.gmr2s) and len(self.dsc_c)==len(self.dsc_s):
            self.assertTrue(self.x.chk_error == 0)
        else: self.assertFalse(self.x.chk_error == 1)
        # значения атрибута данного класса
        if self.x.dc[5]!=0:
            # проверка значений атрибутов целевого класса
            self.assertEqual(self.x.action1, 'ходит!')
            self.assertEqual(self.x.action2, 'отбивает!')
        # значения атрибута данного класса
        if self.x.ds[5]!=0:
            # проверка значений атрибутов целевого класса
            self.assertEqual(self.x.action1, 'отбивает!')
            self.assertEqual(self.x.action2, 'ходит!')

    def test_init(self):
        # проверка значений атрибутов целевого класса
        self.assertEqual(self.x.dc[1], 1) # "Закрытая карта" (колода)
        self.assertEqual(self.x.ds[1], 1) # "§" (рисунок рубашки)
        self.assertEqual(self.x.dc[3], 9) # "Король"
        self.assertTrue(self.x.ds[3] == 2) # "Крести"

    def test_Dsc_img(self):
        # флаг включения режима отображения "наложение карт"
        # значения атрибутов данного класса
        if (self.dsc_c[5]!=0 and self.dsc_s[6]!=0) or (self.dsc_s[5]!=0 and self.dsc_c[6]!=0):
            # проверка значения атрибута целевого класса
            self.assertEqual(self.x.ds[0], 1)

    def teardown(self):
        print('All tests has completed!')
