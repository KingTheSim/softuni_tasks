def drawer(number):
    print("*" * number)
    if number == 1:
        print("#")
        return
    drawer(number - 1)
    print("#" * number)


target = int(input())

drawer(target)
