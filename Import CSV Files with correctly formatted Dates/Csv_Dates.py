import csv
from datetime import datetime


def date_check(date):
    if date == -1:
        return False
    elif date.count(' ') == 2 and date.count(',') == 1:
        return True
    else:
        return False


def in_months(m):
    if m in month_dict:
        return True
    else:
        return False


def in_day(d):
    if 0 < d < 32:
        if (d == 28) and (month == 'February') and (year % 4 != 0):
            return False
        else:
            return True

    else:
        return False


def in_year(y):
    if y in range(1, 10000):
        return True
    else:
        return False


month_dict = {'January': '1',
              'February': '2',
              'March': '3',
              'April': '4',
              'May': '5',
              'June': '6',
              'July': '7',
              'August': '8',
              'September': '9',
              'October': '10',
              'November': '11',
              'December': '12'
              }
date_inp = input()

with open(date_inp, 'r') as csvfile:
    with open('parsedDates.txt', 'w') as csv_file:
        csv_read = list(csv.reader(csvfile))
        for row in csv_read:

            date_conc = ','.join(row)
            month = 0
            day = 0
            year = 0
            check_date = date_check(date_conc)
            if check_date is False:
                continue
            elif check_date is True:
                month = date_conc[:date_conc.find(' ')].strip()
                day = int(date_conc[date_conc.find(' '):date_conc.find(',')].strip())
                year = int(date_conc[date_conc.rfind(' '):].strip())
                check_month = in_months(month)
                while check_date is True:
                    if check_month is False:
                        break
                    elif check_month is True:
                        check_day = in_day(day)
                        if check_day is False:
                            break
                        elif check_day is True:
                            year_check = in_year(year)
                            if year_check is False:
                                break
                            elif year_check is True:
                                tday = datetime.now()
                                compare_date = datetime.strptime(date_conc, '%B %d, %Y')
                                if tday >= compare_date:
                                    csv_file.write(f'{month_dict[month]}/{day}/{year}\n')
                                    print(f'{month_dict[month]}/{day}/{year}')
                                    break
                                else:
                                    break
