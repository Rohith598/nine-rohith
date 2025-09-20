import math
class shape:
    def area(self):
        pass
class circle:
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        return math.pi*self.radius**2
class rectangle:
    def __init__(self,length,breadth):
        self.lenght=length
        self.breadth=breadth
    def area(self):
        return self.lenght*self.breadth
circle=circle(5)
rectangle=rectangle(4,6)
print(circle.area())
print(rectangle.area())