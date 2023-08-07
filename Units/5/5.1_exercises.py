val = 3.14159265

print(f'{val:.3f}')
# output was rounded up

print(f'{val:.7f}')
# output was rounded up
##############################

title1 = 'Name'
title2 = 'City'
title3 = 'State'
title4 = 'Age'
border = '------ ---------- ------------- ----'
name1 = 'Jane'
name2 = 'Fred'
name3 = 'Betsy'
city1 = 'Boston'
city2 = 'Portland'
city3 = 'Orlando'
state1 = 'Massachusetts'
state2 = 'Oregon'
state3 = 'Florida'
age1 = 24
age2 = 31
age3 = 29

print(f'{title1:6} {title2:10} {title3:13} {title4}')
print(border)
print(f'{name1:6} {city1:10} {state1:13} {age1}')
print(f'{name2:6} {city2:10} {state2:13} {age2}')
print(f'{name3:6} {city3:10} {state3:13} {age3}')

# {asdf:>x} will justify to the right
# {asdf:^x} will justify to the center
# {asdf:x} will justify to the left
# x is a placeholder for any number chosen to justify how many characters are taken up before the next input starts (this includes the characters within the input, not just the spaces between)
