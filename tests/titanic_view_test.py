import unittest

from lecture.titanic import TitanicView

class TitanicViewTest(unittest.TestCase):
    mock = TitanicView()

    def test_modeling(self):
        self.mock.modeling()

if __name__ == '__main__':
    unittest.main()
