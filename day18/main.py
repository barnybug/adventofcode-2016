import re

def answer(n):
    row = open('input.txt').read().replace('^', '1').replace('.', '0')
    w = len(row)
    row = int('0b'+row, 2)
    safe = 0
    for i in range(n):
        safe += w-bin(row).count('1')
        row = (row >> 1) ^ (row << 1) & ((2<<(w-1))-1)
    return safe

print('Answer #1:', answer(40))
print('Answer #2:', answer(400000))