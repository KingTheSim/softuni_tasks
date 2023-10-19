def comp(number):
    if 2.00 <= number <= 2.99:
        print("Fail")
    elif 3.00 <= number <= 3.49:
        print("Poor")
    elif 3.50 <= number <= 4.49:
        print("Good")
    elif 4.50 <= number <= 5.49:
        print("Very Good")
    elif 5.50 <= number <= 6.00:
        print("Excellent")


grade = float(input())
comp(grade)
