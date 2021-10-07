from lecture.grade.models import Grade

if __name__ == '__main__':
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
