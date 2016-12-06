from collections import Counter

def answer1():
    return ''.join(Counter(col).most_common()[0][0] for col in zip(*open('input.txt')))

def answer2():
    return ''.join(Counter(col).most_common()[-1][0] for col in zip(*open('input.txt')))

print('Answer #1:', answer1())
print('Answer #2:', answer2())