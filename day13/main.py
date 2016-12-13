import collections
import re

def solve(magic, target, max_steps):
    board = {(1, 1): 'O'}
    queue = collections.deque([(1, 1, 0)])
    while queue:
        ox, oy, steps = queue.popleft()
        for x, y in ((ox-1, oy), (ox+1, oy), (ox, oy-1), (ox, oy+1)):
            if x >= 0 and y >= 0 and (x, y) not in board:
                b = x*x + 3*x + 2*x*y + y + y*y + magic
                if bin(b).count('1') % 2 == 1:
                    board[(x,y)] = '#'
                else:
                    if (x, y) == target:
                        return steps+1
                    if steps < max_steps:
                        board[(x,y)] = 'O'
                        queue.append((x, y, steps+1))
    return sum(row == 'O' for row in board.values())

print('Answer #1:', solve(1352, (31, 39), 100))
print('Answer #2:', solve(1352, (-1, -1), 50))
