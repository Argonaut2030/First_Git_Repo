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
    
    def add_phone(self, phone):  #  створення методу додавання телефону в список телефонів для класу Record
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
        
    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"
    
class AddressBook(UserDict):
    def add_record (self, new_record):
        self.data[new_record.name.value] = new_record 

    def find(self, name):
        for key in book.data:
            if key == name:
                return book.data[key]
        else :
            None

    def delete(self, name):
        for key in book.data:
            if key == name:
                book.data.pop(name)
                return
        else:
            None 


    def __str__(self):
        if not self.data:
            return "AddressBook is empty."

        records = []
        for name, record in self.data.items():
            records.append("\t- " + str(name) + ": " + str(record))
        return  "AddressBook:\n" + '\n'.join(records)

    
        

book = AddressBook()

john_record = Record("John")
john_record.add_phone("1234567890")
john_record.add_phone("5555555555")




    # # Додавання запису John до адресної книги
book.add_record(john_record)
print(book)
# Створення та додавання нового запису для Jane
jane_record = Record("Jane")
jane_record.add_phone("9876543210")
book.add_record(jane_record)


    # # Виведення всіх записів у книзі
     
print(book)

    # # Знаходження та редагування телефону для John
john = book.find("John")

john.edit_phone("1234567890", "1112223333")

print(john)  # Виведення: Contact name: John, phones: 1112223333; 5555555555

    # # Пошук конкретного телефону у записі John
found_phone = john.find_phone("5555555555")
print(f"{john.name}: {found_phone}")  # Виведення: John: 5555555555

    # # Видалення запису Jane
book.delete("Jane")
print(book)

