numbers = [int(x) for x in input().split()]

new_numbers = numbers
totaled = 0
while new_numbers:
    current = int(input())
    if current < 0:
        current_numb = new_numbers[0]
        totaled += current_numb
        new_numbers[0] = new_numbers[-1]
        current = 0
    elif current > len(new_numbers) - 1:
        current_numb = new_numbers[-1]
        totaled += current_numb
        new_numbers[-1] = new_numbers[0]
        current = -1
    else:
        current_numb = new_numbers[current]
        totaled += current_numb
    new_numbers.pop(current)
    for i in range(len(new_numbers)):
        if new_numbers[i] <= current_numb:
            new_numbers[i] += current_numb
        else:
            new_numbers[i] -= current_numb

print(totaled)