from collections import deque

n = 3018458

def answer1(n):
    # From https://en.wikipedia.org/wiki/Josephus_problem:
    # "The most elegant form of the answer.. can be obtained by a one-bit left cyclic shift of n itself"
    x = bin(n)
    return int(x[3:] + x[2], 2)

def answer2(n):
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

print('Answer #1:', answer1(n))
print('Answer #2:', answer2(n))
