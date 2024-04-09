'''
lists = [23, 45, 67]
#lists = [24, 56 ,78]
#print(sum(lists))
for values in list:
    total=+ values
    print(total)
'''
'''
# copy function
original_dict = {'a': 1, 'b':2}

#Creating a shallow copy of the original_dict
copied_dict = original_dict.copy()

#Modifying the copied_dict
copied_dict['c'] = 3

print(original_dict)
print(copied_dict)
'''
#Finding the average for each student

student_grades = {
    'Tessie': [89, 76, 89, 65],
    'Kabete': [12, 45, 86, 34],
    'Solomom': [34, 67, 28, 10],
    'John': [11, 98, 56, 77],
    'Benjamin': [90, 34, 74, 67]
}
student_average = {}
for key, values in student_grades.items():
    student_average[key] = sum(values) / len(values)
print(student_average)

#Student with the highest average grade
highest_student = max(student_average, key=student_average.get)
#print(highest_student)
highest_grade = student_average[highest_student]
#print(highest_grade)
print(f'{highest_student} : {highest_grade}')

#Students above the threshold
pass_mark = 50
for k, v in student_average.items():
    if v > pass_mark:
        print(f'{k}: {v}')


products = [
    {'name': 'laptop', 'price': 1200},
    {'name': 'Smartphone', 'price': 800},
    {'name': 'Tablet', 'price': 500},
    {'name': 'Headphones', 'price': 120}
]

for item in products:
       #print(item)
       
       product_price = {}
       for name, price in item.items():
           product_price[name] = price
       #print(product_price)
           highest_product_price = max(product_price[price], key=product_price.get)
           print(highest_product_price)
        