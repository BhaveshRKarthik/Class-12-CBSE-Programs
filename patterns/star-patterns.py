x = int(input("Enter number of rows(-ish):\t"))

for i in range(1, 1+x):
    print('*' * i)

print()

for i in range(1, 1+x):
    print(' ' * (x-i) + '*' * i)

print()

for i in range(1, 1+x):
    print('*' * i)
for i in range(x-1, 0, -1):
    print('*' * i)

print()

for i in range(1, 1+x):
    print(' ' * (x-i) + '*' * (i * 2 - 1))

print()

for i in range(1, 1+x):
    print(' ' * (x-i) + '*' * (i * 2 - 1))
for i in range(x-1, 0, -1):
    print(' ' * (x-i) + '*' * (i * 2 - 1))

print()

for i in range(1, 1+x):
    if i == 1:
        print(' ' * (x-1) + '*')
    else:
        print(' ' * (x-i) + '*' + ' ' * (i*2-3) + '*')
for i in range(x-1, 0, -1):
    if i == 1:
        print(' ' * (x-1) + '*')
    else:
        print(' ' * (x-i) + '*' + ' ' * (i*2-3) + '*')