number = int(input("Enter a number: "))
count = 0
def count_digits(number):
    while (number > 0):
        number //= 10
        count += 1
    return count
print(count_digits(number))
