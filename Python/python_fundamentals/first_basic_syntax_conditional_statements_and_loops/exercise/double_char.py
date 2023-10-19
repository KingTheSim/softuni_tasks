while True:
    words = input()

    if words == "End":
        break
    if words == "SoftUni":
        continue

    result = ""
    for char in words:
        result += char * 2

    print(result)
