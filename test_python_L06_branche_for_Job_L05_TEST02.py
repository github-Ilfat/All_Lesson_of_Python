#PYTEST "test_python_L06_branche_for_Job_L05_TEST02.py"
#PRJ_PATH='C:\Users\AI_user\PycharmProjects\Python_course\All_Lesson_of_Python\L05_packet_dir'
from L05_packet_dir.Jobs_from_L05_divisor_master import check_nuber

# исследуемое число:
#1, 2,  3,  111,    222,    500,    750,    996,    997,    998,    999,    1000
# результат - максимальный простой делитель исследуемого числа:
#1, 2,  3,  37,     37,     5,      5,      83,     997,    499,    37,     5
def test_1_check_nuber():
    assert check_nuber(1) == 1
def test_2_check_nuber():
    assert check_nuber(2) == 2
def test_3_check_nuber():
    assert check_nuber(3) == 3
def test_4_check_nuber():
    assert check_nuber(111) == 37
def test_5_check_nuber():
    assert check_nuber(222) == 37
def test_6_check_nuber():
    assert check_nuber(500) == 5
def test_7_check_nuber():
    assert check_nuber(750) == 5
def test_8_check_nuber():
    assert check_nuber(996) == 83
def test_9_check_nuber():
    assert check_nuber(997) == 997
def test_10_check_nuber():
    assert check_nuber(998) == 499
def test_11_check_nuber():
    assert check_nuber(999) == 37
def test_12_check_nuber():
    assert check_nuber(1000) == 5
