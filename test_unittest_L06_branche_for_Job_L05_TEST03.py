#UNITTEST "test_unittest_L06_branche_for_Job_L05_TEST03.py"
#PRJ_PATH='C:\Users\AI_user\PycharmProjects\Python_course\All_Lesson_of_Python\L05_packet_dir'
from L05_packet_dir.Jobs_from_L05_divisor_master import check_nuber

# исследуемое число:
#1, 2,  3,  111,    222,    500,    750,    996,    997,    998,    999,    1000
# результат - максимальный простой делитель исследуемого числа:
#1, 2,  3,  37,     37,     5,      5,      83,     997,    499,    37,     5

import unittest

class Test_check_nuber(unittest.TestCase):
    def test_simple_1(self):
        self.assertEqual(check_nuber(1),1)

class Test_check_nuber(unittest.TestCase):
    def test_simple_2(self):
        self.assertEqual(check_nuber(500),5)

class Test_check_nuber(unittest.TestCase):
    def test_simple_3(self):
        self.assertEqual(check_nuber(999),37)


