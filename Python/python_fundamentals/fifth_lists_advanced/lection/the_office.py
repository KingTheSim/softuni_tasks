happiness = [int(x) for x in input().split()]
factor = int(input())

combined = 0
for i in range(len(happiness)):
    happiness[i] = happiness[i] * factor
    combined += happiness[i]

average = combined / len(happiness)
happy = [x for x in happiness if x >= average]

if len(happy) >= (len(happiness) / 2):
    print(f"Score: {len(happy)}/{len(happiness)}. Employees are happy!")
else:
    print(f"Score: {len(happy)}/{len(happiness)}. Employees are not happy!")
