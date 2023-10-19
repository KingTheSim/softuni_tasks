longest = set()

for _ in range(int(input())):
    first_info, second_info = [el.split(",") for el in input().split("-")]
    first = set(range(int(first_info[0]), int(first_info[1]) + 1))
    second = set(range(int(second_info[0]), int(second_info[1]) + 1))

    current = first.intersection(second)
    if len(current) > len(longest):
        longest = current

print(f"Longest intersection is {list(longest)} with length {len(longest)}")
