from rectangle import Rectangle

class Square(Rectangle):
    def __init__(self, name, side):
        super().__init__(name, side, side)
        self.shape_type = 'Square'
    
    @property
    def side(self):
        return self.width  # since width and height are the same in a square
    
    @side.setter
    def side(self, new_side):
        if new_side <= 0:
            raise ValueError("Side must be a positive number.")
        self.width = new_side
        self.height = new_side  # ensure both width and height are the same

if __name__ == "__main__":
    s = Square("MNPQ", 4)
    print(s.name)  # call property name from Shape
    print(s.shape_type)  # call property shape_type from Shape
    print(s.area)  # call property area from Rectangle (overridden from abstract method in Shape)
    print(s)  # call __str__ method from Rectangle (overridden from Shape)
    print(f'Side length: {s.side}')  # call side property
    s.side = 6  # change side length
    print(s)
