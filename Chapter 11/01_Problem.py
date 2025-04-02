
class Vector2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def show(self):
        print(f"The Vector is {self.x}, {self.y}")

class Vector3D(Vector2D):
    def __init__(self, x, y, z):
        super().__init__(x, y)
        self.z = z

    def show(self):
        print(f"The Vector is {self.x}, {self.y}, {self.z}")        


obj1 = Vector2D(2, 3)
obj2 = Vector3D(4, 5, 6)

obj1.show()
obj2.show()