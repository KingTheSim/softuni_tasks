def age_assignment(*args, **kwargs):
    people = {}
    for letter, age in kwargs.items():
        for name in args:
            if name.startswith(letter):
                people[name] = age
                break

    people = dict(sorted(people.items()))

    return "\n".join(f"{name} is {age} years old." for name, age in people.items())

print(age_assignment("Peter", "George", G=26, P=19))

print(age_assignment("Amy", "Bill", "Willy", W=36,
                     A=22, B=61))
