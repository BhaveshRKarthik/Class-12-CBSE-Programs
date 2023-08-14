import operator as op

pf = input().split()

stk = []

fn = {'+': op.add, '-': op.sub, '*': op.mul, '/': op.truediv, '^': op.pow}

for c in pf:
    if c not in '+-*/^':
        stk.append(float(c))
    else:
        i = stk.pop()
        j = stk.pop()
        stk.append(fn[c](j, i))

print(stk[0])
