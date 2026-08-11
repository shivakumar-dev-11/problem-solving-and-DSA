digit = int (input ("enter a number to find first and last digit:"))
last_digit = digit % 10
while digit >= 10:
    digit //= 10
first_digit = digit
print("the first digit is:", first_digit)
print("the last digit is:", last_digit)