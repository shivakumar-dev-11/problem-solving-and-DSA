number = int (input("enter the number "))

count = 0
i = 1
while i  <= number :
    if number % i == 0:
     count +=1
    i+=1
print (count)
