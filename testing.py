'''
# using counter
from collections import Counter

#Create a Counter object from a list
numbers = [1, 2, 3, 4, 1, 2, 3, 1, 2]
number_counts = Counter(numbers)
print(number_counts)

#Access the count of a specific element
print(number_counts[1])

#Find the most common elements
print(number_counts.most_common())
'''
import re

pattern = re.compile('^Hello')

result = pattern.sub('Hi', 'Hello, world!Hello')

print(result)