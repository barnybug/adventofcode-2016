from sortedcontainers import SortedList

def answer1():
    n = 3018458
    elfs = [1 for i in range(n)]
    i = 0
    for _ in range(n-1):
        try:
            j = elfs.index(1, i+1)
        except:
            j = elfs.index(1, 0, i)
        elfs[j] = 0
        # print(elfs, i)

        try:
            i = elfs.index(1, j+1)
        except:
            i = elfs.index(1, 0, j)
    return elfs.index(1)+1

def answer2():
    n = 3018458
    elfs = SortedList(range(1, n+1))
    i = 0
    for l in range(n, 1, -1):
        if l % 10000 == 0: print(l)
        h = l//2
        j = (i+h)%l
        # a = elfs[i]
        # b = elfs[j]
        elfs.pop(j)
        # print(elfs, a, 'from', b)
        if j > i:
            i = (i+1)%(l-1)
        else:
            i = i%(l-1)

    return elfs[0]

print('Answer #1:', answer1())
print('Answer #2:', answer2())
