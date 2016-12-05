import hashlib
import sys

def solution1(key):
    answer = ''
    for i in range(0, sys.maxsize):
        x = (key + str(i)).encode('utf8')
        h = hashlib.md5(x).hexdigest()
        if h.startswith('00000'):
            answer += h[5]
            if len(answer) == 8:
                break
    return answer

def solution2(key):
    answer = [None] * 8
    needed = set('01234567')
    for i in range(0, sys.maxsize):
        x = (key + str(i)).encode('utf8')
        h = hashlib.md5(x).hexdigest()
        if h.startswith('00000'):
            pos = h[5]
            if pos in needed:
                answer[int(pos)] = h[6]
                needed.remove(pos)
                if not needed:
                    break
    return ''.join(answer)

print('Answer #1:', solution1('wtnhxymk'))
print('Answer #2:', solution2('wtnhxymk'))
