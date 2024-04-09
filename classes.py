class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        
    def find_perimeter(self):
        perimeter = 2 * (self.width + self.height )
        print(perimeter)

    def find_area(self):
        area = (self.width * self.height)
        print(area)

#Creating Objects
First = Rectangle(20, 3)
Second = Rectangle( 40, 5)

#Using objects
First.find_perimeter()
Second.find_area()
First.find_area()
Second.find_perimeter()