def rectangle(length, width):
    if not isinstance(length, int) or not isinstance(width, int):
        return "Enter valid values!"

    def area(length, width):
        return length * width

    def perimeter(length, width):
        return (length + width) * 2

    return f"Rectangle area: {area(length, width)}\n" \
           f"Rectangle perimeter: {perimeter(length, width)}"


print(rectangle(2, 10))
print(rectangle('2', 10))