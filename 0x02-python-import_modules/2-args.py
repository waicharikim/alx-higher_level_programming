#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    args = len(sys.argv) - 1

    if args == 0:
        print("{} arguments.".format(args))
    elif args == 1:
        print("{} argument:".format(args))
        print("1: {}".format(sys.argv[1]))
    else:
        print("{} arguments:".format(args))
        i = 0
        for i in range(args):
            print("{}: {}".format(i + 1, sys.argv[i + 1]))
