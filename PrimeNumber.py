# write a prime numbers from 2 to n

number = int(input("Please enter your number:")) # give number from user

for item in range(2 , number + 1): # consider main number for this loop too
    for j in range(2 , item): # made counter
        if (item % j) == 0: # if the answer for dividing item will be zero, don't consider that number
            break # break and exit the loop
    else:
        print(item) # give us answer
#codded by ALIREZA RAHIMI