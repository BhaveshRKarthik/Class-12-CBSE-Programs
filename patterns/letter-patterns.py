x = int(input("Enter number of rows(-ish):\t"))

for i in range(1, 1+x):
    for j in range(i):
        print(chr(65+j), end='')
    print()

print()

for i in range(1, 1+x):
    print(' ' * (x-i), end='')
    for j in range(i):
        print(chr(65+j), end='')
    print()


print()

for i in range(1, 1+x):
    for j in range(i):
        print(chr(65+j), end='')
    print()
for i in range(x-1, 0, -1):
    for j in range(i):
        print(chr(65+j), end='')
    print()


print()

for i in range(1, 1+x):
    print(' ' * (x-i), end='')
    for j in range(i):
        print(chr(65+j), end='')
    for j in range(i-1, 0, -1):
        print(chr(65+j), end='')
    print()
    

print()

for i in range(1, 1+x):
    print(' ' * (x-i), end='')
    for j in range(i):
        print(chr(65+j), end='')
    for j in range(i-1, 0, -1):
        print(chr(65+j), end='')
    print()
for i in range(x-1, 0, -1):
    print(' ' * (x-i), end='')
    for j in range(i):
        print(chr(65+j), end='')
    for j in range(i-1, 0, -1):
        print(chr(65+j), end='')
    print()