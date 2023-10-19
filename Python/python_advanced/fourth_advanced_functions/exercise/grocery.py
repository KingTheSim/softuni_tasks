def grocery_store(**kwargs):
    resulting = []
    for product, quantity in dict(sorted(kwargs.items(), key=lambda x: (-x[1], -len(x[0]), x[0]))).items():
        resulting.append(f"{product}: {quantity}")
    return "\n".join(resulting)


print(grocery_store(
 bread=5,
 pasta=12,
 eggs=12,
))

print(grocery_store(
 bread=2,
 pasta=2,
 eggs=20,
 carrot=1,
))