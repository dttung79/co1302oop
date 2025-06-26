from shape import Shape

class Rectangle(Shape):
    def __init__(self, name, width, height):
        super().__init__(name, 'Rectangle')
        self.width = width
        self.height = height

    @property
    def width(self):
        return self._width
    
    @width.setter
    def width(self, new_width):
        if new_width <= 0:
            raise ValueError("Width must be a positive number.")
        self._width = new_width

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, new_height):
        if new_height <= 0:
            raise ValueError("Height must be a positive number.")
        self._height = new_height

    # overriding the abstract method from Shape
    @property
    def area(self):
        return self.width * self.height

    def __str__(self):
        shape_info = super().__str__()
        return f'{shape_info} ({self.width} x {self.height})'
    

## Test the Rectangle class
if __name__ == "__main__":
    rect = Rectangle("ABCD", 5, 10)
    print(rect.name)  # call property name from Shape
    print(rect.shape_type)  # call property shape_type from Shape
    print(rect.area)  # call property area from Rectangle (overridden from abstract method in Shape)
    print(rect)  # call __str__ method from Rectangle (overridden from Shape)