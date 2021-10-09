import re

import pandas as pd
import numpy as np
import pandas as pd
import numpy as np
import random
import string
np.random.seed(56)
from icecream import ic


class MySeries(object):
    def __init__(self):
        sr = pd.Series({"한국": "서울", "일본": "도쿄", "중국": "베이징"})
        ic(sr)
        '''
        ic| sr: 한국     서울
                일본     도쿄
                중국    베이징
                dtype: object
        '''


class MyPandas(object):
    # noinspection PyMethodMayBeStatic
    def id(self):
        return ''.join(random.choice(string.ascii_letters) for i in range(5))

    # noinspection PyMethodMayBeStatic
    def score(self):
        return np.random.randint(0, 100)

    def __init__(self):
        ic(pd.__version__)
        print('Q1. 다음 결과 출력\n'
                   '   a  b  c\n'
                   '1  1  3  5\n'
                   '2  2  4  6\n')
        df1 = pd.DataFrame({"a": [1, 2], "b": [3, 4], "c": [5, 6]}, index=[1, 2])
        ic(df1)
        '''
        ic| df:    a  b  c
                1  1  3  5
                2  2  4  6
        '''
        print('Q2. 다음 결과 출력\n'
              '   A   B   C\n'
              '1   1   2   3\n'
              '2   4   5   6\n'
              '3   7   8   9\n'
              '4  10  11  12\n')
        df2 = pd.DataFrame([[1, 2, 3],
                            [4, 5, 6],
                            [7, 8, 9],
                            [10, 11, 12]], index=range(1, 5), columns=["A", "B", "C"])
        ic(df2)
        '''
        ic| df2:     A   B   C
                 1   1   2   3
                 2   4   5   6
                 3   7   8   9
                 4  10  11  12
        '''
        print('Q3 두자리 정수를 랜덤으로 2행 3열 데이터프레임을 생성')
        df3 = pd.DataFrame(np.random.randint(10, 100, size=(2, 3)))
        ic(df3)
        '''
        ic| df3:     0   1   2
                 0  85  15  64
                 1  34  14  87
        '''
        print('Q4 국어, 영어, 수학, 사회 4과목을 시험치른 10명의 학생들의 성적표 작성. '
              '단 점수 0 ~ 100이고 학생은 랜덤 알파벳 5자리 ID 로 표기 ')
        ic(self.id())
        ic(self.score())

        df4 = pd.DataFrame([[self.score() for i in range(1, 5)] for i in range(1, 11)],
                           index=[self.id() for i in range(1, 11)],
                           columns=['국어', '영어', '수학', '사회'])
        ic(df4)

        '''
        ic| self.id(): 'MvIZp'
        ic| self.score(): 22
        ic| df4:        국어  영어  수학  사회
                     lzyim  57  90  55  24
                     DyWak  12  66  43  11
                     lZZbx  80  33  89  10
                     gVqqO  31  28  37  34
                     pFcip  15  28  89  19
                     bNdGb  69  41  66  74
                     mlpNX  65  16  13  20
                     kmHNE  44  32   8  29
                     QjAHr  94  78  79  96
                     zkKJk  62  17  75  49
        '''
        print('Q5 4번 문제를 loc 를 통해 동일하게 작성 ')
        df5 = pd.DataFrame({"국어": self.score(), "영어": self.score(), "수학": self.score(), "사회": self.score()},
                           index=[self.id()])
        for i in range(1, 10):
            df5.loc[self.id()] = {"국어": self.score(), "영어": self.score(), "수학": self.score(), "사회": self.score()}

        ic(df5)
        '''
        ic| df5:        국어  영어  수학  사회
                     ROmFm  93  44  14  94
                     GkQZI  25  54  29  10
                     iQMXb  82  65  31  31
                     bFvWW  51  56  56   3
                     crcai  34  32  67  48
                     HShPE  85  24  16   8
                     CcPfg  28  80  52  43
                     StDEl  58  94  93  54
                     LEQiJ  32  50  95   1
                     Llqnx  59  37  80  27
        '''
        # 6 주어진 값으로 DataFrame 객체 생성
        # 6-1 객체내부 정보를 출력
        # 6-2 객체 상위 3열까지 출력
        # 6-3 animal과 age 컬럼만 출력
        # 6-4 객체의 3, 4, 8번 행에 해당하는 animal과 age 값만 출력
        # 6-5 visit 컬럼에서 3 초과하는 값 출력
        # 6-6 age 에서 NaN 값 출력
        # 6-7 age가 3살 미만 고양이값 출력
        # 6-8 age가 2살이상 4살 미만인 값 출력
        # 6-9 f 행의 나이를 1.5살로 변경
        # 6-10 객체에서 visit 의 합 출력
        # 6-11 동물별로 나이의 평균 출력
        # 6-12 k행을 추가하여 dog , 5.5세, 방문회수 2회, 우선권없음(no) 열을 추가
        # 6-13 방금 추가한 열 삭제
        # 6-14 객체에 있는 동물의 종류의 수 출력
        # 6-15 age 는 내림차순, visits 는 오름차순으로 정렬
        # 6-16 priority 의 yes를 True, no 를 False  로 맵핑 후 출력
        # 6-17 snake 를 python 으로 값을 변경
        # 6-18 각각의 동물 유형과 방문 횟수에 대해, 평균나이 출력,
        #            즉,각 행은 animal 이고, 각 열은 visits 이며, 값은 평균연령
        #            (힌트, 피벗 테이블을 활용해야 함)
        print('Q6 주어진 값으로 DataFrame 객체 생성')
        data = {'animal': ['cat', 'cat', 'snake', 'dog', 'dog', 'cat', 'snake', 'cat', 'dog', 'dog'],
                'age': [2.5, 3, 0.5, np.nan, 5, 2, 4.5, np.nan, 7, 3],
                'visits': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
                'priority': ['yes', 'yes', 'no', 'yes', 'no', 'no', 'no', 'yes', 'no', 'no']}
        labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
        df6 = pd.DataFrame(data, index=labels)
        ic(df6)
        '''
        ic| df6:   animal  age  visits priority
                 a    cat  2.5       1      yes
                 b    cat  3.0       3      yes
                 c  snake  0.5       2       no
                 d    dog  NaN       3      yes
                 e    dog  5.0       2       no
                 f    cat  2.0       3       no
                 g  snake  4.5       1       no
                 h    cat  NaN       1      yes
                 i    dog  7.0       2       no
                 j    dog  3.0       1       no
        '''

        print('6-1 객체내부 정보를 출력')
        ic(df6.describe())
        '''
        df6.describe():             
                            age     visits
                    count  8.000000  10.000000
                    mean   3.437500   1.900000
                    std    2.007797   0.875595
                    min    0.500000   1.000000
                    25%    2.375000   1.000000
                    50%    3.000000   2.000000
                    75%    4.625000   2.750000
                    max    7.000000   3.000000
        '''
        
        print('6-2 객체 상위 3열까지 출력')
        ic(df6.iloc[:3])
        '''
        ic| '객체 상위 3열까지 출력'
        ic| df6.iloc[:3]:   
                    animal  age  visits priority
                  a    cat  2.5       1      yes
                  b    cat  3.0       3      yes
                  c  snake  0.5       2       no
        '''
        print('6-3 animal과 age 컬럼만 출력')
        df6.loc[:, ['animal', 'age']]
        '''
        ic| df6.loc[:,['animal','age']]:   
                                    animal  age
                                 a    cat  2.5
                                 b    cat  3.0
                                 c  snake  0.5
                                 d    dog  NaN
                                 e    dog  5.0
                                 f    cat  2.0
                                 g  snake  4.5
                                 h    cat  NaN
                                 i    dog  7.0
                                 j    dog  3.0
        '''
        print('6-4 객체의 3, 4, 8번 행에 해당하는 animal과 age 값만 출력')
        ic(df6.loc[df6.index[[3,4,8]], ['animal','age']])
        print('6-5 visit 컬럼에서 3 초과하는 값 출력')
        ic(df6[df6['visits']>2])
        print('6-6 age 에서 NaN 값 출력')
        ic(df6[df6['age'].isnull()])
        print('6-7 age가 3살 미만 고양이값 출력')
        ic(df6[(df6['age'] <3) & (df6['animal'] =='cat')])
        print('6-8 age가 2살이상 4살 미만인 값 출력')
        ic(df6[df6['age'].between(2,4)])
        print('6-9 f 행의 나이를 1.5살로 변경')
        ic(df6[df6['age'].between(2, 4)])
        print('6-10 객체에서 visit 의 합 출력')
        ic(df6['visits'].sum())
        print('6-11 동물별로 나이의 평균 출력')
        ic(df6.groupby('animal')['age'].mean())
        print('6-12 k행을 추가하여 dog , 5.5세, 방문회수 2회, 우선권없음(no) 열을 추가')
        df6.loc['k'] = ['dog',5.5,2,'no']
        ic(df6)
        print('6-13 방금 추가한 열 삭제')
        df6.drop('k', inplace=True) # del df['k']
        ic(df6)
        print('6-14 객체에 있는 동물의 종류의 수 출력')
        ic(df6['animal'].value_counts())
        print('6-15 age 는 내림차순, visits 는 오름차순으로 정렬')
        ic(df6.sort_values(by=['age','visits'], ascending=[False, True]))
        print('6-16 priority 의 yes를 True, no 를 False  로 맵핑 후 출력')
        df6['priority'] = df6['priority'].map({'yes': True, 'no': False})
        ic(df6)
        print('6-17 snake 를 python 으로 값을 변경')
        df6['animal'] = df6['animal'].replace('snake', 'python')
        ic(df6)
        print('6-18 각각의 동물 유형과 방문 횟수에 대해, 평균나이 출력, \n'
           '즉,각 행은 animal 이고, 각 열은 visits 이며, 값은 평균연령 \n'
           '(힌트, 피벗 테이블을 활용해야 함)')
        df6 = df6.pivot_table(index='animal', columns='visits', values='age', aggfunc='mean')
        ic(df6)
        print('Q7. 키값 A와 중복된 값이 제거된 1,2,3,4,5,6,7 이 출력')
        df7 = pd.DataFrame({'A': [1, 2, 2, 3, 4, 5, 5, 5, 6, 7, 7]})
        df7 = df7.drop_duplicates()
        ic(type(df7['A']))
        ic(df7)
        '''
        ic| type(df7['A']): <class 'pandas.core.series.Series'>
        ic| df7:    A
                 0  1
                 1  2
                 3  3
                 4  4
                 5  5
                 8  6
                 9  7
        '''
        print('Q8. 행의 각 요소에서 행의 평균을 뺀 값을 출력하되 부분집합으로 가로출력')
        df8 = pd.DataFrame(np.random.random(size=(5, 3)))
        df8 = df8.sub(df8.mean(axis=1), axis=0)
        ic(df8)
        '''
                 0 -0.095803 -0.151800  0.247603
                 1 -0.254548  0.229442  0.025106
                 2 -0.134566  0.409687 -0.275121
                 3  0.340665  0.224261 -0.564927
                 4  0.059283  0.010734 -0.070017
        '''
        print('Q9. 가장 작은 합계를 가진 숫자열의 열을 출력(최대값은 max)')
        df9 = pd.DataFrame(np.random.random(size=(5, 10)), columns=list('abcdefghij'))
        ic(df9.sum().idxmax())
        '''ic| df9.sum().idxmax(): 'b'''
        print('Q10. 중복된 값이 없는 유니크한 열의 카운트 출력(중복되지 않은 행은 몇 개..)')
        df10 = pd.DataFrame(np.random.randint(0, 2, size=(10, 3)))
        ic(df10)
        '''
        ic| df10:    0  1  2
                  0  1  0  0
                  1  1  1  1
                  2  1  0  1
                  3  0  1  1
                  4  1  0  0
                  5  1  1  1
                  6  0  1  1
                  7  0  0  1
                  8  0  1  0
                  9  0  1  1
        '''
        ic(len(df10) - df10.duplicated(keep=False).sum())
        '''
        ic| len(df10) - df10.duplicated(keep=False).sum(): 3
        '''
        df10 = df10.drop_duplicates(keep=False)
        ic(df10)
        '''
        ic| df10.drop_duplicates(keep=False):    
                                         0  1  2
                                      2  1  0  1
                                      7  0  0  1
                                      8  0  1  0
        '''

        print('Q11. 체의 각 행에 대해 세번째 NaN 값이 들어 있는 열을 찾으시오. 일련의 열 레이블을 반환해야 합니다.')
        nan = np.nan
        data = [[0.04, nan, nan, 0.25, nan, 0.43, 0.71, 0.51, nan, nan],
                [nan, nan, nan, 0.04, 0.76, nan, nan, 0.67, 0.76, 0.16],
                [nan, nan, 0.5, nan, 0.31, 0.4, nan, nan, 0.24, 0.01],
                [0.49, nan, nan, 0.62, 0.73, 0.26, 0.85, nan, nan, nan],
                [nan, nan, 0.41, nan, 0.05, nan, 0.61, nan, 0.48, 0.68]]
        columns = list('abcdefghij')
        df11 = pd.DataFrame(data, columns=columns)
        ic(type(df11.isnull()))
        df11 = (df11.isnull().cumsum(axis=1) == 3).idxmax(axis=1)
        ic(df11)
        '''
        <class 'pandas.core.frame.DataFrame'>
        0    e
        1    c
        2    d
        3    h
        4    d
        dtype: object
        '''
        print('Q12. grps 에서 a, b, c 별로 가장 큰 값')
        df12 = pd.DataFrame({'grps': list('aaabbcaabcccbbc'),
                           'vals': [12, 345, 3, 1, 45, 14, 4, 52, 54, 23, 235, 21, 57, 3, 87]})
        ic(type(df12.groupby('grps'))) # DataFrameGroupBy
        ic(type(df12.groupby('grps')['vals'])) # SeriesGroupBy
        df12 = df12.groupby('grps')['vals'].max()
        ic(df12)
        '''
        grps
        a    345
        b     57
        c    235
        Name: vals, dtype: int64
        '''





class Crime(object):
    def __init__(self):
        df = pd.read_csv('./data/police_positions.csv', encoding='UTF-8', thousands=',')
        # 발생 합치기
        # print(df.info())
        df2 = pd.pivot_table(df, index='구별', aggfunc=np.sum)
        # print(df2.head(3))
        df2.drop(columns={'살인 검거', '강도 검거', '강간 검거', '절도 검거', '폭력 검거'}, axis=1, inplace=True)
        #for i in ['살인 발생', '강도 발생', '강간 발생', '절도 발생', '폭력 발생']:
        #    print(df.loc[df[i]])

        print(df2.loc['강남구'])


if __name__ == '__main__':
    # MySeries()
    MyPandas()
    # Crime()
