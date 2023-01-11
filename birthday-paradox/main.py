import datetime, random
from typing import List

def get_birthdays(number_of_birthdays) -> List[str]:
    birthdays = []
    for i in range(number_of_birthdays):
        start_of_year = datetime.date(2001,1,1)
        random_number = datetime.timedelta(random.randint(1,366)) 
        birthday = start_of_year + random_number
        birthdays.append(birthday)
    return birthdays

print(get_birthdays(5))
