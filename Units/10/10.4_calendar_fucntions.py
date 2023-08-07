def is_leap_year(year):
    if year.isnumeric():
        year = int(year)
        if year < 1752:
            return None
    else:
        return None
    leap_year = (year % 4 == 0 and year % 100 != 0) or (year % 4 == 0 and year % 100 == 0 and year % 400 == 0)
    return leap_year

# year = input("Input any year after 1752: ")
# print(is_leap_year(year))

# Using your code from the "Is Leap Year" Assignment, wrap your code into a function called is_leap_year that takes the year as a parameter and returns a boolean indicating whether the year passed in is a leap year or not.


def print_month_calendar():
    day_one = "S"
    day_two = "M"
    day_three = "T"
    day_four = "W"
    day_five = "T"
    day_six = "F"
    day_seven = "S"
    month_year_str = f"{month}{year}"
    print(f'{month_year_str:^28}\n')
    print(f'{day_one:>4}{day_two:>4}{day_three:>4}{day_four:>4}{day_five:>4}{day_six:>4}{day_seven:>4}')
    current_day_of_week = 0
    blank_day = " "
    for day in range(1, days_in_month + 1):
        if day == 1:
            for __ in range(start_day-1):
                print(f'{blank_day:4}', end="")
            current_day_of_week = start_day-1
        print(f'{day:4}', end="")
        current_day_of_week += 1
        if current_day_of_week > 6:
            print('\n')
            current_day_of_week = 0
    print()


sun = ('Su', 'Sun', 'Sunday')
mon = ('M', 'Mo', 'Mon', 'Monday')
tue = ('Tu', 'Tue', 'Tues', 'Tuesday')
wed = ('W', 'Wed', 'Wednesday')
thu = ('Th', 'Thu', 'Thur', 'Thursday')
fri = ('F', 'Fr', 'Fri', 'Friday')
sat = ('Sa', 'Sat', 'Saturday')

month = input("Type the month\n > ")
month = month.title()
year = input("Type year\n > ")
start_day = input("Type start day of the week (first day is sunday)\n > ")

while True:
    if start_day.isnumeric():
        start_day = int(start_day)
        break
    elif start_day.isalpha():
        start_day = start_day.title()
        if start_day in sun:
            start_day = 0
            start_day = int(start_day)
            break
        elif start_day in mon:
            start_day = 1
            start_day = int(start_day)
            break
        elif start_day in tue:
            start_day = 2
            start_day = int(start_day)
            break
        elif start_day in wed:
            start_day = 3
            start_day = int(start_day)
            break
        elif start_day in thu:
            start_day = 4
            start_day = int(start_day)
            break
        elif start_day in fri:
            start_day = 5
            start_day = int(start_day)
            break
        elif start_day in sat:
            start_day = 6
            start_day = int(start_day)
            break
        elif start_day == "S":
            sat_or_sun = input("Do you mean Sat or Sun?\n > ")
            sat_or_sun = sat_or_sun.title()
            if sat_or_sun in sun:
                start_day = 0
                start_day = int(start_day)
                break
            elif sat_or_sun in sat:
                start_day = 6
                start_day = int(start_day)
                break
        elif start_day == "T":
            tue_or_thu = input("Do you mean Tue or Thu?\n > ")
            tue_or_thu = tue_or_thu.title()
            if tue_or_thu in tue:
                start_day = 2
                start_day = int(start_day)
                break
            elif tue_or_thu in thu:
                start_day = 4
                start_day = int(start_day)
                break
        else:
            start_day = input('Day not recognized. Please enter a valid start day:\n>  ')

# made some booleans that can tell if someone types sunday it will make start day 1. Maye even just type in w for wed. And if its just an s for sat or sun have an input ask if they mean sat or sun, same with a t for tue and thur
# ajsn_days = 30
# jmmjaod_days = 31
# feb_days = 28
if month in ("April June July September November"):
    days_in_month = 30
elif month in ("January March May June August October December"):
    days_in_month = 31
elif month in ("February"):
    if is_leap_year(year):
        days_in_month = 29
    else:
        days_in_month = 28

print_month_calendar()

start_day = 5
day_one = "S"
day_two = "M"
day_three = "T"
day_four = "W"
day_five = "T"
day_six = "F"
day_seven = "S"
month_year_str = f"{month}{year}"
print(f'{month_year_str:^28}\n')
print(f'{day_one:>4}{day_two:>4}{day_three:>4}{day_four:>4}{day_five:>4}{day_six:>4}{day_seven:>4}')
current_day_of_week = 1
blank_day = " "
for day in range(1, days_in_month + 1):
    if day == 1:
        for __ in range(start_day-1):
            print(f'{blank_day:4}', end="")
        current_day_of_week = start_day
    print(f'{day:4}', end="")
    current_day_of_week += 1
    if current_day_of_week > 7:
        print('\n')
        current_day_of_week = 1
print()


# Using your code from the "Print Month Calendar" assignment, wrap your print calendar code into a function call print_month_calendar that prints a month calendar from the following parameters:
# month - The name of the month to print at the top of the calendar
# year - The year to print at the top of the calendar
# start_day_of_week - A number between 0-6 that indicates the starting day of the week for the calendar. 0 = Sunday, 6 = Saturday
# days_in_month - The number of days in the month
