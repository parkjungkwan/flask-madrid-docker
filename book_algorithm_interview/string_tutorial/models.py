
class Palindrome(object):
    def str_to_list(payload: str) -> [] :
        return [i for i in payload if i.isalnum()]


    def isPalindrome(ls: []) -> bool:
        return {"RESULT": False for i in ls if ls.pop(0) != ls.pop()}

def str_to_list(payload: str) -> []:
    return []

def reverse_list(ls: []) -> []:
    return []

def list_to_str(ls: []) -> str:
    return ''

if __name__ == '__main__':
    ls = str_to_list(input("Input"))
    resversed_ls = reverse_list(ls)
    print(list_to_str(resversed_ls))