import random
import time

print("🎲 Welcome to Simple Ludo Game 🎲")
print("----------------------------------")

player1_pos = 0
player2_pos = 0

target = 30

while True:
    # Player 1 Turn
    input("\nPlayer 1 Press Enter to roll dice...")
    dice = random.randint(1, 6)
    print("Player 1 rolled:", dice)

    if player1_pos == 0 and dice == 6:
        player1_pos = 1
        print("Player 1 started!")
    elif player1_pos > 0:
        player1_pos += dice

    print("Player 1 position:", player1_pos)

    if player1_pos >= target:
        print("\n🎉 Player 1 Wins! 🎉")
        break


    time.sleep(1)

    # Player 2 Turn
    input("\nPlayer 2 Press Enter to roll dice...")
    dice = random.randint(1, 6)
    print("Player 2 rolled:", dice)

    if player2_pos == 0 and dice == 6:
        player2_pos = 1
        print("Player 2 started!")
    elif player2_pos > 0:
        player2_pos += dice

    print("Player 2 position:", player2_pos)

    if player2_pos >= target:
        print("\n🎉 Player 2 Wins! 🎉")
        break

    time.sleep(1)
