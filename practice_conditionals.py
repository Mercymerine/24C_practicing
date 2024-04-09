'''
# Write a simple programme that checks for age and tells whethe a user can vote or note
age = int(input('Enter tha age:'))

if (age >= 18 and age <=200):
    print('You can vote')
elif (age < 0 and age > 200):
    print('Invalid value')
else:
    print('You cannot vote')

'''
#In your elif conditions, you check for ranges that are implicitly guaranteed by the flow of your if-elif-else structure. For example, if the program reaches elif(mark>=40 and mark<49):, it's already known that mark is not less than 40 because the first if condition wasn't met. Therefore, you can simplify the conditions by only checking the upper bound of each range.
#For the final else:, it's a good practice to specify the condition explicitly if there's a known upper limit for valid marks (assuming marks are out of 100). This improves readability and ensures that your code only processes expected values. If marks above a certain value (say 100) are not considered valid, it's helpful to add a condition to handle such cases.

'''
amount = int(input('Enter amount:'))

if (amount > 1000 and amount < 12000):
    print('You can withdraw')
elif (amount > 12000):
    print('You need to report before withdrawal')
elif (amount < 0):
    print('You are broke')
elif (amount > 0 and amount <= 100):
    print('Too little to withdraw')
else:
    print('Welcome to the bank')

#write a python programme that takes in student population in a school and determines whether the people should get funding or not. Use extended if statements.
    
population = int(input('Enter population'))

if (population <= 5000):
    print('Your population is too small so we will not fund you.')
elif (population > 5000 and population < 15000):
    print('We will fund you')
elif (population > 15000 and population <= 30000 ):
    print('We will fund half your population')
elif (population <= 0):
    print('Invalid Value') 
else:
    print('Seek for help from the government')
'''

#Write a python program that analyzes student scores and assigns them a grade
    
percentage = int(input('Enter the percentage:'))

if (percentage >=0 and percentage <=39):
    print('E')
elif (percentage <= 49):
    print('D')
elif (percentage <= 59):
    print("C")
elif (percentage <= 69):
    print('B')
elif ( percentage <=100):
    print('A')
else:
    print('invalid value')

