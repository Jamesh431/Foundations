# month = 'September 2021'
# days = ' S  M  T  W  T  F  S \n'
# week_1 = ' 1   2   3   4 \n'
# week_2 = ' 5   6   7   8   9  10  11 \n'
# week_3 = '12  13  14  15  16  17  18 \n'
# week_4 = '19  20  21  23  24  25 \n'
# week_5 = '26  27  28  29  30 \n'

# print(f'{month:>25}')
# print(f'{days:>30}')
# print(f'{week_1:>30}')
# print(f'{week_2:30}')
# print(f'{week_3:15}')
# print(f'{week_4:15}')
# print(f'{week_5:20}')

month = 'September 2021\n'
days = ' S    M    T    W    T    F    S\n'
week_1 = ' 1    2    3    4\n'
week_2 = ' 5    6    7    8    9   10   11\n'
week_3 = '12   13   14   15   16   17   18\n'
week_4 = '19   20   21   22   23   24   25\n'
week_5 = '26   27   28   29   30\n'

print(f'{month:>25}')
print(f'{days:>30}')
print(f'{week_1:>33}')
print(f'{week_2:20}')
print(f'{week_3:15}')
print(f'{week_4:15}')
print(f'{week_5:20}')


# how john did it below
# COMPLEX CALANDER
month = "September"
year = 2022
days_in_month = 30
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
