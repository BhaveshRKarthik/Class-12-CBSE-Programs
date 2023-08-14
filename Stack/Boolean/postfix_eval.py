import operator as op

pf = input().split()

stk = []

fn = {'&': op.and_, '|': op.or_}

for c in pf:
    if c not in '~&|':
        stk.append(bool(int(c)))
    elif c == '~':
        stk.append(bool(1-stk.pop()))
    else:
        i = stk.pop()
        j = stk.pop()
        stk.append(fn[c](j, i))

print(stk[0])
