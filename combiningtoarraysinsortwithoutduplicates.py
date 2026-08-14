arr1 =[1,2,2,2,3,3,4]
arr2 = [2,3,4,4,6,6,7,8,8]
arr=[]
for i in range (0 , len(arr)):
    for j in range (0, len(arr)):
      if arr1[i] < arr2[j]:
         arr+=arr1[i]
    
         