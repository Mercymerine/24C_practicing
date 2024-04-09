# for loop
'''
for number in range(0, 100):
    if (number % 2 == 0):
        print(f'{number} this is an EVEN NUMBER')
    else:
        print(f'{number} this is an ODD NUMBER')
'''
#Write a programme that prints multiples of three in a given range specified by a user
'''
for number in range(0, 100):
    if (number % 3 ==0):
        print(number)
'''
'''
userInput = int(input('Enter a range: '))

for i in range(userInput):
    if (i % 3 ==0):
        print(f'{i} is a multiple of 3')
'''
'''
# while loop
userInput = int(input('Enter number: '))

while (userInput < 10):
   print('Am too young')

userInput = int(input('Enter number: '))

while (userInput < 10):
   userInput = userInput + 1
   print('Am too young')
else:
   print('Am here')
'''
'''
Write a Python program that finds all prime numbers in a given list of integers. The program should:
Take a list of integers as input.
Use a for loop to iterate through the list.
Check each number to see if it is a prime number.
Collect all prime numbers found into a new list.
Print the list of prime numbers.
'''
''' 
Have an input as a list
Have an empty list called prime_numbers
Iterate over each value in the list: if the values is divisible by itself and one alone
Add to the value to the list called prime_numbers
print out the list 
'''
userInput = int(input('Enter list of numbers: '))
prime_numbers = []

for i in range(2, userInput):
    if (i % i ==0  and i % 1 == i ):
        print(i)
        


