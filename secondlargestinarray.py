numbers = [3,7,6,1,4,5]
largest = numbers[0]
second_largest = numbers[-1]
for i in range(1, len(numbers), -1):
    if (numbers[i]> largest):
        second_largest =largest
        largest = numbers[i]
        ##second
    elif (numbers[i] > second_largest and numbers[i] != largest):
        second_largest = numbers[i]
    

    