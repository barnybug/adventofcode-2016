import collections
import re

bots = collections.defaultdict(list)

def run():
    bots = collections.defaultdict(list)
    outputs = {}
    rules = [line.split() for line in open('input.txt')]
    while rules:
        for r in rules:
            if r[0] == 'value':
                bots[int(r[5])].append(int(r[1]))
                rules.remove(r)
            else:
                a = int(r[1])
                if len(bots[a]) == 2:
                    bots[a].sort()
                    low, high = bots[a]
                    if r[5] == 'bot':
                        bots[int(r[6])].append(low)
                    else:
                        outputs[int(r[6])] = low
                    if r[10] == 'bot':
                        bots[int(r[11])].append(high)
                    else:
                        outputs[int(r[11])] = high
                    rules.remove(r)

    for n, vs in bots.items():
        if vs == [17, 61]:
            print('Answer #1:', n)
            break

    print('Answer #2:', outputs[0] * outputs[1] * outputs[2])

run()
