def loader(num):
    if num == 100:
        print("100% Complete!")
        print("[%%%%%%%%%%]")
    else:
        current = num // 10
        print(f"{num}% ",end="")
        print("[", end="")
        for a in range(current):
            print("%",end="")
        for b in range(current, 10):
            print(".",end="")
        print("]")
        print("Still loading...")


number = int(input())
loader(number)
