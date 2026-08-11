digit = int (input("Enter a number: "))
count = 0 
while digit > 0:
    last_digit = digit % 10
    if last_digit % 2 != 0:
        count += last_digit
    digit //= 10
print("The sum of odd digits is:", count)