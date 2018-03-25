import datetime

print('-----------------------------------------')
print('           BIRTHDAY COUNTDOWN')
print('-----------------------------------------')
print()

y = int(input('What year were you born? '))
m = int(input('What month were you born? '))
d = int(input('What day were you born? '))
birthday = datetime.date(y, m, d)
today = datetime.date.today()

if today.month > birthday.month:
    bd_passed = True
    bd_today = False
elif today.month < birthday.month:
    bd_passed = False
    bd_today = False
elif today.day > birthday.day:
    bd_passed = True
    bd_today = False
elif today.day < birthday.day:
    bd_passed = False
    bd_today = False
else:
    bd_passed = True
    bd_today = True

if not bd_passed:
    bd_year = today.year
else:
    bd_year = today.year + 1

n_birthday = datetime.date(bd_year, birthday.month, birthday.day)
countdown = (n_birthday - today).days

print(f'\nIt looks like you were born on {birthday}.')

if bd_today:
    print('Today is your birthday. You should celebrate!!!')
else:
    print(f'Your birthday is in {countdown} days!')
    print('Aren\'t you excited?!')
