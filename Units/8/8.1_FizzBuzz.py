for i in range(1, 101):
    if i % 15 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)

# with line 1 I declared a loop that ranges from 1 to 100. As the range() will always end at 1 number before the last number listed I listed it to 101
# I used the if statements to check the multiiplicity of every number. If its divisible (modulo) by 15, print "FizzBuzz" if its divisible (modulo) by 3, print "Fizz" if it's divisible (modulo) by 5, print "Buzz.". Every other number is then listed and not replaced.

# with if statements, use the least common case senerio first
