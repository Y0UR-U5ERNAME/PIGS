import re

def initvar(v):
    if v not in variables:
        variables[v] = 0

def clamp(n): n = n % (2 ** 32)


program = input()
program = re.sub('[^PIGS+-=:#01]', '', program)
#print('Compressed Program:', program + '\n')

variables = {0: 0}
commands = [i for i in re.findall('([PIGS+-=:#])([01]+)', program) if i[0] in 'PIGS+-=:#']
#print(commands)

c = 0
pv = 0

while c < len(commands):
    i, j = commands[c]
    j = int(j, 2)
    initvar(j)
    J = variables[j]
    if i == 'P':
        try:
            print(chr(J), end='', flush=True)
        except:
            pass
    elif i == 'I':
        inp = input()
        for k in range(len(inp)):
            idx = J + k
            clamp(idx)
            variables[idx] = ord(inp[k])
    elif i == 'G':
        c = J - 1
    elif i == 'S':
        pv = J
        initvar(pv)
    elif i == '+':
        variables[pv] += J
        clamp(variables[pv])
    elif i == '-':
        variables[pv] -= J
        clamp(variables[pv])
    elif i == '=':
        variables[pv] = int(variables[pv] == J)
    elif i == ':':
        initvar(J)
        variables[pv] = variables[J]
    elif i == '#':
        variables[pv] = j
        clamp(variables[pv])
    c += 1
