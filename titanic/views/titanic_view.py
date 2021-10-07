import pandas as pd

from titanic.models.dataset import Dataset
from titanic.models.titanic_service import TitanicService
from sklearn.ensemble import RandomForestClassifier

class TitanicView(object):
    dataset = Dataset()
    service = TitanicService()

    def modeling(self):
        this = self.preprocessing()
        self.learning(this)
        return this

    def preprocessing(self) -> object:
        service = self.service
        this = self.dataset
        this.train = service.new_model("train")
        this.test = service.new_model("test")
        this.id = this.test['PassengerId']
        this.label = service.create_label(this)
        this.train = service.create_train(this)
        this = service.embarked_nominal(this)
        this = service.title_nominal(this)
        this = service.gender_nominal(this)
        this = service.age_ordinal(this)
        this = service.fare_ordinal(this)
        this = service.drop_feature(this, 'Name', 'Cabin', 'Sex', 'Age', 'Fare', 'SibSp', 'Parch', 'Ticket')
        # self.print_this(this)
        return this

    def learning(self, this):
        print(f'SKLearn Algorithm Accuracy is {self.service.accuracy_by_classfier(this)}')

    def submit(self):
        this = self.modeling()
        clf = RandomForestClassifier()
        clf.fit(this.train, this.test)
        prediction = clf.predict(this.test)
        pd.DataFrame({'PassengerId' : this.id, 'Survived' : prediction}).to_csv('../data/submission.csv', index=False)


    @staticmethod
    def print_this(this):
        print('*'*100)
        print(f'\nThe Type of Train is {type(this.train)},\nThe Type of Test is  {type(this.test)}')
        print(f'\nThe Columns of Train is {this.train.columns},\nThe Columns of Test is {this.test.columns}')
        print(f'\n Head of Train \n {this.train.head(3)},\n Head of Test \n {this.test.head(3)}')
        print(f'\nNull Count of Train is {this.train.isnull().sum()} '
              f'\nNull Count of Test is {this.test.isnull().sum()}')

