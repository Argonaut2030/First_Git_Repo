from collections import UserDict
from datetime import datetime,date,timedelta



def string_to_date(date_string):
    return datetime.strptime(date_string, "%d.%m.%Y").date()


def date_to_string(date):
    return date.strftime("%Y.%m.%d")


def find_next_weekday(start_date, weekday):
    days_ahead = weekday - start_date.weekday()
    if days_ahead <= 0:
        days_ahead += 7
    return start_date + timedelta(days=days_ahead)


def adjust_for_weekend(birthday):
    if birthday.weekday() >= 5:
        return find_next_weekday(birthday, 0)
    return birthday

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Birthday(Field):
    def __init__(self, value):
        super().__init__(value)
        
        try:
            date_format = "%d.%m.%Y"
            self.birthday = datetime.strptime(value, date_format).date()
                      
        except ValueError:
            raise ValueError("Invalid date format. Use DD.MM.YYYY")


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
        self.birthday = None
    
    def add_phone(self, phone):  #  створення методу додавання телефону в список телефонів для класу Record
        phone_obj = Phone(phone)
        self.phones.append(phone_obj)

    def add_birthday(self, date_string):
        self.birthday = Birthday(date_string)

   
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
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}, birthday:  { self.birthday}"
    
class AddressBook(UserDict):
    def add_record (self, new_record): 
        self.data[new_record.name.value] = new_record 

    def find(self, name):
        for key in self.data:
            if key == name:
                return self.data[key]
        else :
            None

    def delete(self, name):
        for key in self.data:
            if key == name:
                self.data.pop(name)
                return
        else:
            None 



#  Get_Birthdays *****************************


    def prepare_user_list(user_data):
        prepared_list = []
        for user in user_data:
            prepared_list.append({"name": user["name"], "birthday": string_to_date(user["birthday"])})
        return prepared_list

        
    def get_upcoming_birthdays(self, days=7):
        upcoming_birthdays = []
        today = date.today()

        for key in self.data:
            record = self.data[key]
            b = string_to_date(record.birthday.value)
           
            birthday_this_year =  b.replace(year=today.year)  
                  #user["birthday"].replace(year=today.year)
        
            """
            Додайте на цьому місці перевірку, чи не буде 
            припадати день народження вже наступного року.
            """
            if birthday_this_year < today:
                birthday_this_year = b.replace(year=today.year+1)
                

            if 0 <= (birthday_this_year - today).days <= days:
                """ 
                Додайте перенесення дати привітання на наступний робочий день,
                якщо день народження припадає на вихідний. 
                """
                birthday_this_year =  adjust_for_weekend(birthday_this_year)
                congratulation_date_str = date_to_string(birthday_this_year)
                upcoming_birthdays.append({"name": record.name.value, "congratulation_date":congratulation_date_str})
        return  upcoming_birthdays





# ********************************



    def __str__(self):
        if not self.data:
            return "AddressBook is empty."


        records = []
        for name, record in self.data.items():
            records.append("\t- " + str(name) + ": " + str(record))
        return  "AddressBook:\n" + '\n'.join(records)

    
        

def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me name and phone please."
        except KeyError:
            return f" Contact {args[0]} doesn't exist."
        
        try:
            return func (*args)
           
        except IndexError:
            return f"Give me the name"

    return inner




@input_error
def add_contact(args, book: AddressBook):
    name, phone, *_ = args
    record = book.find(name)
    message = "Contact updated."
    if record is None:
        record = Record(name)
        book.add_record(record)
        message = "Contact added."
    if phone:
        record.add_phone(phone)
    return message


@input_error
def change_contact(args, book):
    name, phone = args
    # try:
    book.pop(name)
    book[name] = phone
    return "Contact changed."   

@input_error
def add_birthday2(args, book: AddressBook):
    name, date_string = args
    record = book.find(name)
  
   
    if record:
        record.add_birthday(date_string)
        message =  "Birthday added "
        print(record.birthday)
    else: 
        message =  "Contact is not found"
    return message

@input_error
def show_birthday(args, book: AddressBook):
    name,*_ = args
    record = book.find(name)
    
    if record:
        return record.birthday.value
    else :
        return "Contact is not found"
   
    # else: "Contact is not found"
@input_error
def change_phone (args, book: AddressBook):
    name, phone_1, phone_2 = args
    record = book.find(name)
    record.edit_phone(phone_1,phone_2)
    return "Phone is changed"
 


@input_error
def main():
    book = AddressBook()
    print("Welcome to the assistant bot!")
    # contacts = {}
    
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break

        elif command == "hello":
            print("How can I help you?")
      
        elif command == "add":
            print(add_contact(args, book))

        elif command == "phone":
            print(book.get(args[0]))
        elif command == "all":
            for key, value in book.items():
                print(f"{key} {value}")
        elif command == "change":
            print(change_phone(args, book))
        
        elif command == "add-birthday":
            print(add_birthday2(args, book))

        elif command == "show-birthday":
            print(show_birthday(args, book))

        elif command == "birthdays":
            b_list = book.get_upcoming_birthdays()
            output_string = ""
            for person in b_list:
                output_string += f"Name: {person['name']}, Congratulation date: {person['congratulation_date']}\n"
            print(output_string)
                

        else:
           print("Invalid command.")

if __name__ == "__main__":
    main()
