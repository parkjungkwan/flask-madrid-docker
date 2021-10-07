'''
국어 kor, 영어 eng, 수학 math 를 입력받아서
평균점수를 통해 A ~ F 학점을 출력하시오
'''
class Grade(object):

    def __init__(self, kor, eng, math):
        self.kor = kor
        self.eng = eng
        self.math = math

    def sum(self):
        return self.kor + self.eng + self.math

    def avg(self):
        return self.sum() / 3






