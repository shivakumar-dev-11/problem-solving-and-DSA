arr =[1,3,2,4,5,6]
count = 0 
x = int (input("enter an number"))
for i in range (0, len(arr), +1):
    if x == arr[i]:
     count+=1
print(count)
    