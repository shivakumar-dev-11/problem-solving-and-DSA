for i in range(1, 6):
    for j in range(1, 6):
        print("*", end="")
    print()


for i in range(1, 7):
    for j in range(1, i):
        print("*", end="")
    print()


n=5
for i in range(n, 0, -1):
    for j in range (n-i):
        print(" ",end="")
    for j in range(2 * i - 1):
        print("*", end="")
     
    print()





for i in range(1, n):
    for j in range( n-i):
        print(" ", end="")
    for j in range(2 * i - 1):
        print("*", end="")
    print()
for i in range(n, 0, -1):
    for j in range (n-i):
        print(" ",end="")
    for j in range(2 * i - 1):
        print("*", end="")
     
    print()

numbers = [22, 36, 4, 98, 12, 54]
length = len(numbers)
maximumnumber = max(numbers)
print(maximumnumber)


arraynumber = [22, 36, 4, 98, 12, 54]
length = len(arraynumber)
maximumnumber = max(arraynumber)
print(maximumnumber)

count = 0
def count_digits(number):
    while (number > 0):
        number = number // 10
        count += 1
    return count