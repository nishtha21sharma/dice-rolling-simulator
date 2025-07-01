import random

def roll_dice():
    input("🎲 Press Enter to roll the dice...")
    print("You rolled a", random.randint(1, 6))

while True:
    roll_dice()
    again = input("Roll again? (y/n): ")
    if again.lower() != 'y':
        break
