import unittest

from basic.olympic_medals import OlympicMedals


class OlympicMedalsTest(unittest.TestCase):

    mock = OlympicMedals()

    def test_read_wiki(self):
        self.mock.read_wiki()

if __name__ == '__main__':
    unittest.main()