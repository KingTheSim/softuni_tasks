n = float(input())
below = 0
if n == 0:
    print("zero")
else:
    if n > 0:
        if 0 < n < 1:
            print("small positive")
        elif 1 < n < 1000000:
            print("positive")
        else:
            print("large positive")
    else:
        below = abs(n)
        if 0 < below < 1:
            print("small negative")
        elif 1 < below < 1000000:
            print("negative")
        else:
            print("large negative")
