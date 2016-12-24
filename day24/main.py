from collections import deque
from itertools import permutations
import re

test = [
    '###########\n',
    '#0.1.....2#\n',
    '#.#######.#\n',
    '#4.......3#\n',
    '###########\n',
]

def distance_matrix(lines):
    lines = [line.strip() for line in lines]
    HEIGHT = len(lines)
    WIDTH = len(lines[0])
    numbers = {}
    neighbours = []
    for y in range(HEIGHT):
        for x in range(WIDTH):
            n = []
            ch = lines[y][x]
            if ch in '0123456789':
                numbers[int(ch)] = x+y*WIDTH
            if ch != '#':
                if x > 0 and lines[y][x-1] != '#':
                    n.append(x-1+y*WIDTH)
                if y > 0 and lines[y-1][x] != '#':
                    n.append(x+(y-1)*WIDTH)
                if x < WIDTH-1 and lines[y][x+1] != '#':
                    n.append(x+1+y*WIDTH)
                if y < HEIGHT-1 and lines[y+1][x] != '#':
                    n.append(x+(y+1)*WIDTH)
            neighbours.append(n)

    def shortest(a, b):
        # calculate shortest path from a -> b
        s = numbers[a]
        queue = deque([(s, 0)])
        seen = set()
        while queue:
            c, steps = queue.popleft()
            if numbers[b] == c:
                return steps

            for neighbour in neighbours[c]:
                if neighbour not in seen:
                    queue.append((neighbour, steps+1))
                    seen.add(neighbour)

    # compute matrix of shortest paths
    places = sorted(numbers.keys())
    matrix = [[None for a in places] for b in places]
    for a in places:
        for b in places:
            if a == b:
                continue
            matrix[a][b] = shortest(a, b)

    return places, matrix

places, matrix = distance_matrix(open('input.txt'))

def answer1():
    # brute force possible routes
    answer = min(
        sum(
            matrix[a][b]
            for a, b in zip((0,)+route, route)
        )
        for route in permutations(places[1:])
    )
    return answer

def answer2():
    # finishing up at start (ie 0 at end of route as well as start)
    answer = min(
        sum(
            matrix[a][b]
            for a, b in zip((0,)+route, route+(0,))
        )
        for route in permutations(places[1:])
    )
    return answer

print('Answer #1:', answer1())
print('Answer #2:', answer2())
