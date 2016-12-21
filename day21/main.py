import itertools
from functools import partial
import re

def swap_position(a, b, s):
    s = list(s)
    s[a], s[b] = s[b], s[a]
    return ''.join(s)

def swap_letter(a, b, s):
    return s.replace(a, 'X').replace(b, a).replace('X', b)

def reverse_positions(a, b, s):
    return s[:a] + ''.join(reversed(s[a:b+1])) + s[b+1:]

def rotate_left(a, s):
    a = a % len(s)
    return s[a:] + s[:a]

def rotate_right(a, s):
    a = a % len(s)
    return s[-a:] + s[:-a]

def move_position(a, b, s):
    if b > a:
        l = s[a]
        s = s[:a] + s[a+1:]
        return s[:b] + l + s[b:]
    else:
        l = s[a]
        s = s[:a] + s[a+1:]
        return s[:b] + l + s[b:]

def rotate_based(a, s):
    n = s.index(a)
    n += 2 if n >= 4 else 1
    n = n % len(s)
    return s[-n:] + s[:-n]

def compile():
    ret = []
    for line in open('input.txt'):
        line = line.strip()
        if line.startswith('swap position'):
            a, b = map(int, re.findall('\d+', line))
            ret.append(partial(swap_position, a, b))
        elif line.startswith('swap letter'):
            a, b = re.findall('letter ([a-z])', line)
            ret.append(partial(swap_letter, a, b))
        elif line.startswith('reverse positions'):
            a, b = map(int, re.findall('\d+', line))
            ret.append(partial(reverse_positions, a, b))
        elif line.startswith('rotate left'):
            a, = map(int, re.findall('\d+', line))
            ret.append(partial(rotate_left, a))
        elif line.startswith('rotate right'):
            a, = map(int, re.findall('\d+', line))
            ret.append(partial(rotate_right, a))
        elif line.startswith('move position'):
            a, b = map(int, re.findall('\d+', line))
            ret.append(partial(move_position, a, b))
        elif line.startswith('rotate based'):
            a, = re.findall('letter ([a-z])', line)
            ret.append(partial(rotate_based, a))
        else:
            raise ValueError

    return ret

fns = compile()

def transform(code):
    for fn in fns:
        code = fn(code)
    return code

def answer1():
    code = 'abcdefgh'
    return transform(code)

def answer2():
    for p in itertools.permutations('abcdefgh'):
        p = ''.join(p)
        if transform(p) == 'fbgdceah':
            return p

print('Answer #1:', answer1())
print('Answer #2:', answer2())
