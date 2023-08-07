# ".1" in python is not equal to 1/10 as there are additional numbers like .010000087. The same is with .2 not being equal to 1/5.


# This is due to how floating point numbers are stored as binary and hardware restrictions. Basically a fraction will work if a prime denominator is 2, but it won't otherwise
