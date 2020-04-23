import unittest
from encapsulation import Dice_inc
# https://docs.python.org/3/library/unittest.html

class TestDice_unittest(unittest.TestCase):

    def setUp(self):
        print('Start test !')
        self.dice_game = Dice_inc(3)
        self.dice_game.set_hidden_numbers()

    def tearDown(self):
        self.dice_game.current_throw = 0
        print('Test completed!')
        # обычно происходит освобождение кеша:
        del self.dice_game

    def test_init(self):
        self.assertEqual(self.dice_game.throw_num, 3)
        self.assertFalse(self.dice_game.current_throw > 0)

    def test_dice_setter(self):
        self.dice_game.hidden_num_1 = 5
        self.dice_game.hidden_num_2 = 5
        self.assertTrue((self.dice_game.hidden_num_1 == 5)&(self.dice_game.hidden_num_2 == 5))

        with self.assertRaises(ValueError): #ValueError
            # Код, вызывающий данную ошибку!
            self.dice_game.hidden_num_1 = 8

    def test_throw_dices(self):

        list_throw = []
        list_throw.append(self.dice_game.current_throw)
        self.dice_game.throw_dices()
        list_throw.append(self.dice_game.current_throw)

        self.assertTrue( self.dice_game.current_throw  == 1)
        self.assertListEqual( list_throw, [0,1])