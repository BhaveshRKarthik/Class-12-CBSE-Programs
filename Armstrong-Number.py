num = int(input("Enter number:\t"))
num_saved = num
num_of_digits = 0

while num:
    num_of_digits += 1
    num //= 10

num = num_saved
arm = 0

while num:
    arm += (num%10) ** num_of_digits
    num //= 10

if num_saved == arm:
    print(f"{num_saved} is an Armstrong Number")
else:
    print(f"{num_saved} is not an Armstrong Number")