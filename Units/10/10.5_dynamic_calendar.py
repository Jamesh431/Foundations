month = input("Enter a month number (1-12) \n >")
for i in month:
    thirty_days = ['4', '6', '9', '11']
    thirty_one_days = ['1', '3', '5', '7', '8', '10', '12']
    twenty_eight_days = ['2']
    if month not in (thirty_days) and month not in (thirty_one_days) and month not in (twenty_eight_days):
        month = input("Month not recognized, please input month number 1-12\n > ")
    else:
        break
year = input("Enter a year \n >")

for i in month:
    if month == '1':
        month_name = 'January'
    elif month == '2':
        month_name = 'February'
    elif month == '3':
        month_name = 'March'
    elif month == '4':
        month_name = 'April'
    elif month == '5':
        month_name = 'May'
    elif month == '6':
        month_name = 'June'
    elif month == '7':
        month_name = 'July'
    elif month == '8':
        month_name = 'August'
    elif month == '9':
        month_name = 'September'
    elif month == '10':
        month_name = 'October'
    elif month == '11':
        month_name = 'November'
    elif month == '12':
        month_name = 'December'


def is_leap_year(input_year):

    if (input_year % 4 == 0 and input_year % 100 != 0) or (input_year % 400 == 0):
        return True

    else:
        return False


def get_days_in_month(month, year):
    month = int(month)
    year = int(year)
    thirty_days = [4, 6, 9, 11]
    thirty_one_days = [1, 3, 5, 7, 8, 10, 12]
    twenty_eight_days = [2]
    if month in (thirty_days):
        days_in_month = 30
        return days_in_month
    elif month in (thirty_one_days):
        days_in_month = 31
        return days_in_month
    elif month in (twenty_eight_days):
        if is_leap_year(year):
            days_in_month = 29
            return days_in_month
        else:
            days_in_month = 28
            return days_in_month
    elif month in (twenty_eight_days) and not is_leap_year(year):
        days_in_month = 28
        return days_in_month


def get_starting_day_of_week(year, month):
    month = int(month)
    year = int(year)
    t = [0, 3, 2, 5, 0, 3, 5, 1, 4, 6, 2, 4]

    if month < 3:
        year -= 1
    return ((year + int(year/4) - int(year/100) + int(year/400) + t[month-1] + 1) % 7)


def print_month_calendar(month, year):
    days_in_month = get_days_in_month(month, year)
    start_day = get_starting_day_of_week(year, month)
    day_one = "S"
    day_two = "M"
    day_three = "T"
    day_four = "W"
    day_five = "T"
    day_six = "F"
    day_seven = "S"
    month_year_str = f"{month_name} {year}"
    print(f'{month_year_str:^35}\n')
    print(f'{day_one:^5}{day_two:^5}{day_three:^5}{day_four:^5}{day_five:^5}{day_six:^5}{day_seven:^5}\n')
    current_day_of_week = 0
    blank_day = " "
    for day in range(1, days_in_month+1):
        if day == 1:
            for x in range(start_day):
                print(f'{blank_day:^5}', end="")
            current_day_of_week = start_day
        print(f'{day:^5}', end="")
        current_day_of_week += 1
        if current_day_of_week > 6:
            print('\n')
            current_day_of_week = 0
    print()


print_month_calendar(month, year)


# month=input("Enter a month number (1-12) \n >")
# year=input("Enter a year \n >")

# # jan=('jan','Jan','january','January')
# # feb=('feb','Feb','February','february','Febuary','febuary')
# # mar=('mar','Mar','March','march')
# # apr=('apr','Apr','April','april')
# # may=('may','May')
# # jun=('june','June')
# # jul=('july','July')
# # aug=('aug','Aug','August','august')
# # sep=('sep','Sep','September','september')
# # oct=('oct','Oct','October','october')
# # nov=('nov','Nov','november','November')
# # dec=('dec','Dec','December','december')


# 30_days = ('4','6','9','11')
# 31_days = ('1','3','5','7','8','10','12')
# 28_days = ('2')

# def is_leap_year(year):
#   if year.isnumeric():
#     year = int(year)
#     if year < 1752:
#       return None
#   else:
#     return None
#   leap_year = (year % 4 == 0 and year % 100 != 0) or (year % 4 ++ 0 and year % 100 == 0 and year % 400 == 0)
#   return leap_year

# while True
#   def get_days_in_month(month, year):
#     if month in (30_days):
#       days_in_month = 30
#       break
#     elif month in (31_days):
#       days_in_month = 31
#       break
#     elif month in (28_days):
#       if is_leap_year(year):
#         days_in_month = 29
#         break
#       else:
#         days_in_month = 28
#         break
#     elif month in (28_days) and not is_leap_year(year):
#       days_in_month = 28
#       break
#     else:
#       year = input("Month not recognized, please input month number 1-12\n > ")


# def get_starting_day_of_week(year, month, ):
# t = [0, 3, 2, 5, 0, 3, 5, 1, 4, 6, 2, 4]
# 	if month < 3:
#     year -= 1
# 	return (year + int(year/4) - int(year/100) + int(year/400) + t[month-1] + day) % 7

# def print_month_calendar():
#     day_one= "S"
#     day_two= "M"
#     day_three= "T"
#     day_four= "W"
#     day_five= "T"
#     day_six= "F"
#     day_seven= "S"
#     month_year_str = f"{month} {year}"
#     print(f'{month_year_str:^28}\n')
#     print(f'{day_one:>4}{day_two:>4}{day_three:>4}{day_four:>4}{day_five:>4}{day_six:>4}{day_seven:>4}')
#     current_day_of_week =1
#     blank_day = " "
#     for day in range(1, days_in_month +1):
#       if day == 1:
#         for __                  in range(start_day-1):
#           print(f'{blank_day:4}', end="")
#         current_day_of_week = start_day
#       print(f'{day:4}', end="")
#       current_day_of_week +=1
#       if current_day_of_week>7:
#         print('\n')
#         current_day_of_week=1
#     print()

# sun=('Su','Sun','Sunday')
# mon=('M','Mo','Mon','Monday')
# tue=('Tu', 'Tue', 'Tues', 'Tuesday')
# wed=('W','Wed','Wednesday')
# thu=('Th','Thu','Thur','Thursday')
# fri=('F','Fr','Fri','Friday')
# sat=('Sa','Sat','Saturday')

# month=input("Type the month\n > ")
# month=month.title()
# year=input("Type year\n > ")
# start_day=input("Type start day of the week (first day is sunday)\n > ")

# while True:
#   if start_day.isnumeric():
#       start_day = int(start_day)
#       break
#   elif start_day.isalpha():
#       start_day = start_day.title()
#       if start_day in sun:
#           start_day = 1
#           start_day = int(start_day)
#           break
#       elif start_day in mon:
#           start_day = 2
#           start_day = int(start_day)
#           break
#       elif start_day in tue:
#           start_day = 3
#           start_day = int(start_day)
#           break
#       elif start_day in wed:
#           start_day = 4
#           start_day = int(start_day)
#           break
#       elif start_day in thu:
#           start_day = 5
#           start_day = int(start_day)
#           break
#       elif start_day in fri:
#           start_day = 6
#           start_day = int(start_day)
#           break
#       elif start_day in sat:
#           start_day = 7
#           start_day = int(start_day)
#           break
#       elif start_day == "S":
#           sat_or_sun = input("Do you mean Sat or Sun?\n > ")
#           sat_or_sun = sat_or_sun.title()
#           if sat_or_sun in sun:
#               start_day = 1
#               start_day = int(start_day)
#               break
#           elif sat_or_sun in sat:
#               start_day = 7
#               start_day = int(start_day)
#               break
#       elif start_day == "T":
#           tue_or_thu = input("Do you mean Tue or Thu?\n > ")
#           tue_or_thu = tue_or_thu.title()
#           if tue_or_thu in tue:
#               start_day = 3
#               start_day = int(start_day)
#               break
#           elif tue_or_thu in thu:
#               start_day = 5
#               start_day = int(start_day)
#               break
#       else:
#           start_day = input('Day not recognized. Please enter a valid start day:\n>  ')

# # made some booleans that can tell if someone types sunday it will make start day 1. Maye even just type in w for wed. And if its just an s for sat or sun have an input ask if they mean sat or sun, same with a t for tue and thur
# # ajsn_days = 30
# # jmmjaod_days = 31
# # feb_days = 28
# if month in ("April June July September November"):
#   days_in_month = 30
# elif month in ("January March May June August October December"):
#   days_in_month = 31
# elif month in ("February"):
#   if is_leap_year(year) :
#     days_in_month = 29
#   else:
#     days_in_month = 28

# print_month_calendar()


# month=input("Enter a month number (1-12) \n >")
# year=input("Enter a year \n >")

# for i in month:
#   if month == '1':
#     month_name='January'
#   elif month == '2':
#     month_name='February'
#   elif month == '3':
#     month_name='March'
#   elif month == '4':
#     month_name='April'
#   elif month == '5':
#     month_name='May'
#   elif month == '6':
#     month_name='June'
#   elif month == '7':
#     month_name='July'
#   elif month == '8':
#     month_name='August'
#   elif month == '9':
#     month_name='September'
#   elif month == '10':
#     month_name='October'
#   elif month == '11':
#     month_name='November'
#   elif month == '12':
#     month_name='December'


# def is_leap_year(input_year):

#  if (input_year % 4 == 0 and input_year % 100 != 0) or (input_year % 400 ==0):
#   return True

#  else:
#   return False

# def get_days_in_month(month, year):
#   month = int(month)
#   year = int(year)
#   thirty_days = [4,6,9,11]
#   thirty_one_days = [1,3,5,7,8,10,12]
#   twenty_eight_days = [2]
#   if month in (thirty_days):
#     days_in_month = 30
#     return days_in_month
#   elif month in (thirty_one_days):
#     days_in_month = 31
#     return days_in_month
#   elif month in (twenty_eight_days):
#     if is_leap_year(year):
#       days_in_month = 29
#       return days_in_month
#     else:
#       days_in_month = 28
#       return days_in_month
#   elif month in (twenty_eight_days) and not is_leap_year(year):
#     days_in_month = 28
#     return days_in_month
#   else:
#     year = input("Month not recognized, please input month number 1-12\n > ")

# def get_starting_day_of_week(year, month):
#   month = int(month)
#   year = int(year)
#   t = [1, 4, 3, 6, 1, 4, 6, 2, 5, 7, 3, 5]
#   if month < 3:
#     year -= 1
#   return ((year + int(year/4) - int(year/100) + int(year/400) + t[month-1] + 1) % 7)


# def print_month_calendar(month, year):
#     days_in_month = get_days_in_month(month, year)
#     start_day = get_starting_day_of_week(year, month)
#     day_one= "S"
#     day_two= "M"
#     day_three= "T"
#     day_four= "W"
#     day_five= "T"
#     day_six= "F"
#     day_seven= "S"
#     month_year_str = f"{month_name} {year}"
#     print(f'{month_year_str:^35}\n')
#     print(f'{day_one:^5}{day_two:^5}{day_three:^5}{day_four:^5}{day_five:^5}{day_six:^5}{day_seven:^5}\n')
#     current_day_of_week =1
#     blank_day = " "
#     for day in range(1, days_in_month +1):
#       if day == 1:
#         for __                  in range(start_day-1):
#           print(f'{blank_day:^5}', end="")
#         current_day_of_week = start_day
#       print(f'{day:^5}', end="")
#       current_day_of_week +=1
#       if current_day_of_week>7:
#         print('\n')
#         current_day_of_week=1
#     print()


# print_month_calendar(month, year)


# month=input("Enter a month number (1-12) \n >")
# year=input("Enter a year \n >")

# # jan=('jan','Jan','january','January')
# # feb=('feb','Feb','February','february','Febuary','febuary')
# # mar=('mar','Mar','March','march')
# # apr=('apr','Apr','April','april')
# # may=('may','May')
# # jun=('june','June')
# # jul=('july','July')
# # aug=('aug','Aug','August','august')
# # sep=('sep','Sep','September','september')
# # oct=('oct','Oct','October','october')
# # nov=('nov','Nov','november','November')
# # dec=('dec','Dec','December','december')


# 30_days = ('4','6','9','11')
# 31_days = ('1','3','5','7','8','10','12')
# 28_days = ('2')

# def is_leap_year(year):
#   if year.isnumeric():
#     year = int(year)
#     if year < 1752:
#       return None
#   else:
#     return None
#   leap_year = (year % 4 == 0 and year % 100 != 0) or (year % 4 ++ 0 and year % 100 == 0 and year % 400 == 0)
#   return leap_year

# while True
#   def get_days_in_month(month, year):
#     if month in (30_days):
#       days_in_month = 30
#       break
#     elif month in (31_days):
#       days_in_month = 31
#       break
#     elif month in (28_days):
#       if is_leap_year(year):
#         days_in_month = 29
#         break
#       else:
#         days_in_month = 28
#         break
#     elif month in (28_days) and not is_leap_year(year):
#       days_in_month = 28
#       break
#     else:
#       year = input("Month not recognized, please input month number 1-12\n > ")


# def get_starting_day_of_week(year, month, ):
# t = [0, 3, 2, 5, 0, 3, 5, 1, 4, 6, 2, 4]
# 	if month < 3:
#     year -= 1
# 	return (year + int(year/4) - int(year/100) + int(year/400) + t[month-1] + day) % 7

# def print_month_calendar():
#     day_one= "S"
#     day_two= "M"
#     day_three= "T"
#     day_four= "W"
#     day_five= "T"
#     day_six= "F"
#     day_seven= "S"
#     month_year_str = f"{month} {year}"
#     print(f'{month_year_str:^28}\n')
#     print(f'{day_one:>4}{day_two:>4}{day_three:>4}{day_four:>4}{day_five:>4}{day_six:>4}{day_seven:>4}')
#     current_day_of_week =1
#     blank_day = " "
#     for day in range(1, days_in_month +1):
#       if day == 1:
#         for __                  in range(start_day-1):
#           print(f'{blank_day:4}', end="")
#         current_day_of_week = start_day
#       print(f'{day:4}', end="")
#       current_day_of_week +=1
#       if current_day_of_week>7:
#         print('\n')
#         current_day_of_week=1
#     print()

# sun=('Su','Sun','Sunday')
# mon=('M','Mo','Mon','Monday')
# tue=('Tu', 'Tue', 'Tues', 'Tuesday')
# wed=('W','Wed','Wednesday')
# thu=('Th','Thu','Thur','Thursday')
# fri=('F','Fr','Fri','Friday')
# sat=('Sa','Sat','Saturday')

# month=input("Type the month\n > ")
# month=month.title()
# year=input("Type year\n > ")
# start_day=input("Type start day of the week (first day is sunday)\n > ")

# while True:
#   if start_day.isnumeric():
#       start_day = int(start_day)
#       break
#   elif start_day.isalpha():
#       start_day = start_day.title()
#       if start_day in sun:
#           start_day = 1
#           start_day = int(start_day)
#           break
#       elif start_day in mon:
#           start_day = 2
#           start_day = int(start_day)
#           break
#       elif start_day in tue:
#           start_day = 3
#           start_day = int(start_day)
#           break
#       elif start_day in wed:
#           start_day = 4
#           start_day = int(start_day)
#           break
#       elif start_day in thu:
#           start_day = 5
#           start_day = int(start_day)
#           break
#       elif start_day in fri:
#           start_day = 6
#           start_day = int(start_day)
#           break
#       elif start_day in sat:
#           start_day = 7
#           start_day = int(start_day)
#           break
#       elif start_day == "S":
#           sat_or_sun = input("Do you mean Sat or Sun?\n > ")
#           sat_or_sun = sat_or_sun.title()
#           if sat_or_sun in sun:
#               start_day = 1
#               start_day = int(start_day)
#               break
#           elif sat_or_sun in sat:
#               start_day = 7
#               start_day = int(start_day)
#               break
#       elif start_day == "T":
#           tue_or_thu = input("Do you mean Tue or Thu?\n > ")
#           tue_or_thu = tue_or_thu.title()
#           if tue_or_thu in tue:
#               start_day = 3
#               start_day = int(start_day)
#               break
#           elif tue_or_thu in thu:
#               start_day = 5
#               start_day = int(start_day)
#               break
#       else:
#           start_day = input('Day not recognized. Please enter a valid start day:\n>  ')

# # made some booleans that can tell if someone types sunday it will make start day 1. Maye even just type in w for wed. And if its just an s for sat or sun have an input ask if they mean sat or sun, same with a t for tue and thur
# # ajsn_days = 30
# # jmmjaod_days = 31
# # feb_days = 28
# if month in ("April June July September November"):
#   days_in_month = 30
# elif month in ("January March May June August October December"):
#   days_in_month = 31
# elif month in ("February"):
#   if is_leap_year(year) :
#     days_in_month = 29
#   else:
#     days_in_month = 28

# print_month_calendar()
