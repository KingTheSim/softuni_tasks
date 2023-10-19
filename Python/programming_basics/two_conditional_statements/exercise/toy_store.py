# known
puzzle_price = 2.60
doll_price = 3
bear_price = 4.10
minion_price = 8.20
truck_price = 2

# user input
trip_price = float(input())
puzzles_number = int(input())
dolls_number = int(input())
bears_number = int(input())
minions_number = int(input())
trucks_number = int(input())

# logic
puzzles_sum = puzzle_price * puzzles_number
dolls_sum = doll_price * dolls_number
bears_sum = bear_price * bears_number
minions_sum = minion_price * minions_number
trucks_sum = truck_price * trucks_number

total_sum = puzzles_sum + dolls_sum + bears_sum + minions_sum + trucks_sum
total_toys_number = puzzles_number + dolls_number + bears_number + minions_number + trucks_number

if total_toys_number >= 50:
    total_sum -= total_sum * 0.25
final_sum = total_sum * 0.9

# code output
if final_sum >= trip_price:
    print(f"Yes! {final_sum - trip_price:.2f} lv left.")
else:
    print(f"Not enough money! {trip_price - final_sum:.2f} lv needed.")
