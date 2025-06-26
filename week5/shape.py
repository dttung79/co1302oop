from abc import ABC, abstractmethod

class Shape(ABC):
    def __init__(self, name, shape_type):
        self.name = name
        self.shape_type = shape_type
    
    @property
    def name(self):
        return self._name   # protected attribute
    
    @name.setter
    def name(self, new_name):
        if new_name == '':
            raise ValueError("Name cannot be an empty string.")
        self._name = new_name

    @property
    def shape_type(self):
        return self._shape_type

    @shape_type.setter
    def shape_type(self, new_shape_type):
        if new_shape_type == '':
            raise ValueError("Shape type cannot be an empty string.")
        self._shape_type = new_shape_type

    
    @property
    @abstractmethod
    def area(self):
        pass

    def __str__(self):
        return f'{self.shape_type} {self.name}: {self.area:.2f}'