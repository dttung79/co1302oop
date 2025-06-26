from eclipse import Eclipse

class Circle(Eclipse):
    def __init__(self, name, radius):
        super().__init__(name, radius, radius)  # For a circle, h_radius and v_radius are the same
        self.shape_type = 'Circle'

    @property
    def radius(self):
        return self.h_radius  # or self.v_radius, since they are the same for a circle

    @radius.setter
    def radius(self, new_radius):
        if new_radius <= 0:
            raise ValueError("Radius must be a positive number.")
        self.h_radius = new_radius
        self.v_radius = new_radius  # Ensure both radii are updated

if __name__ == "__main__":
    c = Circle("O", 5)
    print(c.name)  # call property name from Shape
    print(c.shape_type)  # call property shape_type from Shape
    print(c.area)  # call property area from Eclipse (overridden from abstract method in Shape)
    print(c)  # call __str__ method from Eclipse (overridden from Shape)
    print(f'Radius: {c.radius}')  # call radius property
    c.radius = 7  # change radius
    print(c)
