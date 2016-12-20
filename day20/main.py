import itertools
import re
import sys

def parse(line):
    return tuple(map(int, line.split('-')))

def simplify(rules):
    for i in range(len(rules)):
        a, b = rules[i]
        for j in range(i+1, len(rules)):
            c, d = rules[j]
            if a <= d+1 and b+1 >= c:
                rules[i] = (min(a, c), max(b, d))
                rules[j:j+1] = []
                return True

def answer1():
    rules = [parse(line) for line in open('input.txt')]
    rules.sort()
    while simplify(rules):
        pass
    return rules[0][1]+1

def answer2():
    rules = [parse(line) for line in open('input.txt')]
    rules.sort()
    while simplify(rules):
        pass

    disallowed = sum(b + 1 - a for a, b in rules)
    return 4294967296 - disallowed

print('Answer #1:', answer1())
print('Answer #2:', answer2())
