from titanic.models.dataset import Dataset
import pandas as pd
from sklearn.model_selection import KFold, cross_val_score
from sklearn.ensemble import RandomForestClassifier
import numpy as np

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
    def fare_oridnal(this) -> object:
        this.train['Fare'] = this.train['Fare'].fillna(1)
        this.test['Fare'] = this.test['Fare'].fillna(1)
        this.train['FareBand'] = pd.qcut(this.train['Fare'], 4)
        this.test['FareBand'] = pd.qcut(this.test['Fare'], 4)
        # qcut() 을 사용하면 자동으로 구간을 4등분한다.
        # 타이타닉에서는 bins = [-1, 8, 15, 31, np.inf] 로 구분된다.
        return this

    @staticmethod
    def title_nominal(this) -> object:
        combine = [this.train, this.test]
        for dataset in combine:
            dataset['Title'] = dataset.Name.str.extract('([A-Za-z]+)\.', expand=False)
        for dataset in combine:
            dataset["Title"] = dataset['Title'].replace(['Capt', 'Col', 'Don', 'Dr', 'Major', 'Rev', 'Jonkheer','Dona', 'Mme'], 'Rare')
            dataset["Title"] = dataset['Title'].replace(['Countess', 'Lady', 'Sir'], 'Royal')
            dataset["Title"] = dataset['Title'].replace('Mile', 'Mr')
            dataset["Title"] = dataset['Title'].replace('Ms', 'Miss')
        title_mapping = {'Mr':1 , 'Miss':2, 'Mrs':3, 'Master':4, 'Royal':5, 'Rare':6}
        for dataset in combine:
            dataset['Title'] = dataset['Title'].map(title_mapping)
            dataset['Title'] = dataset['Title'].fillna(0)
        this.train = this.train
        this.test = this.test
        return this
    """
    ['PassengerId', 'Survived', 'Pclass', 'Name', 'Sex', 'Age', 'SibSp',
       'Parch', 'Ticket', 'Fare', 'Cabin', 'Embarked']
    """

    @staticmethod
    def gender_norminal(this) -> object:
        
        sex_mapping = {'male':0, 'female':1}

        return None

    @staticmethod
    def age_ordinal(this) -> object:
        return None

    def create_k_fold(self) -> object:
        return None

    def accuracy_by_classfier(self):
        return None



