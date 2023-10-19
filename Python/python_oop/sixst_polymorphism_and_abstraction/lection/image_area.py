class ImageArea:
    def __init__(self, width: int, height: int) -> None:
        self.width = width
        self.height = height

    def get_area(self) -> int:
        return self.width * self.height

    def __lt__(self, other) -> bool:
        return self.get_area() < other.get_area()

    def __le__(self, other) -> bool:
        return self.get_area() <= other.get_area()

    def __eq__(self, other) -> bool:
        return self.get_area() == other.get_area()


a1 = ImageArea(7, 10)
a2 = ImageArea(35, 2)
a3 = ImageArea(8, 9)
print(a1 == a2)
print(a1 != a3)

a1 = ImageArea(7, 10)
a2 = ImageArea(35, 2)
a3 = ImageArea(8, 9)
print(a1 != a2)
print(a1 >= a3)

a1 = ImageArea(7, 10)
a2 = ImageArea(35, 2)
a3 = ImageArea(8, 9)
print(a1 <= a2)
print(a1 < a3)