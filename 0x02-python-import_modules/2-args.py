#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv


i = 1
size_argv = len(argv)
if (size_argv == 1):
    print("0 arguments.")
elif (size_argv == 2):
    print("1 argument:")
    print(f"1: {argv[i]}")
else:
    print(f"{size_argv - 1} arguments.")
    while(i < size_argv):
        print(f"{i}: {argv[i]}")
        i = i + 1
