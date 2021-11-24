# write a prime numbers from 2 to n

number = int(input("Please enter your number:")) # give number from user

for item in range(2 , number + 1): # consider main number for this loop too
    for j in range(2 , item): # made counter
        if (item % j) == 0:
            break
    else:
        print(item)
#codded by Alireza Rahimi