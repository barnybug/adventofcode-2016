import itertools
from functools import partial
import re

class Forward(object):
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
        l = s[a]
        s = s[:a] + s[a+1:]
        return s[:b] + l + s[b:]

    def rotate_based(a, s):
        n = s.index(a)
        n += 2 if n >= 4 else 1
        n = n % len(s)
        return Forward.rotate_right(n, s)

class Backward(Forward):
    def rotate_left(a, s):
        return Forward.rotate_right(a, s)

    def rotate_right(a, s):
        return Forward.rotate_left(a, s)

    def move_position(a, b, s):
        l = s[b]
        s = s[:b] + s[b+1:]
        return s[:a] + l + s[a:]

    def rotate_based(a, s):
        n = s.index(a)
        # before shift after
        # 0      1     1
        # 1      2     3
        # 2      3     5
        # 3      4     7
        # 4      6     2
        # 5      7     4
        # 6      8     6
        # 7      9     0
        m = {1: 1, 3: 2, 5: 3, 7: 4, 2: 6, 4: 7, 6: 8, 0: 1}[n]
        return Forward.rotate_left(m, s)

def compile(ops):
    ret = []
    for line in open('input.txt'):
        line = line.strip()
        if line.startswith('swap position'):
            a, b = map(int, re.findall('\d+', line))
            ret.append(partial(ops.swap_position, a, b))
        elif line.startswith('swap letter'):
            a, b = re.findall('letter ([a-z])', line)
            ret.append(partial(ops.swap_letter, a, b))
        elif line.startswith('reverse positions'):
            a, b = map(int, re.findall('\d+', line))
            ret.append(partial(ops.reverse_positions, a, b))
        elif line.startswith('rotate left'):
            a, = map(int, re.findall('\d+', line))
            ret.append(partial(ops.rotate_left, a))
        elif line.startswith('rotate right'):
            a, = map(int, re.findall('\d+', line))
            ret.append(partial(ops.rotate_right, a))
        elif line.startswith('move position'):
            a, b = map(int, re.findall('\d+', line))
            ret.append(partial(ops.move_position, a, b))
        elif line.startswith('rotate based'):
            a, = re.findall('letter ([a-z])', line)
            ret.append(partial(ops.rotate_based, a))
        else:
            raise ValueError

    return ret

def transform(code, fns):
    for fn in fns:
        code = fn(code)
    return code

def answer1():
    fns = compile(Forward)
    return transform('abcdefgh', fns)

def answer2():
    fns = compile(Backward)
    fns = list(reversed(fns))
    return transform('fbgdceah', fns)

print('Answer #1:', answer1())
print('Answer #2:', answer2())
