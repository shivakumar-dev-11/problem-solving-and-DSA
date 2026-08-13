arr = [1,2,3,4,5]
smallest = arr [0]
second_smallest = arr[1]

for i in range (1, len(arr), -1):
    if arr[i] < smallest :
        smallest = smallest
        smallest = arr[i]

print (smallest)

