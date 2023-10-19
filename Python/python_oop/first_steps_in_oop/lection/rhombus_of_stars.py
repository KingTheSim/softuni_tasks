def print_rhombus(n):
    print_upper_triangle(n)
    print_lower_triangle(n)


def print_upper_triangle(n):
    for i in range(1, n + 1):
        print(" " * (n - i), end="")
        print(*["*"] * i)


def print_lower_triangle(n):
    for i in range(n - 1, 0, -1):
        print(" " * (n - i), end="")
        print(*["*"] * i)


N = int(input())

print_rhombus(N)