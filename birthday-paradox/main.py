import datetime, random
from typing import List

def get_birthdays(number_of_birthdays) -> List[str]:
    birthdays = []
    for i in range(number_of_birthdays):
        start_of_year = datetime.date(2001,1,1)
        random_number_of_days = datetime.timedelta(random.randint(1,366)) 
        birthday = start_of_year + random_number_of_days
        birthdays.append(birthday)
        # print(birthdays)
        return birthdays


def find_match_birtdays(birthdays):
    if len(birthdays) == len(set(birthdays)):
        return None
    for i, birthday_i in enumerate(birthdays):
        for j, birthday_j in enumerate(birthdays[i + 1: ]):
            if birthday_i == birthday_j:
                return birthday_i


MONTHS = ('Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec')

while True:
    print('How many birthdays shall i generate')
    response = input('>: ')
    if response.isdecimal() and (0 < int(response) <= 100):
        number_of_birthdays = int(response)
        break

print()
birthdays = get_birthdays(number_of_birthdays)
# for i , birthday in enumerate(birthdays):
#     if i != 0:
#         print(',',end='')
#     month_name = MONTHS[birthday.month - 1]
#     print(f'{month_name}, {birthday.day}', end='')
# print()
    
match = find_match_birtdays(birthdays)
if match != None:
    month_name = MONTHS[match.month - 1]
    print(f'multiple people have a birthday  on{month_name}{match.day}')
else:
    print('there are no matching birthdays')