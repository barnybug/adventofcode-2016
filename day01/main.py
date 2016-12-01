import re

def walk(input):
    x, y = 0, 0
    dx, dy = 0, -1
    for m in re.finditer(r'([LR])(\d+)', input):
        if m.group(1) == 'L':
            dx, dy = dy, -dx
        else:
            dx, dy = -dy, dx
        for i in range(0, int(m.group(2))):
            x += dx
            y += dy
            yield (x, y)

for x, y in walk(open('input.txt').read()):
    pass
print("Answer #1:", abs(x) + abs(y))

seen = set()
for x, y in walk(open('input.txt').read()):
    if (x, y) in seen:
        break
    seen.add((x, y))
print("Answer #2:", abs(x) + abs(y))
