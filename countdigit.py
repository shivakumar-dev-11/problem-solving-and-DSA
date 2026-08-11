digit =  int(input("enter an number:"))


count = 0 
while digit >0:
    digit = digit // 10
    count += 1
print("the number of digits in the number is:", count)