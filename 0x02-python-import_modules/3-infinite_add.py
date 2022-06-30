#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv

size_argv = len(argv)
sum_commands = 0
i = 1
while (i < size_argv):
    sum_commands = sum_commands + int(argv[i])
    i = i + 1

print(sum_commands)
