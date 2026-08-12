n = int (input("enter an number "))
count = 0 
original = n 
temp = n

while temp> 0:
     count+= 1
     temp//=10
sum =0 
temp = n
while temp >0 :
     digit = temp %10
     sum += digit **count
     temp //=10
if sum == original :
     print ("armstrong")     
else:
     print ("not an armstrong")