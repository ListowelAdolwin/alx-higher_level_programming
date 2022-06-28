#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
num = number % 10
print("The last digit of {} is {} ".format(number, num), end="")
if (num > 5):
    print("and is greater than 5")
elif (num == 0):
    print("and is 0")
elif (num < 6) and (num != 0):
    print("and is less than 6 and not 0")
