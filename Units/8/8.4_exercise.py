# for i in range(1,21):
#   if i == 15:
#     break
#   print(i)

# 1. Write a loop that iterates over a range of numbers from 1 to 20. After printing 15, use break to stop printing numbers.

# for i in "1111111devpipeline2222222":
#   if i == "1":
#       continue
#   if i == "2":
#       break
#   print(i)


# how brandon worked it


for i in "1111111devpipeline2222222":
    if i == "1":
        continue
    elif i == "2":
        break
    else:
        print(i, end="")

# doing print(i,end="") instead of print(i) will make it print horizontally instead of virtically. Why? I still don't understand tbh

# for i in [1, 1, 1, 1, 1, 1, 1, "devpipeline", 2, 2, 2, 2, 2, 2, 2]:
#   if i == 1:
#     continue
#   if i == 2:
#     break
#   print(i)

# 2. Write a loop that takes the input of "1111111devpipeline2222222" and uses continue and break to leave us with the output of "devpipeline".
