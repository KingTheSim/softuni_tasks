c_flag, o_flag, n_flag = False, False, False

message = ""
whole_message = ""

while True:
    symbol = input()
    if symbol == "End":
        break
    symbol = ord(symbol)

    if 65 <= symbol <= 90 or 97 <= symbol <= 122:
        if symbol in [99, 110, 111]:
            if symbol == 99:
                if c_flag:
                    symbol = chr(symbol)
                    message += symbol
                else:
                    c_flag = True
            elif symbol == 111:
                if o_flag:
                    symbol = chr(symbol)
                    message += symbol
                else:
                    o_flag = True
            elif symbol == 110:
                if n_flag:
                    symbol = chr(symbol)
                    message += symbol
                else:
                    n_flag = True
            if c_flag and o_flag and n_flag:
                message += " "
                c_flag, o_flag, n_flag = False, False, False
                whole_message += message
                message = ""
        else:
            symbol = chr(symbol)
            message += symbol

print(f"{whole_message}")
