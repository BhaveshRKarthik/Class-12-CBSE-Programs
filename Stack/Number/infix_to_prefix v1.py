s = input().split()

stk = []

pf = []

for c in s:
    if c == '(':
        stk.append('(')
    elif c == ')':
        while stk and stk[-1] in '/^*+-(':
            if stk[-1] == '(': stk.pop(); break
            pf.append(stk.pop())
    elif c == '+':
        while stk and stk[-1] in '/^*+-':
            pf.append(stk.pop())
        stk.append('+')
    elif c == '-':
        while stk and stk[-1] in '/^*+-':
            pf.append(stk.pop())
        stk.append('-')
    elif c == '*':
        while stk and stk[-1] in '/^*':
            pf.append(stk.pop())
        stk.append('*')
    elif c == '/':
        while stk and stk[-1] in '/^*':
            pf.append(stk.pop())
        stk.append('/')
    elif c == '^':
        stk.append('^')
    else: # number/letter
        pf.append(c)
else:
    pf += stk[::-1]

stk = []

for c in pf:
    if c not in '+-*/^':
        stk.append(c)
    else:
        i = stk.pop()
        j = stk.pop()
        stk.append(f'{c} {j} {i}')
        
print(stk[0])
