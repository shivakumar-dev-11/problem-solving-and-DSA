original_number = int(input("enter an number "))
square_number = original_number ** 2

while square_number > 0:
  r1 = square_number % 10
  r2 = original_number % 10
  original_number //= 10
  if r2 != r1:
    print("the number is ")
  