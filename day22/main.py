import re
from collections import deque

WIDTH = 36
HEIGHT = 25
pairs = list(range(WIDTH*HEIGHT))
neighbours = [None for _ in pairs]
for x in range(WIDTH):
    for y in range(HEIGHT):
        n = []
        if x > 0:
            n.append(x-1+y*WIDTH)
        if y > 0:
            n.append(x+(y-1)*WIDTH)
        if x < WIDTH-1:
            n.append(x+1+y*WIDTH)
        if y < HEIGHT-1:
            n.append(x+(y+1)*WIDTH)
        neighbours[x+y*WIDTH] = n

def parse():
    nodes = [0 for p in pairs]
    for line in open('input.txt'):
        m = re.match(r'/dev/grid/node-x(\d+)-y(\d+)\s+(\d+)T\s+(\d+)T\s+(\d+)T', line)
        if not m:
            continue
        x, y, size, used, avail = map(int, m.groups())
        if size > 200:
            t = -1
        elif used == 0:
            t = 0
        else:
            t = 2 if x == WIDTH-1 and y == 0 else 1
        nodes[x + y*WIDTH] = t
    return nodes

def answer1():
    answer = 0
    nodes = parse()
    return sum(
        nodes[p1] > 0 and nodes[p2] == 0
        for p1 in pairs
        for p2 in pairs
        if p1 != p2
    )

def answer2():
    answer = 0
    board = parse()
    space = board.index(0)
    goal = board.index(2)
    queue = deque([(space, goal, 0)])
    seen = set()
    while queue:
        space, goal, steps = queue.popleft()
        if goal == 0:
            break

        for neighbour in neighbours[space]:
            if board[neighbour] != -1:
                if neighbour == goal:
                    t = (neighbour, space)
                else:
                    t = (neighbour, goal)
                if t not in seen:
                    queue.append((t[0], t[1], steps+1))
                    seen.add(t)

    return steps

print('Answer #1:', answer1())
print('Answer #2:', answer2())
