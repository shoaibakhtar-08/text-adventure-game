"""
Text-Based Adventure Game  (PS No. 39)
Rungta International Skills University
School of Computer Science and Engineering
B.Tech CSE in association with IBM

The player starts in the Forest with Health 100 and Score 0 and chooses
where to go from a menu:

    1. Cave  - a monster attacks (random damage 10-40). If the player
               survives, a key is found (+20 score).
    2. River - a treasure is found (+50 score).
    3. Quit  - leave the adventure and show the final score.

The game ends when the player quits or Health reaches 0.

Concepts used: Conditions, Loops, Functions, Random.

Run:  python adventure_game.py
"""

import random

# ---------------- Game settings ----------------
STARTING_HEALTH = 100   # Test Case 2: change to 30
FIXED_DAMAGE = None     # Test Cases 2 and 4: change to 30 (None = random damage)
MIN_DAMAGE = 10
MAX_DAMAGE = 40
KEY_POINTS = 20
TREASURE_POINTS = 50


def forest():
    """Show the menu and return a valid choice ("1", "2" or "3")."""
    print("\nYou are in the Forest. Where do you want to go?")
    print("1. Cave")
    print("2. River")
    print("3. Quit")

    while True:
        choice = input("Choice: ").strip()
        if choice in ("1", "2", "3"):
            return choice
        print("Invalid choice. Enter 1, 2 or 3.")


def cave(score, health):
    """Cave: the monster attacks; a key is found only if the player survives."""
    if FIXED_DAMAGE is None:
        damage = random.randint(MIN_DAMAGE, MAX_DAMAGE)
    else:
        damage = FIXED_DAMAGE

    health = max(0, health - damage)          # health never goes below 0
    print(f"Monster attacks! Damage: {damage}. Health: {health}")

    if health > 0:
        score += KEY_POINTS
        print(f"You found a key! Score: {score}")
    return score, health


def river(score, health):
    """River: a treasure gives +50 score."""
    score += TREASURE_POINTS
    print("You found a treasure!")
    print(f"Score: {score} | Health: {health}")
    return score, health


def play_game():
    """Run the game until the player quits or Health reaches 0."""
    health = STARTING_HEALTH
    score = 0

    print("TEXT-BASED ADVENTURE GAME")
    print(f"Starting health: {health} | Score: {score}")

    while health > 0:
        choice = forest()

        if choice == "1":
            score, health = cave(score, health)
        elif choice == "2":
            score, health = river(score, health)
        else:
            print(f"You left the adventure. Final score: {score} | Health: {health}")
            return score, health

    print(f"Game Over! Final score: {score}")
    return score, health


if __name__ == "__main__":
    play_game()
