class OneToTenSum(object):
    def one_to_ten_sum_1(self):
        sum = 0
        for i in range(1, 11):
            sum += i
        print(sum)

    def one_to_ten_sum_2(self):
        print(sum(i for i in range(1,11)))


    def one_to_ten_sum_3(self):
        print(sum(range(1, 11)))
