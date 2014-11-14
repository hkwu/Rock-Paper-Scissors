__author__ = 'Kelvin Wu'

import random

game_version = "Rock Paper Scissors v1.0"
print(game_version)


def true_or_not(string):
    if not string.lower() in ["y", "yes", "n", "no"]:
        print("That is not a valid answer. Try again.")
        return true_or_not(input("Play again? "))
    elif string.lower() in ["y", "yes"]:
        return True
    elif string.lower() in ["n", "no"]:
        return False


def nat_to_choice(nat):
    if nat == 1:
        return "Rock"
    elif nat == 2:
        return "Paper"
    else:
        return "Scissors"

while True:
    play_or_not = input("Do you want to play? ")
    if play_or_not.lower() in ["y", "yes"]:
        next_round = True
        while next_round:
            computer_choice = random.randint(0, 3)
            player_choice = input("Choose your move. ")
            if not player_choice.lower() in ["rock", "paper", "scissors"]:
                print("That is not a valid move. Try again.")
            elif player_choice.capitalize() == "Rock" and nat_to_choice(computer_choice) == "Scissors":
                print("Rock beats Scissors. You win.")
                next_round = true_or_not(input("Play again? "))
            elif player_choice.capitalize() == "Paper" and nat_to_choice(computer_choice) == "Rock":
                print("Paper beats Rock. You win.")
                next_round = true_or_not(input("Play again? "))
            elif player_choice.capitalize() == "Scissors" and nat_to_choice(computer_choice) == "Paper":
                print("Scissors beats Paper. You win.")
                next_round = true_or_not(input("Play again? "))
            elif player_choice.capitalize() == nat_to_choice(computer_choice):
                print("You chose {0} and your opponent chose {1}. It's a tie.".format(player_choice.capitalize(), nat_to_choice(computer_choice)))
                next_round = true_or_not(input("Play again? "))
            else:
                print("You chose {0} and your opponent chose {1}. You lost.".format(player_choice.capitalize(), nat_to_choice(computer_choice)))
                next_round = true_or_not(input("Play again? "))
        else:
            print("Thanks for trying {0:s}.".format(game_version))
            break
    elif play_or_not.lower() in ["n", "no"]:
        print("Thanks for trying {0:s}.".format(game_version))
        break
    else:
        print("That is not a valid answer. Try again.")