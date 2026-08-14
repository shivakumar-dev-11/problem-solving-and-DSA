arr = [1,2,3,4,5,6]
x = int (input("enter the number"))

for i in range (0,len(arr)):
    if arr[i] == x :
      print(i)
      break
else:
 print (-1)




