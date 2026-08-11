reverse = int (input("enter a number to reverse:"))
count = 0 
while reverse > 0:
    count = count*10 + reverse % 10
    reverse //= 10
print("the reverse of the number is:", count)