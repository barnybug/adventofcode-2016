def checksum(s):
    i = iter(s)
    ret = ''
    for a, b in zip(i, i):
        ret += '1' if a == b else '0'
    if len(ret) % 2 == 0:
        return checksum(ret)
    else:
        return ret

def answer(length):
    initial = '01111001100111011'
    invert_table = str.maketrans('01', '10')
    s = initial
    while len(s) < length:
        s += '0' + ''.join(reversed(s.translate(invert_table)))
    s = s[:length]
    return checksum(s)

print('Answer #1:', answer(272))
print('Answer #2:', answer(35651584))
