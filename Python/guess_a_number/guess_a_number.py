import random
while True:
    # Number generation
    computer_number = random.randint(1, 100)

    while True:
        player_input = input("Guess the number 1-100: ")

        # Type check
        if not player_input.isdigit():
            print("Invalid input. Try again...")
            continue
        else:
            player_number = int(player_input)

        # Comparison
        if player_number == computer_number:
            print("You guessed it!")
            break
        elif player_number > computer_number:
            print("Too High!")
        else:
            print("Too Low!")

    while True:
        repeating = input("Would you like to play again? Type [yes] or [no]: ")
        if repeating not in ["yes", "no"]:
            print("Invalid input. Try again...")
        elif repeating == "no":
            print("Thank you for playing!")
            exit()
        else:
            break
