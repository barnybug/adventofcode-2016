import hashlib
import sys

def solution1(key):
    answer = ''
    for i in range(0, sys.maxsize):
        x = (key + str(i)).encode('utf8')
        h = hashlib.md5(x).digest()
        if h[0] == 0 and h[1] == 0 and (h[2] & 0xf0) == 0:
            answer += '%x' % h[2]
            if len(answer) == 8:
                break
    return answer

def solution2(key):
    answer = ['_'] * 8
    count = 0
    for i in range(0, sys.maxsize):
        x = (key + str(i)).encode('utf8')
        h = hashlib.md5(x).digest()
        if h[0] == 0 and h[1] == 0 and (h[2] & 0xf0) == 0:
            if h[2] < 8 and answer[h[2]] == '_':
                answer[h[2]] = '%x' % (h[3] >> 4)
                print(''.join(answer))
                count += 1
                if count == 8:
                    break
    return ''.join(answer)

print('Answer #1:', solution1('wtnhxymk'))
print('Answer #2:', solution2('wtnhxymk'))
