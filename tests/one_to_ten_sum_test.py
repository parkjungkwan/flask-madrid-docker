import unittest

from book_algorithm_interview.chap_02_program_language.models import OneToTenSum


class OneToTenSumTest(unittest.TestCase):
    mock = OneToTenSum()

    def test_one_to_ten_sum_1(self):
        self.mock.one_to_ten_sum_1()

    def test_one_to_ten_sum_2(self):
        self.mock.one_to_ten_sum_2()


    def test_one_to_ten_sum_3(self):
        self.mock.one_to_ten_sum_3()

if __name__ == '__main__':
    unittest.main()