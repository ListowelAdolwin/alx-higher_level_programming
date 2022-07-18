#!/usr/bin/python3


def safe_print_integer(value):
    state = True
    try:
        print("{:d}".format(value))

    except TypeError:
        state = False
        print("Opps! Wrong data type")

    return (state)
