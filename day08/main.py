import re
import numpy as np

def display(s):
    print('\n'.join(''.join('X' if p else ' '  for p in row) for row in s))

def run(width, height, lines):
    s = np.zeros((height, width), dtype=bool)
    answer = 0
    for line in lines:
        m1 = re.match(r'rect (\d+)x(\d+)', line)
        m2 = re.match(r'rotate row y=(\d+) by (\d+)', line)
        m3 = re.match(r'rotate column x=(\d+) by (\d+)', line)
        if m1:
            w, h = map(int, m1.groups())
            s[:h, :w] = True
        elif m2:
            cy, n = map(int, m2.groups())
            s[cy] = np.roll(s[cy], n)
        elif m3:
            cx, n = map(int, m3.groups())
            s[:,cx] = np.roll(s[:,cx], n)
        else:
            print("XXX ", line)
    return s

# test = run(7, 3, ['rect 3x2', 'rotate column x=1 by 1', 'rotate row y=0 by 4', 'rotate column x=1 by 1'])
# display(test)

answer = run(50, 6, open('input.txt'))
print('Answer #1:', np.sum(answer))
print('Answer #2:')
display(answer)