import unittest
import os
from titanic.models.titanic_service import TitanicService


class TitanicServiceTest(object):

    mock = TitanicService()

    def test_new_model(self) :
        # self.mock.new_model('train.csv')
        print(os.getcwd())

    def count_survived_dead(self, ):
        return []

    def create_train(self):
        return None

    def create_label(self):
        return None

    def drop_feature(self, *feature):
        return None

    def embarked_nominal(self):
        return None

    def fare_oridnal(self):
        return None

    def title_nominal(self):
        return None

    def gender_norminal(self):
        return None

    def age_ordinal(self):
        return None

    def create_k_fold(self):
        return None

    def accuracy_by_classfier(self):
        return None



if __name__ == '__main__':
    unittest.main()