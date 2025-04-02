# In Python, the  decorator is used to define methods that act like attributes. 
# It allows you to access a method like you would access an attribute, without explicitly calling the method. 
# This is helpful for managing attributes that require some computation or logic before being returned.


class Circle:
    def __init__(self, radius):
        self._radius = radius  # Private attribute

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        if value >= 0:
            self._radius = value
        else:
            raise ValueError("Radius cannot be negative.")

    @property
    def area(self):
        return 3.1416 * self._radius**2

circle = Circle(5)
print(circle.radius)  # Access the radius using @property
print(circle.area)    # Access the computed area using @property

circle.radius = 10    # Modify radius using the setter method
print(circle.area)    # Output changes as radius is updated