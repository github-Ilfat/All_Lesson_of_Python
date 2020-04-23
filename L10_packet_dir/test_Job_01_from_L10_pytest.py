import pytest
import csv
import copy

from For_Job_01_L10_Game_fool_card_desc import Game_fool_card_desc


class Test_Game_fool_card_desc_pytest:

    def setup(self):
        # Присвоение значений для параметров класса "-=СТОЛ КАРТОЧНОЙ ИГРЫ "В ДУРАКА"=-"
        name1 = 'Комп1'  # ──── имя игрока 1
        name2 = 'Комп2'  # ──── имя игрока 2
        gmr1c = [0, 0, 0, 6, 0, 0, 0, 0, 0]  # ──── ранг карты, игрока 1
        gmr1s = [0, 0, 0, 3, 0, 0, 0, 0, 0]  # ──── масть карты, игрока 1
        dsc_c = [0, 1, 0, 9, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                 0]  # ──── ранг карты, для позиций с 1 по 4 и 18
        dsc_s = [0, 1, 0, 2, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                 0]  # ──── масть карты, для позиций с 1 по 4 и 18
        gmr2c = [0, 0, 0, 8, 0, 0, 0, 0, 0]  # ──── ранг карты, игрока 2
        gmr2s = [0, 0, 0, 3, 0, 0, 0, 0, 0]  # ──── масть карты, игрока 2
        cld_n = 36
        # Запуск класса "-=СТОЛ КАРТОЧНОЙ ИГРЫ "В ДУРАКА"=-"
        self.x = Game_fool_card_desc(name1, gmr1c, gmr1s, name2, gmr2c, gmr2s, dsc_c, dsc_s, cld_n)
        self.x.blk_chk()
        self.x.Dsc_img()

        # Присвоение атрибутов для этого класса, с целью тестирования целевого класса
        self.card = [' ', '§', ' 6', ' 7', ' 8', ' 9', '10', ' V', ' D', ' K', ' T']
        self.suit = [' ', '§', '♣', '\033[31m♦\033[0m', '\033[31m♥\033[0m', '♠']
        self.name1 = name1
        self.name2 = name1
        self.gmr1c = gmr1c
        self.gmr1s = gmr1s
        self.dsc_c = dsc_c
        self.dsc_s = dsc_s
        self.gmr2c = gmr2c
        self.gmr2s = gmr2s
        self.cld_n = cld_n

        print('Sets for start test completed!')

    def test_blk_chk(self):
        if len(self.gmr1c) == len(self.gmr1s) and len(self.gmr2c) == len(self.gmr2s) and len(self.dsc_c) == len(
                self.dsc_s):
            assert self.x.chk_error == 0
        else:
            assert self.x.chk_error == 1
        # значения атрибута данного класса
        if self.x.dc[5] != 0:
            # проверка значений атрибутов целевого класса
            assert self.x.action1 == 'ходит!'
            assert self.x.action2 == 'отбивает!'
        # значения атрибута данного класса
        if self.x.ds[5] != 0:
            # проверка значений атрибутов целевого класса
            assert self.x.action1 == 'отбивает!'
            assert self.x.action2 == 'ходит!'

    def test_init(self):
        # проверка значений атрибутов целевого класса
        assert self.x.dc[1] == 1  # "Закрытая карта" (колода)
        assert self.x.ds[1] == 1  # "§" (рисунок рубашки)
        assert self.x.dc[3] == 9  # "Король"
        assert self.x.ds[3] == 2  # "Крести"

    def test_Dsc_img_swch(self):
        # флаг включения режима отображения "наложение карт"
        # значения атрибутов данного класса
        if (self.dsc_c[5] != 0 and self.dsc_s[6] != 0) or (self.dsc_s[5] != 0 and self.dsc_c[6] != 0):
            # проверка значения атрибута целевого класса
            assert self.x.ds[0] == 1

    def test_Dsc_img_prn(self):

        # Тест изображения 1
        # Присвоение значений для параметров класса "-=СТОЛ КАРТОЧНОЙ ИГРЫ "В ДУРАКА"=-"
        name1 = 'Комп1'  # ──── имя игрока 1
        name2 = 'Комп2'  # ──── имя игрока 2
        gmr1c = [0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0]  # ──── ранг карты, игрока 1
        gmr1s = [0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0]  # ──── масть карты, игрока 1
        dsc_c = [0, 1, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]  # ──── ранг карты, для позиций с 1 по 4 и 18
        dsc_s = [0, 1, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]  # ──── масть карты, для позиций с 1 по 4 и 18
        gmr2c = [0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0]  # ──── ранг карты, игрока 2
        gmr2s = [0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0]  # ──── масть карты, игрока 2
        cld_n = 36

        cards_imgs = []
        # Заполнение списка образцовым изображением из файла csv
        with open('Image_cards_for_compare.csv', encoding="utf8") as f:
            rdr = csv.reader(f, delimiter=',')
            i = 0
            for row in rdr:
                cards_imgs.append(row) # построчная загрузка списка
                #print(cards_imgs[i]) # построчный вывод списка и вложенных списков
                i = i + 1

        for x_suite in range(2,6):
            for y_card in range(2,11):
                gmr2c[3]=y_card
                gmr2s[3]=x_suite

                # Запуск класса "-=СТОЛ КАРТОЧНОЙ ИГРЫ "В ДУРАКА"=-"
                self.x = Game_fool_card_desc(name1, gmr1c, gmr1s, name2, gmr2c, gmr2s, dsc_c, dsc_s, cld_n)
                self.x.blk_chk()
                self.x.Dsc_img()

                # вывод изображения 1ой карты
                y_line_card=y_card # 0-10 строка блока изображения карты
                x_line_suit = x_suite  # 0-3 столбец блока изображения карты
                ln_bgn = 9*y_line_card  # 0,9,18,27,36,45,54,63,72,81 -- начала блоков строк изображения карт
                ln_end = ln_bgn + 9  # 9,18,27,36,45,54,63,72,81,90 -- концы блоков строк изображения карт
                i = 0
                k = 0
                self.img_chk1=0
                for ln in range(ln_bgn, ln_end):
                    if k==9:k=0
                    #print(cards_imgs[ln][x_line_suit])
                    if (k>2 and k<6) or k==7:
                        #print(self.x.line_img[k][36:45])
                        if cards_imgs[ln][x_line_suit] == self.x.line_img[k][36:45]:
                            self.img_chk1+=1
                    elif k<=2 or k==6:
                        #print(self.x.line_img[k][27:36])
                        if cards_imgs[ln][x_line_suit] == self.x.line_img[k][27:36]:
                            self.img_chk1+=1
                    i += 1
                    k+=1
        assert self.img_chk1 == 8

    def teardown(self):
        print('All tests has completed!')


if __name__ == '__main__':
    test = Test_Game_fool_card_desc_pytest()
    test.test_Dsc_img_prn()
