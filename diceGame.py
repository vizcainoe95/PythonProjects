# Multiplayer dice game where you roll a die, get a number 1-6, and roll until you hit 1.
# Rolling a number raises your score based on the number rolled on the dice.
# If you roll a 5, add 5 to your score. 
# Once you roll a 1, your score is reset and the next player's turn begins.
# Reaching a score of 50 means you win.

import random

def roll():
    min_value = 1
    max_value = 6
    roll = random.randint(min_value, max_value)

    return roll

# value = roll()
# print(value)

while True:
    players = input("Enter the numnber of players (2-4): ")
    if players.isdigit():   #checks to see if there's a digit
        players = int(players)
        if 2 <= players <= 4:
            break
        else:
            print("Must be between 2-4 players.")
    else:
        print("Invalid, try again.")

# print(players)

max_score = 50
player_scores = [0 for _ in range(players)]

#print(player_scores)

while max(player_scores) < max_score:

    for player_index in range(players):
        print("\nPlayer ", player_index + 1, "turn has just started!\n")
        print("Your total score is: ", player_scores[player_index], "\n")
        current_score = 0

        while True:
            should_roll = input("Would you like to roll? (y) or (n)")
            if should_roll.lower() != "y":
                break

            value = roll()
            if value == 1: 
                print("You rolled a 1! Turn done!")
                current_score = 0
                break
            else:
                current_score += value
                print("You rolled a: ", value)

            print("Your score is: ", current_score)

        player_scores[player_index] += current_score
        print("Your total score is: ", player_scores[player_index])

max_score = max(player_scores)
winner_index = player_scores.index(max_score)
print("Player ", winner_index + 1, "is the winner with a score of: ", max_score)
