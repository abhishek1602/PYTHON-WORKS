#Done Randomnumbers

# write a function that takes an array filled with random numbers from 1 to 100 
# and returns the sum of odd values and even values separatly

import random

def rand(numbers):
    even = 0
    odd = 0

    for num in numbers:
        if num % 2 == 0:
            even += num

        else:
            odd += num

    return even,odd

numbers = [random.randint(1,100) for i in range(5)]

even,odd = rand(numbers)

print(f"Numbers: {numbers} \nSum of even: {even} \nSum of odd: {odd}" )
