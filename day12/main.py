import re

def answer(**regs):
    def read(reg):
        if reg in regs:
            return regs[reg]
        return int(reg)

    ins = [line.split() for line in open('input.txt')]
    pc = 0
    while pc < len(ins):
        i = ins[pc]
        if i[0] == 'cpy':
            regs[i[2]] = read(i[1])
        elif i[0] == 'inc':
            regs[i[1]] = regs[i[1]] + 1
        elif i[0] == 'dec':
            regs[i[1]] = regs[i[1]] - 1
        elif i[0] == 'jnz':
            if read(i[1]):
                pc += int(i[2])
                continue
        pc += 1
            
    return regs['a']

print('Answer #1:', answer(a=0, b=0, c=0, d=0))
print('Answer #2:', answer(a=0, b=0, c=1, d=0))
