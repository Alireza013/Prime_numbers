# Write a prime numbers from 2 to n
# Using python V3

number = int(input("Please enter your number:")) # Give number from user

for item in range(2 , number + 1): # Consider main number
    for j in range(2 , item): # Made counter
        if (item % j) == 0: # If the answer for dividing item will be zero, don't consider that number
            break # Break and exit the loop

    else:
        print(item) # Give us answer
#Codded by ALIREZA RAHIMI