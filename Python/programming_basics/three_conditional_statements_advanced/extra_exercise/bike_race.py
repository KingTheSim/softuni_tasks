# user input
j_num = int(input())
s_num = int(input())
type_track = input()

# logic
j_price = 0
s_price = 0
if type_track == "trail":
    j_price = 5.50 * j_num
    s_price = 7.00 * s_num
elif type_track == "cross-country":
    j_price = 8.00 * j_num
    s_price = 9.50 * s_num
    if j_num + s_num >= 50:
        j_price = j_price * 0.75
        s_price = s_price * 0.75
elif type_track == "downhill":
    j_price = 12.25 * j_num
    s_price = 13.75 * s_num
else:
    j_price = 20.00 * j_num
    s_price = 21.50 * s_num
total = (j_price + s_price) * 0.95

# code output
print(f"{total:.2f}")
