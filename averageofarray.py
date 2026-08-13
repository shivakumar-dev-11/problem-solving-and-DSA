arr = [1,2,3,4,5,6]
n = len(arr)
total = 0 
avg = 0
for i in range(0, len(arr)):
    total += arr[i]
    avg = total//n
    
print (avg)