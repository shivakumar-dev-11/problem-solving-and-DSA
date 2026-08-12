digit1 = int(input("Enter the first digit: "))
digit2 = int(input("Enter the second digit: "))

a, b = digit1, digit2

while b != 0:
    a, b = b, a % b
    gcd = a
print(gcd)