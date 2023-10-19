def concatenate(*args, **kwargs):
    args = "".join(args)
    for key, val in kwargs.items():
        if key in args:
            args = args.replace(key, val)

    return args


print(concatenate("Soft", "UNI", "Is", "Grate", "!",
                  UNI="Uni", Grate="Great"))

print(concatenate("I", " ", "Love", " ", "Cythons",
C="P", s="", java='Java'))
