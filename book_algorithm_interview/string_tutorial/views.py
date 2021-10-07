from book_algorithm_interview.string_tutorial.models import str_to_list, reverse_list, list_to_str

if __name__ == '__main__':
    ls = str_to_list(input("Input"))
    resversed_ls = reverse_list(ls)
    print(list_to_str(resversed_ls))