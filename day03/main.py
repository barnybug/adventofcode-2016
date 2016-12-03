def valid(a, b, c):
    return a + b > c and a + c > b and b + c > a

def parse(line):
    return map(int, line.strip().split())

def answer1():
    return sum(valid(*parse(line)) for line in open('input.txt'))

def answer2():
    lines = iter(parse(line) for line in open('input.txt'))
    return sum(
        valid(*t)
        for l in zip(lines, lines, lines)
        for t in zip(*l)
    )

print('Answer #1:', answer1())
print('Answer #2:', answer2())