number = int (input("enter an number"))
count = 0 
i = 1
while i <= number :
    if number % i == 0:
        count+=1
    i+=1

if count == 2:
    print ("prime number")
else:
      print("not prime") 
