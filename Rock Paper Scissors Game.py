import random

def random_logic(_random_key):
    if _random_key == 0:
        random_str = "Rock"

    elif _random_key == 1:
        random_str = "Paper"

    else:
        random_str = "Scissors"

    return random_str


try_the_game = int(input("How many times you want to play it: "))
print('Rock for "R", Paper for "P", Scissors for "S", For Quit the game "Quit"\n\n')
play_time_start = 1

while play_time_start <= try_the_game:

    random_key = random.randint(0, 2)

    random_str = random_logic(_random_key = random_key)
    user_random_str_input = input(f"{play_time_start}. Read The Instraction From Top & Choose One: ").lower()

    if (user_random_str_input == "r"):
        if(random_str == "Rock"):
            print("Rock Vs. Rock (Match Draw!)\n")

        elif (random_str == "Paper"):
            print("Rock Vs. Paper (Opps! You Lose...)\n")

        else:
            print("Rock Vs. Scissors (Yeahoo! You Win...)\n")

    elif (user_random_str_input == "p"):
        if (random_str == "Rock"):
            print("Paper Vs. Rock (Yeahoo! You Win...)\n")

        elif (random_str == "Paper"):
            print("Paper Vs. Paper (Match Draw!)\n")

        else:
            print("Paper Vs. Scissors (Opps! You Lose...)\n")

    elif (user_random_str_input == "s"):
        if (random_str == "Rock"):
            print("Scissors Vs. Rock (Opps! You Lose...)\n")

        elif (random_str == "Paper"):
            print("Scissors Vs. Paper (Yeahoo! You Win...)\n")

        else:
            print("Scissors Vs. Sesar (Match Draw!)\n")

    elif (user_random_str_input == "quit"):
        break

    else:
        print("Invalid Syntax!\n")
        continue

    play_time_start += 1
