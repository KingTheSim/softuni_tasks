def definer(input_type):
    if input_type == "int":
        result = int(input())
        result = result * 2
    elif input_type == "real":
        result = float(input())
        result = f"{(result * 1.5):.2f}"
    else:
        result = "$" + input() + "$"

    return result


word = input()

print(definer(word))
