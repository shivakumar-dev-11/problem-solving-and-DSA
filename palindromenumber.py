number = int (input ("Enter a number: "))
original = number
count = 0
while number > 0 :
    count = count * 10 + number % 10
    number //= 10
if count == original:
    print("the number is a palindrome")
else:
    print("the number is not a palindrome")
