from collections import deque

n = 3018458

def answer1():
    elfs = deque(range(n, 0, -1))
    while len(elfs) > 1:
        x = elfs.pop()
        elfs.pop()
        elfs.appendleft(x)
    return elfs[0]

def answer2():
    left = deque()
    right = deque()
    for i in range(1, n+1):
        if i < n//2 + 1:
            left.append(i)
        else:
            right.appendleft(i)

    while right:
        if len(left) > len(right):
            left.pop()
        else:
            right.pop()

        right.appendleft(left.popleft())
        left.append(right.pop())
    return left[0]

print('Answer #1:', answer1())
print('Answer #2:', answer2())
