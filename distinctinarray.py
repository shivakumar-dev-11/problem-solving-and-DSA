arr1 = [1,2,3,4,5,6]
arr2 = [2,4,3,5,8,9]
for i in range (0,len(arr1)):
    for j in range (0,len(arr2)):
       if arr1[i] != arr2[j]:
          print(arr1[i])