import unittest


class PalindromeTest(unittest.TestCase):
    def test_str_to_list(self):
        ls = [i for i in "A man, a plan, a canal: Panama" if i.isalnum()]
        print(f'test_str_to_list : {ls}')

    def test_isPalindrome(self) -> bool:
        ls = [i for i in "A man, a plan, a canal: Panama" if i.isalnum()]
        dict = {"RESULT": False for i in ls if ls.pop(0) != ls.pop()}
        print(f'test_isPalindrome : {dict["RESULT"]}')


if __name__ == '__main__':
    unittest.main()
