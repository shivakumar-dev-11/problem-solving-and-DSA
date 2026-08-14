arr =[1,3,2,4,5,6,7]
for i in range (0,len(arr)-1 ):
    if arr[i] <= arr[i+1]:
         continue
    else:
        print ("they are not in increasing order")
    break
else:
 print("they are in increasing order")