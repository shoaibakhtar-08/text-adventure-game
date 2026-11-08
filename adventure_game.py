import random

# Game settings
DEFAULT_HEALTH = 100
MIN_DAMAGE = 10
MAX_DAMAGE = 40
KEY_SCORE = 20
TREASURE_SCORE = 50

# Menu options
CAVE = 1
RIVER = 2
QUIT = 3


def get_damage(fixed_damage=None):
    """Return random monster damage, or a fixed value for repeatable tests."""
    if fixed_damage is not None:
        return fixed_damage
    return random.randint(MIN_DAMAGE, MAX_DAMAGE)


def show_status(score, health):
    """Print the player's current score and health."""
    print(f"Score: {score} | Health: {health}")


def forest():
    """Show the menu and keep asking until the player enters a valid choice."""
    print("\nYou are in the Forest. Where do you want to go?")
    print("1. Cave")
    print("2. River")
    print("3. Quit")

    while True:
        try:
            choice = input("Choice: ").strip()
        except EOFError:
            return QUIT

        if choice in ("1", "2", "3"):
            return int(choice)
        print("Invalid choice. Enter 1, 2 or 3.")


def cave(score, health, fixed_damage=None):
    """Apply the Cave attack and reward a key if the player survives."""
    damage = get_damage(fixed_damage)
    health = max(0, health - damage)
    print(f"Monster attacks! Damage: {damage}. Health: {health}")

    if health > 0:
        score += KEY_SCORE
        print(f"You found a key! Score: {score}")
    return score, health


def river(score, health):
    """Give the player the River treasure."""
    score += TREASURE_SCORE
    print("You found a treasure!")
    show_status(score, health)
    return score, health


def play(health=DEFAULT_HEALTH, fixed_damage=None):
    """Run the game until the player quits or loses all health."""
    score = 0

    print("=" * 40)
    print("       TEXT-BASED ADVENTURE GAME")
    print("=" * 40)
    print(f"You start in the Forest. Health: {health} | Score: {score}")

    while health > 0:
        choice = forest()

        if choice == CAVE:
            score, health = cave(score, health, fixed_damage)
        elif choice == RIVER:
            score, health = river(score, health)
        else:
            print(f"You left the adventure. Final score: {score} | Health: {health}")
            return score, health

    print(f"Game Over! Final score: {score}")
    return score, health


def main():
    """Start the game and handle Ctrl+C cleanly."""
    try:
        play()
    except KeyboardInterrupt:
        print("\nYou left the adventure.")


if __name__ == "__main__":
    main()
