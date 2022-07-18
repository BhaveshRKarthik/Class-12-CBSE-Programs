num = int(input("Enter number:\t"))
rev = 0
while num:
    rev *= 10
    rev += (num % 10)
    num //= 10
print(f"The reversed number is:\t{rev}")