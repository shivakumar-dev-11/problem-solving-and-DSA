number = int(input("Enter a number: "))

def count_digits(number):
    temp = 0
    while (number > 0):
        rem = number % 10
        temp = temp * 10 + rem
        number = number // 10
    return ("Reversed number:", temp)
print(count_digits(number))