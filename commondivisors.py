num1 = int (input("enter an number"))
num2 = int (input ("enter an number"))

i = 1 
while i <= num1 and i<=num2:
    if num1%i ==0 and num2 %i ==0:
        print(i)
    i+=1
