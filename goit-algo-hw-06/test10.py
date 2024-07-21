from collections import UserDict

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    def __init__(self, value):
        super().__init__(value)
        self.name = value

class Phone(Field):
      def __init__(self, value):
         super().__init__(value)  # Викликаємо конструктор базового класу
         if not value.isdigit() or len(value) != 10:
           print("Invalid phone number format")
         self.phone = value
class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
    
    def add_phone(self, phone):
        phone_obj = Phone(phone)
        self.phones.append(phone_obj)
   
    def remove_phone(self, phone_del):
        for i, phone in enumerate(self.phones):  
            if self.phones[i].value == phone_del:
                del self.phones[i]  
                return  
        else :
            raise ValueError

        

    def edit_phone (self, phone_del, phone_new) :
        for i, phone in enumerate(self.phones):  
            if self.phones[i].value == phone_del:
                self.phones[i] = Phone(phone_new)
                return  
        else:
            raise ValueError
     
    def find_phone(self, phone_f):
        for i, phone in enumerate(self.phones):  
                if self.phones[i].value == phone_f:
                    return self.phones[i]              
        else:
            return None



# book = AddressBook()

john_record = Record("John")
john_record.add_phone("1234567890")
john_record.add_phone("5555555555")
# john_record.edit_phone("5555555555", "6666666666")
# john_record.remove_phone("6666666666")
# print(john_record.phones[1].value)

print(john_record.find_phone("8888888888"))
# print(john_record.phones)


# print(john_record.name)
# print(john_record.phones)
