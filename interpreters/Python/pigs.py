import re, sys

variables = {0: 0}

def initvar(v):
    if v not in variables:
        variables[v] = 0

def clamp(n): n = n % (2 ** 32)

def main(argv=sys.argv):
    if len(argv) < 2:
        print('Please input the file location of a .pigs program.')
        quit()
    elif not argv[1].endswith(".pigs"):
        print('Specified file is not a .pigs file.')
        quit()
    else:
        try:
            prgm = open(argv[1])
        except:
            print('Could not find specified .pigs program.')
            quit()

    program = prgm.read()
    program = re.sub('[^PIGS+-=:#01]', '', program)
    prgm.close()
    #print('Compressed Program:', program + '\n')

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

if __name__ == "__main__":
    main()
