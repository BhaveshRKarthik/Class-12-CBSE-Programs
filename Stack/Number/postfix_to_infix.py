pf = input().split()
stk = []

for c in pf:
    if c not in '+-*/^':
        stk.append(c)
    else:
        i = stk.pop()
        j = stk.pop()
        stk.append(f'({j} {c} {i})')
        
print(stk[0])
