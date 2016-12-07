import re

def abba(x):
    return any(a == d and b == c and a != b for a, b, c, d in zip(x, x[1:], x[2:], x[3:]))

def answer1():
    answer = 0
    for line in open('input.txt'):
        parts = re.split(r'\[([^\]]+)\]', line)
        sn = ' '.join(parts[::2])
        hn = ' '.join(parts[1::2])
        answer += abba(sn) and not(abba(hn))
    return answer

def answer2():
    answer = 0
    for line in open('input.txt'):
        parts = re.split(r'\[([^\]]+)\]', line)
        sn = '  '.join(parts[::2])
        hn = '  '.join(parts[1::2])
        answer += any(a == c and a != b and b+a+b in hn for a, b, c in zip(sn, sn[1:], sn[2:]))

    return answer

print('Answer #1:', answer1())
print('Answer #2:', answer2())