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

    @staticmethod
    def main():
        kor = int(input('Korean: '))
        eng = int(input('English: '))
        math = int(input('Math: '))
        grade = Grade(kor, eng, math)
        avg = grade.avg()
        if avg >= 90:
            result = 'A'
        elif avg >= 80:
            result = 'B'
        elif avg >= 70:
            result = 'C'
        elif avg >= 60:
            result = 'D'
        elif avg >= 50:
            result = 'E'
        else:
            result = 'F'
        print(f'{result}')

Grade.main()

"""
학생이름, 국어 kor, 영어 eng, 수학 math 를 입력받아서
학생이름, 평균, 학점을 출력하시오
"""
class GradeWithName(object):

    def __init__(self, name):
        self.name = name
        self.scores = []

    def addScores(self, score):
        self.scores.append(score)

    def avg(self):
        return sum(self.scores) / len(self.scores)


def main():
    grade = GradeWithName(input('Input Student Name:'))
    for i in ['Korean','English','Math']:
        grade.addScores(int(input(f'{i}: ')))
    avg = grade.avg()
    if avg >= 90:
        result = 'A'
    elif avg >= 80:
        result = 'B'
    elif avg >= 70:
        result = 'C'
    elif avg >= 60:
        result = 'D'
    elif avg >= 50:
        result = 'E'
    else:
        result = 'F'
    print(f'{result}')


if __name__ == '__main__':
    main()



"""
이름, 나이, 주소를 입력받아서 자기 소개하는 프로그램을 작성하시오.
출력은 안녕하세요, 제 이름은 Tom 이고, 나이는 28세이고, 서울에서 거주합니다. 로 됩니다.
이때, 여러 사람이면 전부 입력 받아서 전체가 일괄 출력되는 시스템이어야 합니다.
"""

class Person(object):
    def __init__(self,name,age,address):
        self.name = name
        self.age = age
        self.address = address
    def to_string(self):
        print(f'이름{self.name},나이{self.age},사는곳{self.address}')

def main():
    persons = []
    while 1:
        menu = input('0-EXIT 1- Add 2- Print')
        if menu == '0':
            return
        elif menu == '1':
            persons.append(Person(input('name'),input('age'),input('address')))
        elif menu == '2':
            for i in persons:
                i.to_string()


if __name__ == '__main__':
    main()


