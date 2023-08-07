for x in range(1, 5):
    print(f'Loop #{x} starts here')
    for y in range(10, 20):
        if y == 15:
            continue
          # when this is set as continue it will reach 14, then move to the next interation and then count from 16 and on. If its set as break then it will end up just stopping all together for that one loop and not continue on with said loop
        print(y)
    print(f'Loop #{x} ends here')


for x in range(1, 5):
    print(f'Loop #{x} starts here')
    for y in range(10, 20):
        if y == 15:
            break
          # this will only break the loop its in, not the parent loop(s)
        print(y)
    print(f'Loop #{x} ends here')


# for x in [1, 2, 3,]:
#     for y in ["a", "b", "c"]:
#       for z in ["x","y","z"]:
#         print(z)
#       print(y)
#     print(x)
