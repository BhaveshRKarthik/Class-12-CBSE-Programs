from os import get_terminal_size

total = b = c = 0

while True:
    ty = input("Insert type of TV:\t").casefold()
    sz = int(input("Insert size of TV: (21, 33 or 55; in inches):\t"))
    if ty != "bw" and ty != "black and white" and ty != "black & white" and ty != "black white" \
        and ty != "colour" and ty != "color" and ty != "c" and c != "b":
        print("Invalid Type of TV.")
    elif sz != 21 and sz != 33 and sz != 55:
        print("Invalid Size of TV.")
    elif ty == "colour" or ty == "color" or ty == "c": # Colour TV
        c += 1
        if sz == 21:
            total += 30000
        elif sz == 33:
            total += 40000
        else:
            total += 60000
    else: # Black and White TV
        b += 1
        if sz == 21:
            total += 20000
        elif sz == 33:
            total += 30000
        else:
            total += 50000
    resp = input("Do you wish to continue? y/n:\t").casefold()
    if resp != 'y' and resp != 'yes':
        break
    else:
        print('-' * (get_terminal_size().columns - 1))

print(f"Your total was: ₹{total}")
if b + c >= 2:
    if c >= 2:
        print(f"You got a 25% discount! Your amount is now ₹{total * 0.75}")
    elif c == 1:
        print(f"You got a 20% discount! Your amount is now ₹{total * 0.8}")
    else:
        print(f"You got a 15% discount! Your amount is now ₹{total * 0.85}")