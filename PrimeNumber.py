#write a prime numbers from 2 to n

number = int(input("Please enter your number:"))

for item in range(2 , number + 1):
    for j in range(2 , item):
        if (item % j) == 0:
            break
    else:
        print(item)