import collections
import itertools
import re

class Board(object):
    def __init__(self, e, chips, gens, steps):
        self.e = e
        self.chips = chips
        self.gens = gens
        self.steps = steps

    elements = ['polonium', 'thulium', 'promethium', 'ruthenium', 'cobalt']
    nelements = 5

    @classmethod
    def initial(cls, inp):
        gens = 0
        chips = 0
        floor = 0
        for line in inp:
            gen = 0
            for s in re.findall('(\S+) generator', line):
                gen = gen | (1 << cls.elements.index(s))

            gens += gen << (floor * 8)

            chip = 0
            for s in re.findall('(\S+)-compatible', line):
                chip = chip | (1 << cls.elements.index(s))
            chips += chip << (floor * 8)
            floor += 1

        return cls(0, chips, gens, 0)

    def __str__(self):
        fs = []
        for i in range(3, -1, -1):
            f = 'F%s %s   ' % (i+1, 'E' if self.e == i else '.')
            for e in range(self.nelements):
                f += 'G ' if self.gens & (1 << (e + i * 8)) else '. '
                f += 'C ' if self.chips & (1 << (e + i * 8)) else '. '
            fs.append(f)

        return '\n'.join(fs) + '\n%d steps' % self.steps

    def move(self, n, c, g):
        chips = self.chips & ~(c << (self.e*8)) | (c << n*8)
        gens = self.gens & ~(g << (self.e*8)) | (g << n*8)
        if valid(chips, gens):
            return type(self)(n, chips, gens, self.steps+1)
        return None

    def moves(self):
        f = self.e*8
        transitions = [(1,), (0, 2), (1, 3), (2,)][self.e]
        sa = self.state(self.e)

        c = (self.chips >> f) & 0xff
        g = (self.gens >> f) & 0xff
        cgtocg = [i for i in range(self.nelements) if c & g & 1<<i]

        for en in transitions:
            fn = en*8
            sb = self.state(en)

            cn = (self.chips >> fn) & 0xff
            gn = (self.gens >> fn) & 0xff
            xgtocg = [i for i in range(self.nelements) if ~c & g & cn & 1<<i]
            cxtocg = [i for i in range(self.nelements) if c & ~g & gn & 1<<i]

            if cgtocg:
                i = cgtocg[0]
                if en > self.e:
                    # only move a pair upwards, downwards never makes sense
                    yield self.move(en, 1 << i, 1 << i)

                if g & ~c == 0 and cn & ~gn == 0:
                    # if no unpaired gs on this level and no unpaired cs in next level
                    # break 1 pair, moving g up
                    yield self.move(en, 0, 1 << i)

            elif cxtocg:
                # move 1c to make a pair
                i = cxtocg[0]
                yield self.move(en, 1 << i, 0)

                # move 2cs to make 2 pairs
                if len(cxtocg) > 1:
                    i, j = cxtocg[0:2]
                    yield self.move(en, 1 << i | 1 << j, 0)

            elif xgtocg:
                # move 1g to make a pair
                i = xgtocg[0]
                yield self.move(en, 0, 1 << i)

                if len(xgtocg) > 1:
                    # move 2gs to make 2 pairs
                    i, j = xgtocg[0:2]
                    yield self.move(en, 0, 1 << i | 1 << j)

    def complete(self):
        return (self.chips & 0xffffff == 0) and  (self.gens & 0xffffff == 0)

    def __hash__(self):
        return hash(self.e) ^ hash(self.chips) ^ hash(self.gens)

    def __eq__(self, that):
        return self.e == that.e and self.gens == that.gens and self.chips == that.chips

    def state(self, level):
        m = 0xff << (level*8)
        if ((self.chips & ~self.gens) & m):
            return 'uc'
        if ((self.gens & ~self.chips) & m):
            return 'ug'
        return 'p'

def valid(chips, gens):
    return (
        ((chips & ~gens & 0xff) == 0 or (gens & ~chips & 0xff) == 0) and
        ((chips & ~gens & 0xff00) == 0 or (gens & ~chips & 0xff00) == 0) and
        ((chips & ~gens & 0xff0000) == 0 or (gens & ~chips & 0xff0000) == 0) and
        ((chips & ~gens & 0xff000000) == 0 or (gens & ~chips & 0xff000000) == 0)
    )

def run(board):
    queue = collections.deque([board])
    seen = set([board])

    i = 0
    while queue:
        board = queue.popleft()
        i += 1
        if i % 10000 == 0:
            print(board, len(queue), len(seen))
        for m in board.moves():
            if m not in seen:
                # check completion
                if m.complete():
                    return m.steps

                queue.append(m)
                seen.add(m)


board1 = Board.initial(open('input.txt'))
print('Answer #1:', run(board1))

# elerium, dilithium
class LargerBoard(Board):
    nelements = 7
board2 = LargerBoard.initial(open('input.txt'))
board2.chips |= 0b1100000
board2.gens |= 0b1100000
print('Answer #2:', run(board2))
