from datetime import datetime, date, timedelta


def string_to_date(date_string):
    return datetime.strptime(date_string, "%Y.%m.%d").date()


def date_to_string(date):
    return date.strftime("%Y.%m.%d")


def prepare_user_list(user_data):
    prepared_list = []
    for user in user_data:
        prepared_list.append({"name": user["name"], "birthday": string_to_date(user["birthday"])})
    return prepared_list


def find_next_weekday(start_date, weekday):
    days_ahead = weekday - start_date.weekday()
    if days_ahead <= 0:
        days_ahead += 7
    return start_date + timedelta(days=days_ahead)


def adjust_for_weekend(birthday):
    if birthday.weekday() >= 5:
        return find_next_weekday(birthday, 0)
    return birthday


def get_upcoming_birthdays(users, days=7):
    upcoming_birthdays = []
    today = date.today()

    for user in users:
        birthday_this_year = user["birthday"].replace(year=today.year)
    
        """
        Додайте на цьому місці перевірку, чи не буде 
        припадати день народження вже наступного року.
        """
        if birthday_this_year < today:
            birthday_this_year = user["birthday"].replace(year=today.year+1)
            

        if 0 <= (birthday_this_year - today).days <= days:
            """ 
            Додайте перенесення дати привітання на наступний робочий день,
            якщо день народження припадає на вихідний. 
            """
            birthday_this_year =  adjust_for_weekend(birthday_this_year)
            congratulation_date_str = date_to_string(birthday_this_year)
            upcoming_birthdays.append({"name": user["name"], "congratulation_date":congratulation_date_str})
    return upcoming_birthdays

users = [
    {"name": "Bill Gates", "birthday": "1955.6.25"},
    {"name": "Steve Jobs", "birthday": "1955.6.21"},
    {"name": "Jinny Lee", "birthday": "1956.6.22"},
    {"name": "Sarah Lee", "birthday": "1957.7.3"},
    {"name": "Jonny Lee", "birthday": "1958.7.2"},
    {"name": "John Doe", "birthday": "1985.6.23"},
    {"name": "Jane Smith", "birthday": "1990.6.30"}
]

print(get_upcoming_birthdays(prepare_user_list(users),7))