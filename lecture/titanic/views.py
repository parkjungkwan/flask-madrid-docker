from sklearn.ensemble import RandomForestClassifier
import pandas as pd

from lecture.common.models import ValueObject
from lecture.menu.models import print_menu
from lecture.titanic.models import Titanic

if __name__ == '__main__':
    vo = ValueObject()
    titanic = Titanic()
    while 1:
        menu = print_menu(['exit', 'modeling', 'plotting',
                           'preprocessing', 'learning'])
        if menu == 1:
            vo.train = titanic.new_model("train")
            vo.test = titanic.new_model("test")
        elif menu == 2:
            titanic.plot_survived_dead(vo)
            titanic.plot_pclass(vo)
            #titanic.plot_embarked(vo)
            titanic.plot_gender(vo)
        elif menu == 3:
            vo.id = vo.test['PassengerId']
            vo.label = titanic.create_label(vo)
            vo.train = titanic.drop_label(vo)
            vo = titanic.embarked_nominal(vo)
            vo = titanic.title_nominal(vo)
            vo = titanic.gender_nominal(vo)
            vo = titanic.age_ordinal(vo)
            vo = titanic.fare_ordinal(vo)
            vo = titanic.drop_feature(vo, 'Name', 'Cabin', 'Sex', 'Age', 'Fare', 'SibSp', 'Parch', 'Ticket')
        elif menu == 4:
            print(f'SKLearn Algorithm Accuracy is {titanic.accuracy_by_classfier(vo)}')
            print('*' * 100)
            print(f'\nThe Type of Train is {type(vo.train)},\nThe Type of Test is  {type(vo.test)}')
            print(f'\nThe Columns of Train is {vo.train.columns},\nThe Columns of Test is {vo.test.columns}')
            print(f'\n Head of Train \n {vo.train.head(3)},\n Head of Test \n {vo.test.head(3)}')
            print(f'\nNull Count of Train is {vo.train.isnull().sum()} '
                  f'\nNull Count of Test is {vo.test.isnull().sum()}')
            clf = RandomForestClassifier()
            clf.fit(vo.train, vo.test)
            prediction = clf.predict(vo.test)
            pd.DataFrame({'PassengerId': vo.id, 'Survived': prediction}).to_csv('./data/submission.csv', index=False)


        else:
            break





