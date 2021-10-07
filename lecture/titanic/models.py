import pandas as pd
from sklearn.model_selection import KFold, cross_val_score
from sklearn.ensemble import RandomForestClassifier
import numpy as np

from matplotlib import font_manager, rc
import seaborn as sns
import matplotlib.pyplot as plt

from lecture.common.models import ValueObject

rc('font', family = font_manager.FontProperties(fname='C:/Windows/Fonts/H2GTRE.ttf').get_name())
"""
Titanic's features
PassengerId,Survived,Pclass,Name,Sex,Age,SibSp,Parch,Ticket,Fare,Cabin,Embarked

['PassengerId', 'Survived', 'Pclass', 'Name', 'Sex', 'Age', 'SibSp',
   'Parch', 'Ticket', 'Fare', 'Cabin', 'Embarked']
"""
class Titanic(object):

    vo = ValueObject()

    def new_model(self, fname) -> object:
        return pd.read_csv(f"./data/{fname}.csv")

    def create_label(self, vo) -> object:
        return vo.train['Survived']

    def drop_label(self, vo) -> object:
        return vo.train.drop('Survived', axis=1)

    def drop_feature(self, vo, *feature) -> object:
        for i in feature:
            vo.train = vo.train.drop([i], axis=1)
            vo.test = vo.test.drop([i], axis=1)
        return vo

    def plot_survived_dead(self, vo):
        this = vo.train
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

    def plot_pclass(self, vo):
        this = vo.train
        this['생존결과'] = this['Survived'].replace(0,'사망자').replace(1,'생존자')
        this['좌석등급'] = this['Pclass'].replace(1,'1등석').replace(2,'2등석').replace(3,'3등석')
        sns.countplot(data=this, x='좌석등급', hue='생존결과')
        plt.show()

    def plot_embarked(self, vo):
        # 승선항구 C: 쉘버그, S: 사우스햄튼, Q: 퀸즈타운
        this = vo.train
        this['생존결과'] = this['Survived'].replace(0, '사망자').replace(1, '생존자')
        this['좌석등급'] = this['Embarked'].replace("C", "쉘버그").replace("S", "사우스햄튼").replace("Q", "퀸즈타운")
        sns.countplot(data=this, x='승선항구', hue='생존결과')
        plt.show()

    def plot_gender(self, vo):
        this = vo.train
        f, ax = plt.subplots(1, 2, figsize= (18, 8))
        male_series = this['Survived'][this['Sex'] == 'male'].value_counts()
        female_series = this['Survived'][this['Sex'] == 'female'].value_counts()
        male_series.plot.pie(explode=[0, 0.1], autopct='%1.1f%%', ax=ax[0], shadow=True)
        female_series.plot.pie(explode=[0, 0.1], autopct='%1.1f%%', ax=ax[1], shadow=True)
        ax[0].set_title('남성의 생존비율 0.사망자 vs 1.생존자')
        ax[1].set_title('여성의 생존비율 0.사망자 vs 1.생존자')
        plt.show()




    def embarked_nominal(self, this) -> object:
        this.train = this.train.fillna({'Embarked':'S'})
        this.test = this.test.fillna({'Embarked': 'S'})
        this.train['Embarked'] = this.train['Embarked'].map({'S': 1, 'C': 2, 'Q': 3})
        this.test['Embarked'] = this.test['Embarked'].map({'S': 1, 'C': 2, 'Q': 3})
        return this

    def fare_ordinal(self, this) -> object:
        this.train['Fare'] = this.train['Fare'].fillna(1)
        this.test['Fare'] = this.test['Fare'].fillna(1)
        this.train['FareBand'] = pd.qcut(this.train['Fare'], 4, labels={1, 2, 3, 4})
        this.test['FareBand'] = pd.qcut(this.test['Fare'], 4, labels={1, 2, 3, 4})
        # qcut() 을 사용하면 자동으로 구간을 4등분한다.
        # 타이타닉에서는 bins = [-1, 8, 15, 31, np.inf] 로 구분된다.
        return this

    def title_nominal(self, this) -> object:
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

    def gender_nominal(self, this) -> object:
        combine = [this.train, this.test]
        sex_mapping = {'male':0, 'female':1}
        for dataset in combine:
            dataset['Gender'] = dataset['Sex'].map(sex_mapping)
        return this

    def age_ordinal(self, this) -> object:
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


    def create_k_fold(self) -> object:
        return KFold(n_splits=10, shuffle=True, random_state=0)


    def accuracy_by_classfier(self, this):
        score = cross_val_score(RandomForestClassifier(),
                                this.train,
                                this.label,
                                cv=self.create_k_fold(),
                                n_jobs=1,
                                scoring='accuracy')
        return round(np.mean(score) * 100, 2)





