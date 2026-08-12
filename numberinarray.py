array = [3,7,6,1,4,5]
number = int(input("Enter a number to check if it is in the array: "))

for i in range(0, len(array), 1):
    if array[i] == number:
        print(array[i], "is present in the array")