n = int(input())
word = input()

whole_list = []
containing = []
for _ in range(n):
    current = input()
    whole_list.append(current)
    if word in current:
        containing.append(current)

print(whole_list)
print(containing)
