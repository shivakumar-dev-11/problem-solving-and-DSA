number = int (input("enter an number"))
addition=0
i = 1
while i < number :
    if number % i ==0:
        addition+=i 
       
   
    i+=1
if addition == number:
    print("true")
else:
    print("false")