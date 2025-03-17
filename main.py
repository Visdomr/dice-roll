import random

print("=======================")
print("  DICE DASH TO 50  ")
print("=======================")
print("Roll wisely, aim for 50!")
print("Bust over 50, you’re out!")
print("=======================")


def player_turn(player_num, current_score, opponent_score, num_players):
    total = 0
    while True:
        print(f"Player {player_num}'s Turn")
        try:
            num_dice = int(input("How many dice do you want to roll? (0-4): "))
            if 0 <= num_dice <= 4:
                break
            print("Please enter a number between 0 and 4!")
        except ValueError:
            print("That’s not a number! Try again.")
    for i in range(num_dice):
        roll = random.randint(1, 6)
        total += roll
        print(roll)
    print("----")
    current_score += total
    print(f"Player {player_num} game total: ", current_score)

    if current_score == 50:
        print(f"Player {player_num} wins with exactly 50!")
        return current_score, True
    elif current_score > 50:
        if num_players == 2 and opponent_score <= 50:
            print(
                f"Player {3 - player_num} wins—Player {player_num} busted with", current_score)
            return current_score, True
        elif num_players == 2:
            print("Both players busted! No winner.")
            return current_score, True
        else:
            print(f"Player {player_num} busted! No winner against computer.")
            return current_score, True
    return current_score, False


# Main game functionality
num_players = int(input("How many players? (1-2): "))
if num_players == 2:
    print("Welcome both players!")
elif num_players == 1:
    print("Welcome player! Good luck against the computer!")
else:
    print("Invalid input, try again!")

player1_score = 0
player2_score = 0

round = 0
while round < 6:
    # Player 1's turn
    player1_score, end_game = player_turn(
        1, player1_score, player2_score, num_players)
    if end_game:
        break

    # Player 2's turn (if 2 players)
    if num_players == 2:
        player2_score, end_game = player_turn(
            2, player2_score, player1_score, num_players)
        if end_game:
            break

    round += 1

print("Player 1 score:", player1_score)
print("Player 2 score:", player2_score)

while True:
    play_again = input("Play again? (yes/no): ").lower()
    if play_again in ["yes", "no"]:
        break
        print("Please enter 'yes' or 'no'!")
    if play_again == "no":
        print("Thanks for playing!")
    break
