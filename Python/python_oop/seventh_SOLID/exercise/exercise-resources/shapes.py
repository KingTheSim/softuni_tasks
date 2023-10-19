from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def __init__(self) -> None:
        pass

    @abstractmethod
    def area(self) -> int or float:
        pass


class Rectangle(Shape):

    def __init__(self, width: int or float, height: int or float) -> None:
        self.width = width
        self.height = height

    def area(self) -> int or float:
        return self.width * self.height


class Triangle(Shape):
    def __init__(self, side: int or float, height: int or float):
        self.side = side
        self.height = height

    def area(self) -> int or float:
        return (self.side * self.height) / 2


class AreaCalculator:

    def __init__(self, shapes: list[Shape]) -> None:
        self.shapes = shapes

    @property
    def shapes(self) -> list[Shape]:
        return self.__shapes

    @shapes.setter
    def shapes(self, value) -> None or AssertionError:
        if isinstance(value, list):
            self.__shapes = value

        else:
            raise AssertionError(f"`shapes` should be of type `list`.")

    @property
    def total_area(self) -> int or float:
        total = 0
        for shape in self.shapes:
            total += shape.area()

        return total


shapes = [Rectangle(1, 6), Triangle(2, 3)]
calculator = AreaCalculator(shapes)
print("The total area is: ", calculator.total_area)
