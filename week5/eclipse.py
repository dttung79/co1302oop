from shape import Shape

class Eclipse(Shape):
    def __init__(self, name, h_radius, v_radius):
        super().__init__(name, 'Eclipse')
        self.h_radius = h_radius
        self.v_radius = v_radius
    
    @property
    def h_radius(self):
        return self._h_radius
    
    @h_radius.setter
    def h_radius(self, new_h_radius):
        if new_h_radius <= 0:
            raise ValueError("Horizontal radius must be a positive number.")
        self._h_radius = new_h_radius

    @property
    def v_radius(self):
        return self._v_radius
    
    @v_radius.setter
    def v_radius(self, new_v_radius):
        if new_v_radius <= 0:
            raise ValueError("Vertical radius must be a positive number.")
        self._v_radius = new_v_radius

    # overriding the abstract method from Shape
    @property
    def area(self):
        return 3.14 * self.h_radius * self.v_radius
    
    def __str__(self):
        shape_info = super().__str__()
        return f'{shape_info} ({self.h_radius} x {self.v_radius})'
    
# Test the Eclipse class
if __name__ == "__main__":
    e = Eclipse("E", 5, 10)
    print(e.name)  # call property name from Shape
    print(e.shape_type)  # call property shape_type from Shape
    print(e.area)  # call property area from Eclipse (overridden from abstract method in Shape)
    print(e)  # call __str__ method from Eclipse (overridden from Shape)
    print(f'Horizontal radius: {e.h_radius}')  # call h_radius property
    print(f'Vertical radius: {e.v_radius}')  # call v_radius property
    e.h_radius = 6  # change horizontal radius
    e.v_radius = 12  # change vertical radius
    print(e)