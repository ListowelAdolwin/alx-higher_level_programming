#!/usr/bin/python3
for number in range(0, 100):
    if number < 10:
        print("{:0>2d}, ".format(number), end="")
    elif number < 99:
        print("{}, ".format(number), end="")
    else:
        print(number)
