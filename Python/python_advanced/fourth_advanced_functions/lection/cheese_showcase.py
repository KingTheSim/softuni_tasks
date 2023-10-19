def sorting_cheeses(**cheeses):
    res = ""
    new_cheeses = dict(sorted(cheeses.items(), key=lambda x: (-len(x[1]), x[0])))
    for cheese, quantities in new_cheeses.items():
        res += cheese + "\n" + '\n'.join(str(c) for c in sorted(quantities, reverse=True)) + "\n"

    return res


print(
 sorting_cheeses(
 Parmesan=[102, 120, 135],
 Camembert=[100, 100, 105, 500, 430],
 Mozzarella=[50, 125],
 )
)


print(
 sorting_cheeses(
 Parmigiano=[165, 215],
 Feta=[150, 515], Brie=[150, 125],
 )
)