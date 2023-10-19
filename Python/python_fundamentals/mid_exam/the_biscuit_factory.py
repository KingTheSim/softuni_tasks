daily_biscuits = int(input())
workers = int(input())
competer = int(input())

total = 0
for i in range(1, 31):
    if i % 3 == 0:
        produced = (daily_biscuits * workers) * 0.75
        produced = int(produced)
    else:
        produced = int(daily_biscuits * workers)

    total += produced

print(f"You have produced {total} biscuits for the past month.")

difference = abs(total - competer)
percentage = difference / competer * 100

if total < competer:
    print(f"You produce {percentage:.2f} percent less biscuits.")
else:
    print(f"You produce {percentage:.2f} percent more biscuits.")
