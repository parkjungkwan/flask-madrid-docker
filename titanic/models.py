from titanic.views import Dataset
import pandas as pd
from sklearn.model_selection import KFold, cross_val_score
from sklearn.ensemble import RandomForestClassifier
import numpy as np

from matplotlib import font_manager, rc
import seaborn as sns
import matplotlib.pyplot as plt
rc('font', family = font_manager.FontProperties(fname='C:/Windows/Fonts/H2GTRE.ttf').get_name())
"""
Titanic's features
PassengerId,Survived,Pclass,Name,Sex,Age,SibSp,Parch,Ticket,Fare,Cabin,Embarked

['PassengerId', 'Survived', 'Pclass', 'Name', 'Sex', 'Age', 'SibSp',
   'Parch', 'Ticket', 'Fare', 'Cabin', 'Embarked']
"""
class TitanicService(object):

    dataset = Dataset()

    def new_model(self, payload) -> object:
        return pd.read_csv(f"/data/{payload}.csv")

    @staticmethod
    def create_train(this) -> object:
        return this.train.drop('Survived', axis=1)
    @staticmethod
    def create_label(this) -> object:
        return this.train['Survived']

    @staticmethod
    def drop_feature(this, *feature) -> object:
        for i in feature:
            this.train = this.train.drop([i], axis=1)
            this.test = this.test.drop([i], axis=1)
        return this

    @staticmethod
    def embarked_nominal(this) -> object:
        this.train = this.train.fillna({'Embarked':'S'})
        this.test = this.test.fillna({'Embarked': 'S'})
        this.train['Embarked'] = this.train['Embarked'].map({'S': 1, 'C': 2, 'Q': 3})
        this.test['Embarked'] = this.test['Embarked'].map({'S': 1, 'C': 2, 'Q': 3})
        return this

    @staticmethod
    def fare_ordinal(this) -> object:
        this.train['Fare'] = this.train['Fare'].fillna(1)
        this.test['Fare'] = this.test['Fare'].fillna(1)
        this.train['FareBand'] = pd.qcut(this.train['Fare'], 4, labels={1, 2, 3, 4})
        this.test['FareBand'] = pd.qcut(this.test['Fare'], 4, labels={1, 2, 3, 4})
        # qcut() 을 사용하면 자동으로 구간을 4등분한다.
        # 타이타닉에서는 bins = [-1, 8, 15, 31, np.inf] 로 구분된다.
        return this

    @staticmethod
    def title_nominal(this) -> object:
        combine = [this.train, this.test]
        title_mapping = {'Mr': 1, 'Miss': 2, 'Mrs': 3, 'Master': 4, 'Royal': 5, 'Rare': 6}
        for dataset in combine:
            dataset['Title'] = dataset.Name.str.extract('([A-Za-z]+)\.', expand=False)
        for dataset in combine:
            dataset['Title'] = dataset['Title'].replace(
                ['Capt', 'Col', 'Don', 'Dr', 'Major', 'Rev', 'Jonkheer', 'Dona', 'Mme'], 'Rare')
            dataset['Title'] = dataset['Title'].replace(['Countess', 'Lady', 'Sir'], 'Royal')
            dataset['Title'] = dataset['Title'].replace('Mlle', 'Mr')
            dataset['Title'] = dataset['Title'].replace('Ms', 'Miss')
            dataset['Title'] = dataset['Title'].fillna(0)
            dataset['Title'] = dataset['Title'].map(title_mapping)
        return this

    @staticmethod
    def gender_nominal(this) -> object:
        combine = [this.train, this.test]
        sex_mapping = {'male':0, 'female':1}
        for dataset in combine:
            dataset['Gender'] = dataset['Sex'].map(sex_mapping)
        return this

    @staticmethod
    def age_ordinal(this) -> object:
        train = this.train
        test = this.test
        train['Age'] = train['Age'].fillna(-0.5)
        test['Age'] = test['Age'].fillna(-0.5)
        bins = [-1, 0, 5, 12, 18, 24, 35, 60, np.inf]
        labels = ['Unknown','Baby','Child','Teenager','Student','Young Adult','Adult', 'Senior']
        age_mapping = {'Unknown': 0, 'Baby': 1, 'Child': 2, 'Teenager': 3, 'Student': 4, 'Young Adult': 5, 'Adult': 6,
                       'Senior': 7}
        for i in train, test:
            i['AgeGroup'] = pd.cut(i['Age'], bins=bins, labels=labels)
            i['AgeGroup'] = i['AgeGroup'].map(age_mapping)
        return this

    @staticmethod
    def create_k_fold() -> object:
        return KFold(n_splits=10, shuffle=True, random_state=0)


    def accuracy_by_classfier(self, this):
        score = cross_val_score(RandomForestClassifier(),
                                this.train,
                                this.label,
                                cv=self.create_k_fold(),
                                n_jobs=1,
                                scoring='accuracy')
        return round(np.mean(score) * 100, 2)


class Plot(object):
    dataset = Dataset()
    service = Service()

    def __init__(self):
        self.df = self.service.new_model('train.csv') # object is dataframe

    def show_plot_survived_dead(self):
        this = self.df
        f, ax = plt.subplots(1, 2, figsize= (18, 8))
        series = this['Survived'].value_counts()
        print(type(series))
        print(series)
        series.plot.pie(explode=[0,0.1], autopct='%1.1f%%', ax=ax[0], shadow=True)
        ax[0].set_title('0.사망자 vs 1.생존자')
        ax[0].set_ylabel('')
        ax[1].set_title('0.사망자 vs 1.생존자')
        sns.countplot('Survived', data=this, ax=ax[1])
        plt.show()

    def show_plot_pclass(self):
        this = self.df
        this['생존결과'] = this['Survived'].replace(0,'사망자').replace(1,'생존자')
        this['좌석등급'] = this['Pclass'].replace(1,'1등석').replace(2,'2등석').replace(3,'3등석')
        sns.countplot(data=this, x='좌석등급', hue='생존결과')
        plt.show()

    def show_plot_embarked(self):
        # 승선항구 C: 쉘버그, S: 사우스햄튼, Q: 퀸즈타운
        this = self.df
        this['생존결과'] = this['Survived'].replace(0, '사망자').replace(1, '생존자')
        this['좌석등급'] = this['Embarked'].replace("C", "쉘버그").replace("S", "사우스햄튼").replace("Q", "퀸즈타운")
        sns.countplot(data=this, x='승선항구', hue='생존결과')
        plt.show()

    def show_plot_sex(self):
        this = self.df
        f, ax = plt.subplots(1, 2, figsize= (18, 8))
        male_series = this['Survived'][this['Sex'] == 'male'].value_counts()
        female_series = this['Survived'][this['Sex'] == 'female'].value_counts()
        male_series.plot.pie(explode=[0, 0.1], autopct='%1.1f%%', ax=ax[0], shadow=True)
        female_series.plot.pie(explode=[0, 0.1], autopct='%1.1f%%', ax=ax[1], shadow=True)
        ax[0].set_title('남성의 생존비율 0.사망자 vs 1.생존자')
        ax[1].set_title('여성의 생존비율 0.사망자 vs 1.생존자')
        plt.show()

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
