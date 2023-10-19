n = int(input())

liters_total = 0
degrees_total = 0
for i in range(n):
    liters = float(input())
    degrees = float(input())

    liters_total += liters
    degrees_total += degrees * liters

av_degrees = degrees_total / liters_total

print(f"Liter: {liters_total:.2f}")
print(f"Degrees: {av_degrees:.2f}")

if av_degrees < 38:
    print("Not good, you should baking!")
elif av_degrees <= 42:
    print("Super!")
else:
    print("Dilution with distilled water!")
