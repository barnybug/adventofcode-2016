import re

def answer(**regs):
    def read(reg):
        if reg in regs:
            return regs[reg]
        return int(reg)

    ins = [[line.split(), False] for line in open('input.txt') if not line.startswith('//')]
    pc = 0
    while pc < len(ins):
        i, toggled = ins[pc]
        ix = i[0]
        if toggled:
            if ix == 'inc':
                ix = 'dec'
            elif ix in ('dec', 'tgl'):
                ix = 'inc'
            elif ix == 'jnz':
                ix = 'cpy'
            else:
                ix = 'jnz'

        if ix == 'cpy':
            if i[2] in regs:
                regs[i[2]] = read(i[1])
        elif ix == 'inc':
            if i[1] in regs:
                regs[i[1]] = regs[i[1]] + 1
        elif ix == 'dec':
            if i[1] in regs:
                regs[i[1]] = regs[i[1]] - 1
        elif ix == 'jnz':
            if read(i[1]):
                pc += read(i[2])
                continue
        elif ix == 'tgl':
            x = pc + read(i[1])
            if x < len(ins):
                ins[x][1] = not ins[x][1]
        elif ix == 'mul':
            regs[i[3]] = read(i[1]) * read(i[2])

        pc += 1
            
    return regs['a']

print('Answer #1:', answer(a=7, b=0, c=0, d=0))
print('Answer #2:', answer(a=12, b=0, c=0, d=0))
