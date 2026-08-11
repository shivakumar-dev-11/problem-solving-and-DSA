sum =  int(input("enter a number:"))

count = 0
while sum > 0:
    count += sum % 10
    sum = sum // 10

print("the sum of the digits is:", count)
