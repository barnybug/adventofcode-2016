import collections
import hashlib

seed = 'rrrbmfta'

def moves():
    queue = collections.deque()
    queue.append(('', 0, 0))
    while queue:
        state, x, y = queue.popleft()
        if x == 3 and y == 3:
            yield state
            continue
        h = hashlib.md5((seed+state).encode('utf8')).hexdigest()
        if h[0] in 'bcdef' and y > 0:
            queue.append((state+'U', x, y-1))
        if h[1] in 'bcdef' and y < 3:
            queue.append((state+'D', x, y+1))
        if h[2] in 'bcdef' and x > 0:
            queue.append((state+'L', x-1, y))
        if h[3] in 'bcdef' and x < 3:
            queue.append((state+'R', x+1, y))

def answer1():
    return next(moves())

def answer2():
    for l in moves():
        pass
    return len(l)

print('Answer #1:', answer1())
print('Answer #2:', answer2())