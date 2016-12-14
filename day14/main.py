import collections
import hashlib
import itertools
import re
import sys

salt = 'cuanljph'

def hashes(stretch):
    for i in range(0, sys.maxsize):
        x = (salt + str(i)).encode('utf8')
        h = hashlib.md5(x).hexdigest()
        for j in range(0, stretch):
            h = hashlib.md5(h.encode('utf8')).hexdigest()
        yield h

def answers(hashiter):
    q = collections.deque()
    for h, _ in zip(hashiter, range(1001)):
        q.append(h)
    for i in range(sys.maxsize):
        h = q.popleft()
        m = re.search(r'000|111|222|333|444|555|666|777|888|999|aaa|bbb|ccc|ddd|eee|fff', h)
        # only consider the first
        if m:
            s = m.group(0)[0] * 5
            if any(h2 for h2 in q if s in h2):
                yield i
        q.append(next(hashiter))

number = 63 # 64th

def answer1():
    return(next(itertools.islice(answers(hashes(0)), number, None))+1)

def answer2():
    return(next(itertools.islice(answers(hashes(2016)), number, None))+1)

print('Answer #1:', answer1())
print('Answer #2:', answer2())