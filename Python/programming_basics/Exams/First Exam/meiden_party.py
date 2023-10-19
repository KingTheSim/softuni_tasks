love_letter_price = 0.60
wax_price = 7.20
keyring_price = 3.60
painting_price = 18.20
surprise_price = 22

party_price = float(input())
love_letter_number = int(input())
wax_number = int(input())
keyring_number = int(input())
painting_number = int(input())
surprise_number = int(input())

love_letters_final = love_letter_number * love_letter_price
wax_final = wax_number * wax_price
keyring_final = keyring_number * keyring_price
painting_final = painting_number * painting_price
surprise_final = surprise_number * surprise_price

total_number = love_letter_number + wax_number + keyring_number + painting_number + surprise_number
final_price = love_letters_final + wax_final + keyring_final + painting_final + surprise_final

if total_number >= 25:
    final_price = final_price * 0.65

final_price = final_price * 0.9

diff = abs(final_price - party_price)
if final_price >= party_price:
    print(f"Yes! {diff:.2f} lv left.")
else:
    print(f"Not enough money! {diff:.2f} lv needed.")
