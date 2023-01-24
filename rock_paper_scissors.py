import random

rock = "Rock"
paper = "Paper"
scissors = "Scissors"
games = 0
computer_points = 0
player_points = 0
print("If you want to stop the game - write 'stop'")
player_name = input("Enter your name: ")

while games <= 3:
    player_move = input("Choose [r]ock, [p]aper or [s]cissors: ")

    if player_move == "stop":
        print("Bye!")
        break

    if player_move == "r":
        player_move = rock
    elif player_move == "p":
        player_move = paper
    elif player_move == "s":
        player_move = scissors
    else:
        print("Invalid Input! Try again...")
        continue

    random_number = random.randint(1, 3)

    computer_move = ""

    if random_number == 1:
        computer_move = scissors
    elif random_number == 2:
        computer_move = rock
    else:
        computer_move = paper

    if (player_move == rock and computer_move == scissors) or \
            (player_move == paper and computer_move == rock) or \
            (player_move == scissors and computer_move == paper):
        player_points += 1
        print(f"{player_name} Win The Round!")
    elif player_move == computer_move:
        print("Draw!")
    else:
        computer_points += 1
        print(f"Computer Win The Round!")

    if player_points == 2:
        print(f"{player_name} Win The Game!!!")
        break
    elif computer_points == 2:
        print("Computer Win The Game!!!")
        break
