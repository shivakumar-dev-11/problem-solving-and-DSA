array = [67,32,9,54,76]
for i in range (0, len(array)-1, +1): 
    if i == 0:
        temp = array[i]  
    array[i] = array[i+1]
array[len(array)-1] = temp
print(array)