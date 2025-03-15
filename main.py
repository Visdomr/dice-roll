import random


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
    total = 0
    num_dice = int(input("How many dice do you want to roll? (0-4): "))
    for i in range(num_dice):
        roll = random.randint(1, 6)
        total += roll
        print(roll)
    print("----")
    print("Total: ", total)
    player1_score += total
    round += 1
print("Player 1 score:", player1_score)
