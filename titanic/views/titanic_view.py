from titanic.models.dataset import Dataset
from titanic.models.titanic_service import TitanicService


class TitanicView(object):
    dataset = Dataset()
    service = TitanicService()

    def modeling(self):
        this = self.preprocessing()
        return this

    def preprocessing(self) -> object:
        service = self.service
        this = self.dataset
        this.train = service.new_model("train")
        this.test = service.new_model("test")
        this.id = this.test['PassengerId']
        this = service.embarked_nominal(this)
        this = service.title_nominal(this)
        this = service.age_ordinal(this)
        this = service.gender_norminal(this)
        this = service.drop_feature(this, 'Name', 'Cabin', 'Sex', 'Age', 'Fare')
        self.print_this(this)
        return this

    @staticmethod
    def print_this(this):
        print('*'*100)
        print(f'The Type of Train is {type(this.train)},The Type of Test is  {type(this.test)}')
        print(f'The Columns of Train is {this.train.columns},The Columns of Test is {this.test.columns}')
        print(f'Top Row of Train is {this.train.head(1)}, Top Row of Test is {this.test.head(1)}')
        print(f'Null Count of Train is {this.train.isnull().sum()}, '
              f'Null Count of Test is {this.test.isnull().sum()}')
