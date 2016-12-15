import collections
import hashlib
import itertools
import re
import sys

def answer1():
    # Disc #1 has 5 positions; at time=0, it is at position 2.
    # Disc #2 has 13 positions; at time=0, it is at position 7.
    # Disc #3 has 17 positions; at time=0, it is at position 10.
    # Disc #4 has 3 positions; at time=0, it is at position 2.
    # Disc #5 has 19 positions; at time=0, it is at position 9.
    # Disc #6 has 7 positions; at time=0, it is at position 0.
    return next(
        i
        for i in range(sys.maxsize)
        if ((i+2+1) % 5 == 0
        and ((i+7+2) % 13) == 0
        and ((i+10+3) % 17) == 0
        and ((i+2+4) % 3) == 0
        and ((i+9+5) % 19) == 0
        and ((i+0+6) % 7) == 0)
    )

def answer2():
    # Extra disk with 11 position, at time=0 pos 0.
    return next(
        i
        for i in range(sys.maxsize)
        if ((i+2+1) % 5 == 0
        and ((i+7+2) % 13) == 0
        and ((i+10+3) % 17) == 0
        and ((i+2+4) % 3) == 0
        and ((i+9+5) % 19) == 0
        and ((i+0+6) % 7) == 0
        and ((i+0+7) % 11) == 0)
    )

print('Answer #1:', answer1())
print('Answer #2:', answer2())
