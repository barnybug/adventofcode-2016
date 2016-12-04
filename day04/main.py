import collections
import re
import string

def answer1():
    total = 0
    for line in open('input.txt'):
        m = re.match('^(.+)-(\d+)\[(.{5})\]', line)
        name, sector, checksum = m.groups()
        name = name.replace('-', '')
        counts = collections.Counter(name).most_common()
        counts.sort(key=lambda k: (-k[1], k[0]))
        c = ''.join(ch for ch, _ in counts[:5])
        if c == checksum:
            total += int(sector)
    return total

def answer2():
    for line in open('input.txt'):
        m = re.match('^(.+)-(\d+)\[(.{5})\]', line)
        name, sector, checksum = m.groups()
        sector = int(sector)
        s = string.ascii_lowercase
        table = str.maketrans(s, s[sector % 26:] + s[0: sector%26])
        if name.translate(table) == 'northpole-object-storage':
            return sector

print("Answer #1:", answer1())
print("Answer #2:", answer2())