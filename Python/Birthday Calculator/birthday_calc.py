
print('Birthday Calculator\nEnter the Current Day: \n')

current_month = (int(input('Month: ')))
current_day = (int(input('Day: ')))
current_year = (int(input('Year: ')))
print(f'The current day is {current_month}/{current_day}/{current_year}')

print('\nEnter your Birthday: ')

b_day_month = (int(input('Month: ')))
b_day_day = (int(input('Day: ')))
b_day_year = (int(input('Year: ')))
if (current_day == b_day_day) and (current_month == b_day_month):
    years_old = current_year - b_day_year
    print(f'Happy Birthday! You are {years_old} years old!')
elif current_month < b_day_month:
    years_old = (current_year - b_day_year) - 1
    print(f'You are {years_old} year\'s old.')
elif current_month > b_day_month:
    years_old = (current_year - b_day_year)
    print(f'You are {years_old} year\'s old.')
elif current_month == b_day_month and current_day < b_day_day:
    years_old = (current_year - b_day_year) - 1
    print(f'You are {years_old} year\'s old.')
else:
    years_old = (current_year - b_day_year)
    print(f'You are {years_old} year\'s old.')
