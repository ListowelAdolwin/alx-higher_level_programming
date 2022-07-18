#!/usr/bin/python3


def safe_print_list(my_list=[], x=0):
    i = 0
    count = 0
    try:
        for item in my_list:
            while(i <= x):
                print(my_list[i], end='')
                count += 1

    except Exception:
        pass
        print()
    return (count)
