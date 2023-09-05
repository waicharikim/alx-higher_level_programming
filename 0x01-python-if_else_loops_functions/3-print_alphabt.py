#!/usr/bin/python3
for alpha in range(97, 123):
    if alpha == ord('e') or alpha == ord('q'):
        continue
    print("{:c}".format(alpha), end='')
