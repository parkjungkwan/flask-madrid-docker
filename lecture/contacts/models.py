"""
name, phone, email, address
"""


class Contacts(object):
    def __init__(self, name, phone, email, address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address

    def to_string(self):
        print(f'{self.name}, {self.phone}, {self.email}, {self.address}')

    @staticmethod
    def set_contact() -> object:
        return Contacts(input('name'),input('phone'),input('email'),input('address'))

    @staticmethod
    def get_contacts(ls):
        for i in ls:
            i.to_string()

    @staticmethod
    def del_contact(ls, name):
        for i, j in enumerate(ls):
            if name == j.name:
                del ls[i]






