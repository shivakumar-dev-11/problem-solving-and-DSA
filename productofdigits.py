product = int (input ("enter an number for product of digits:"))
count = 1
while product > 0:
    count = count * (product % 10)
    product = product // 10
print("the product of the digits is:", count)