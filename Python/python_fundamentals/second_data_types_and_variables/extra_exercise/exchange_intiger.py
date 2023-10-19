a = input()
b = input()

c = a
print("Before:")
print(f"a = {a}")
print(f"b = {b}")

a = b
b = c

print("After:")
print(f"a = {a}")
print(f"b = {b}")
