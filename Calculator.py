from os import get_terminal_size

while True:
    op = input("Insert operator: (one of +, -, *, /, //, **, %):\t")
    a = input("Insert first number:\t")
    b = input("Insert second number:\t")
    if op == '+':
        print(f"{a + b = }")
    elif op == '-':
        print(f"{a - b = }")
    elif op == '*':
        print(f"{a * b = }")
    elif op == '/':
        print(f"{a / b = }")
    elif op == '//':
        print(f"{a // b = }")
    elif op == '**':
        print(f"{a ** b = }")
    elif op == '%':
        print(f"{a % b = }")
    else:
        print("Invalid operator.")
    resp = input("Do you wish to continue? y/n:\t").lower()
    if resp != 'y' and resp != 'yes':
        break
    else:
        print('-' * (get_terminal_size().columns - 1))
