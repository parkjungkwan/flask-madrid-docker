import unittest

from titanic.views.titanic_view import TitanicView

class TitanicViewTest(unittest.TestCase):

    def test_modeling(self):
        mock = TitanicView()
        this = mock.preprocessing()
        print(f'The Type of This is {type(this.train)}')
        print(f'The head of Train is \n {this.train.head(2)}')
        print(f'The head of Test is \n {this.test.head(2)}')

    def test_preprocessing(self) -> object:
        service = self.service
        this = self.dataset
        this.train = service.new_model("train")
        this.test = service.new_model("test")
        return this

if __name__ == '__main__':
    unittest.main()
