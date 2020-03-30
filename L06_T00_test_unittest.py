import unittest
fib_num = lambda n: fib_num(n-1)+ fib_num(n-2) if n > 2 else 1



class TestFibNum(unittest.TestCase):
    def test_simple_1(self):
        self.assertEqual(fib_num(3),2)

    def test_simple_2(self):
        self.assertTrue(fib_num(5) < 3)

    def test_simple_3(self):
        self.assertFalse(fib_num(5) < 3)