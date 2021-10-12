import pandas as pd
from icecream import ic

class Conversion(object):
    def __init__(self):
        print('자료구조 타입변환 예제')
        print('Q1. 1부터 9까지 요소를 갖는 튜플 생성')
        tpl = self.create_tuple()
        ic(type(tpl))
        ic(tpl)
        print('Q2. 튜플을 리스트로 전환')
        lst = self.tuple_to_list(tpl)
        ic(type(lst))
        ic(lst)
        print('Q3. 리스트의 int 값을 float 로 전환')
        lst = self.int_to_float(lst)
        ic(type(lst))
        ic(lst)
        print('Q4. float 리스트를 int 리스트 로 전환')
        lst = self.float_to_int(lst)
        ic(type(lst))
        ic(lst)
        print('Q5. int 리스트를 딕셔너리로 전환. 단 키값은 int 를 str 로 변환시켜서 활용함')
        dic = self.list_to_dictionary(lst)
        ic(type(dic))
        ic(dic)
        print('Q6. "hello"를 가진 튜플생성')
        tpl = self.hello_to_tuple('hello')
        ic(type(tpl))
        ic(tpl)
        print('Q7. 6번 튜플을 리스트로 전환')
        lst = self.dictionary_to_dataframe(tpl)
        ic(type(lst))
        ic(lst)
        print('Q8. 5번 딕셔너리를 dataframe 으로 전환, orient 속성값으로 인덱스 지정')
        df = self.dictionary_to_dataframe(dic)
        ic(type(df))
        ic(df)
    # Q1. 1부터 9까지 요소를 갖는 튜플 생성
    def create_tuple(self) -> ():
        return (1,2,3,4,5,6,7,8,9)
    # Q2. 튜플을 리스트로 전환
    def tuple_to_list(self, tpl) -> []:
        a = []
        for i in tpl:
            a.append(i)
        return [i for i in tpl]
    # Q3. 리스트의 int 값을 float 로 전환
    def int_to_float(self, lst) -> []:
        a = []
        for i in lst:
            a.append(float(i))
        return [float(i) for i in lst]
    # Q4. float 리스트를 int 리스트 로 전환
    def float_to_int(self, lst) -> []:
        a = []
        for i in lst:
            a.append(int(i))
        return [int(i) for i in lst]
    # Q5. int 리스트를 딕셔너리로 전환. 단 키값은 int 를 str 로 변환시켜서 활용함.
    def list_to_dictionary(self, lst) -> {}:
        return { str(i) : i for i in lst}

    def hello_to_tuple(self,param:str) -> ():
        a = ()

        return a

    def hello_to_list(self, tpl ) -> []:
        a = []
        for i in tpl:
            a.append(i)
        return a

    def dictionary_to_dataframe(self) -> object:
        df = pd.DataFrame()

        return df

if __name__ == '__main__':
    Conversion()