text = input()

final_result = text
while True:
    command = input().split()

    if command[0] == "Done":
        print(f"Your password is: {final_result}")
        break

    elif command[0] == "TakeOdd":
        current_res = ""
        for i in range(len(final_result)):
            if i % 2 != 0:
                current_res += final_result[i]
        final_result = current_res
        print(final_result)

    elif command[0] == "Cut":
        current_res = final_result[int(command[1]):int(command[1]) + int(command[2])]
        final_result = final_result.replace(current_res, "", 1)
        print(final_result)

    else:
        if command[1] in final_result:
            final_result = final_result.replace(command[1], command[2])
            print(final_result)
        else:
            print("Nothing to replace!")
