#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    args = len(sys.argv) - 1

    total_result = 0
    for i in range(args):
        result = int(sys.argv[i + 1])
        total_result += result
    print("{}".format(total_result))
