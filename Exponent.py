a = int(input("Enter base:\t"))
b = int(input("Enter exponent:\t"))
exp = 1
while b:
    b -= 1
    exp *= a
print(f"{exp} is the value of the exponential expression.")