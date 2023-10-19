def adder(nums):
    total = 0
    for n in nums:
        total += n
    return total


population = [int(x) for x in input().split(", ")]
minimum = int(input())

whole = adder(population)
if whole / len(population) < minimum:
    unequality = True
else:
    unequality = False
counter = 0
if not unequality:
    for i in population:
        if i < minimum:
            current_max = max(population)
            max_index = population.index(max(population))
            needed = minimum - population[counter]
            population[counter] += needed
            population[max_index] -= needed
        counter += 1
    print(population)
else:
    print("No equal distribution possible")