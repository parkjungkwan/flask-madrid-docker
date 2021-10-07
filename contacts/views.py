from contacts.models import Contacts
from menu.models import print_menu

if __name__ == '__main__':
    # ls = ['0-exit', '1-add', '2-print', '3-delete']
    # ls2 = ['exit', 'add', 'print', 'delete']
    # print(menu(ls2))
    ls = []
    while 1:
        menu = print_menu(['exit', 'add', 'print', 'delete'])
        if menu == 1:
            t = Contacts.set_contact()
            ls.append(t)
        elif menu == 2:
            Contacts.get_contacts(ls)
        elif menu == 3:
            Contacts.del_contact(ls, input('Del Name'))
        else:
            break