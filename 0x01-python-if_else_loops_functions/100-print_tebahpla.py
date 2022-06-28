for letter in reversed(range(97, 123)):
    print("{:c}".format(letter if (letter % 2 == 0) else (letter - 32)), end='')
