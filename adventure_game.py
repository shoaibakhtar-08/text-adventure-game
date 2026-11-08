import random

# Game settings
STARTING_HEALTH = 100
MIN_DAMAGE = 10
MAX_DAMAGE = 40
KEY_POINTS = 20
TREASURE_POINTS = 50


def show_menu():
    """Show the Forest menu and return a valid choice."""
    print("\nYou are in the Forest. Where do you want to go?")
    print("1. Cave")
    print("2. River")
    print("3. Quit")

    while True:
        choice = input("Choice: ").strip()
        if choice in ("1", "2", "3"):
            return choice
        print("Invalid choice. Enter 1, 2 or 3.")


def cave(score, health, fixed_damage=None):
    """Apply the Cave event and return the updated score and health."""
    if fixed_damage is None:
        damage = random.randint(MIN_DAMAGE, MAX_DAMAGE)
    else:
        damage = fixed_damage

    health = max(0, health - damage)
    print(f"Monster attacks! Damage: {damage}. Health: {health}")

    if health > 0:
        score += KEY_POINTS
        print(f"You found a key! Score: {score}")

    return score, health


def river(score, health):
    """Apply the River event and return the updated score and health."""
    score += TREASURE_POINTS
    print("You found a treasure!")
    print(f"Score: {score} | Health: {health}")
    return score, health


def play_game(starting_health=STARTING_HEALTH, fixed_damage=None):
    """Run the game and return the final score and health."""
    health = starting_health
    score = 0

    print("=" * 40)
    print("       TEXT-BASED ADVENTURE GAME")
    print("=" * 40)
    print(f"You start in the Forest. Health: {health} | Score: {score}")

    while health > 0:
        choice = show_menu()

        if choice == "1":
            score, health = cave(score, health, fixed_damage)
        elif choice == "2":
            score, health = river(score, health)
        else:
            print(
                f"You left the adventure. Final score: {score} | Health: {health}"
            )
            return score, health

    print(f"Game Over! Final score: {score}")
    return score, health


if __name__ == "__main__":
    play_game()
