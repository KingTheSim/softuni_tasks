# user input
type_scr = input()
row_num = int(input())
cols_num = int(input())

# logic
price = 0
all_seats = row_num * cols_num

if type_scr == "Premiere":
    price = 12.00
elif type_scr == "Normal":
    price = 7.50
else:
    price = 5.00

# code output
final_price = all_seats * price
print(f"{final_price:.2f} leva")
