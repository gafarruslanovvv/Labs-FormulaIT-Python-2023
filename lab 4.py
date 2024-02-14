class GeometricShape:
    def __init__(self, name: str):
        self.name = name

    def __str__(self) -> str:
        return f"This is a {self.name}"

    def __repr__(self) -> str:
        return f'GeometricShape(name={self.name})'


class Rectangle(GeometricShape):
    def __init__(self, name: str, length: float, width: float):
        super().__init__(name)
        self.length = length
        self.width = width

    def calculate_area(self) -> float:
        return self.length * self.width

    def calculate_perimeter(self) -> float:
        return 2 * (self.length + self.width)


class Circle(GeometricShape):
    def __init__(self, name: str, radius: float):
        super().__init__(name)
        self.radius = radius

    def calculate_area(self) -> float:
        return 3.14 * self.radius ** 2

    def calculate_circumference(self) -> float:
        return 2 * 3.14 * self.radius


if __name__ == "__main__":
    rectangle = Rectangle("Rectangle", 5.0, 3.0)
    print(rectangle)
    print("rectangle area = ", rectangle.calculate_area())
    print("rectangle perimeter = ", rectangle.calculate_perimeter())

    circle = Circle("Circle", 4.0)
    print(circle)
    print("circle area = ", circle.calculate_area())
    print("circle primeter = ", circle.calculate_circumference())