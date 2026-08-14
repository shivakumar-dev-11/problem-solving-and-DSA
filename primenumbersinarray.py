arr = [2, 3, 4, 5]
count = 0

for num in arr:
    if num < 2:
        continue

    prime = True

    for i in range(2, num):
        if num % i == 0:
            prime = False
            break

    if prime:
        count += 1

print(count)