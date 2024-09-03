#!/usr/bin/python3
for num in range(0, 8):
    for num2 in range(1, 10):
        if num < num2:
            print("{}{}, ".format(num, num2), end="")
print("{}".format(89))
