def lenghter(passw):
     return len(passw) < 6 or len(passw) > 10


def char_checker(passw):
    return not passw.isalnum()


def num_checker(passw):
    counter = 0
    for i in passw:
        if i.isdigit():
            counter += 1
        if counter == 2:
            break
    return not counter == 2


password = input()

valid = True
if lenghter(password):
    valid = False
    print("Password must be between 6 and 10 characters")

if char_checker(password):
    valid = False
    print("Password must consist only of letters and digits")

if num_checker(password):
    valid = False
    print("Password must have at least 2 digits")

if valid:
    print("Password is valid")
