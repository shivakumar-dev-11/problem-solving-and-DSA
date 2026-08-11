digit = int (input("Enter a number: "))
original_digit = digit

counteven = 0
countodd = 0
while digit > 0:
    original_digit = digit % 10 
    if  original_digit % 2 == 0: 
        counteven += 1
    else:
        countodd += 1
    digit //= 10
print("The count of even digits is:", counteven)
print("The count of odd digits is:", countodd) 
    