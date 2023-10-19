# user input
number = int(input())

# logic
for i in range(number + 1):
    if i % 2 == 0:
        print(2 ** i)
