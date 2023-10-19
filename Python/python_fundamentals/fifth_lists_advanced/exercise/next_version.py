def increaser(n1, n2, n3):
    n3 += 1
    if n3 == 10:
        n3 = 0
        n2 += 1

        if n2 == 10:
            n2 = 0
            n1 += 1
    return f"{n1}.{n2}.{n3}"


major, minor, patch = [int(x) for x in input().split(".")]
new_version = increaser(major, minor, patch)

print(new_version)
