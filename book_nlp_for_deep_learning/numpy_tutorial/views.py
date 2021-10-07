from book_nlp_for_deep_learning.numpy_tutorial.models import IntegerTutorial, NumpyTutorial

if __name__ == '__main__':
    a = NumpyTutorial()
    # show_numpy()
    # numpy_choice()
    # numpy_not_need_for_loop()
    # indexing_slicing()
    # np_zeors()
    a.np_ones()
    # np_eye()
    # np_arange()
    # np_linspace()
    # np_mask()
    # np_bubble()
    b = IntegerTutorial()
    while 1:
        menu = input('\n0-Exit \n1-Integer Checker\n')
        if menu == '0':
            break
        elif menu == '1':
            ls = [1, 3, 6, 3, 8, 7, 13, 23, 13, 2, 3.14, 2, 3, 7]
            for i in ls:
                b.integer_checker(i)