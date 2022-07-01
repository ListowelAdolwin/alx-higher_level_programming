#!/usr/bin/python3


def no_c(my_string):
    new_string = ""
    for i in range(len(my_string) - 1):
        if (my_string[i].upper()) != 'C':
            new_string = new_string + my_string[i]

    my_string = new_string
    return new_string
