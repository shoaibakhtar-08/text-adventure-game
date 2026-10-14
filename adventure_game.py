import argparse
import random

# ----------------------------------------------------------------------
# Game settings (constants)
# ----------------------------------------------------------------------
DEFAULT_HEALTH = 100   # starting health of the player
MIN_DAMAGE = 10        # lowest possible monster damage
MAX_DAMAGE = 40        # highest possible monster damage
KEY_SCORE = 20         # score earned for finding the key in the cave
TREASURE_SCORE = 50    # score earned for finding the treasure at the river

# Menu options
CAVE = 1
RIVER = 2
QUIT = 3


# ----------------------------------------------------------------------
# Helper functions
# ----------------------------------------------------------------------
def get_damage(fixed_damage=None):
    """Return the monster's damage.

    A random value between MIN_DAMAGE and MAX_DAMAGE is returned, unless
    `fixed_damage` is given (used to make test cases repeatable).
    """
    if fixed_damage is not None:
        return fixed_damage
    return random.randint(MIN_DAMAGE, MAX_DAMAGE)


def show_status(score, health):
    """Print the player's current score and health."""
    print(f"Score: {score} | Health: {health}")


# ----------------------------------------------------------------------
# The three places of the game
# ----------------------------------------------------------------------
def forest():
    """Show the Forest menu and return a validated choice (1, 2 or 3).

    The player is asked again until a valid option is entered, so invalid
    input never affects health or score. If the input stream ends
    (Ctrl+D / Ctrl+Z), the game treats it as Quit.
    """
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
    """Cave: a monster attacks; if the player survives, a key gives +20.

    Returns the updated (score, health).
    """
    damage = get_damage(fixed_damage)
    health = max(0, health - damage)          # health never goes below 0
    print(f"Monster attacks! Damage: {damage}. Health: {health}")

    if health > 0:                            # survived the attack
        score += KEY_SCORE
        print(f"You found a key! Score: {score}")
    return score, health


def river(score, health):
    """River: a treasure gives +50 score.

    Returns the updated (score, health).
    """
    score += TREASURE_SCORE
    print("You found a treasure!")
    show_status(score, health)
    return score, health


# ----------------------------------------------------------------------
# Main game loop
# ----------------------------------------------------------------------
def play(health=DEFAULT_HEALTH, fixed_damage=None):
    """Run one full game and return the final (score, health)."""
    score = 0

    print("=" * 40)
    print("       TEXT-BASED ADVENTURE GAME")
    print("=" * 40)
    print(f"You start in the Forest. Health: {health} | Score: {score}")

    while health > 0:                         # runs until quit or Health == 0
        choice = forest()

        if choice == CAVE:
            score, health = cave(score, health, fixed_damage)
        elif choice == RIVER:
            score, health = river(score, health)
        else:                                 # QUIT
            print(f"You left the adventure. Final score: {score} | Health: {health}")
            return score, health

    print(f"Game Over! Final score: {score}")
    return score, health


# ----------------------------------------------------------------------
# Command-line interface
# ----------------------------------------------------------------------
def positive_int(text):
    """argparse type: an integer greater than 0."""
    value = int(text)
    if value <= 0:
        raise argparse.ArgumentTypeError("must be a positive whole number")
    return value


def non_negative_int(text):
    """argparse type: an integer greater than or equal to 0."""
    value = int(text)
    if value < 0:
        raise argparse.ArgumentTypeError("must be 0 or more")
    return value


def parse_args(argv=None):
    parser = argparse.ArgumentParser(
        description="Text-Based Adventure Game - explore the forest, cave and river."
    )
    parser.add_argument(
        "--health", type=positive_int, default=DEFAULT_HEALTH,
        help=f"starting health (default: {DEFAULT_HEALTH}); use 30 for Test Case 2",
    )
    parser.add_argument(
        "--damage", type=non_negative_int, default=None,
        help="fix the monster damage instead of random 10-40; use 30 for Test Cases 2 and 4",
    )
    return parser.parse_args(argv)


def main(argv=None):
    args = parse_args(argv)
    try:
        play(args.health, args.damage)
    except KeyboardInterrupt:                 # Ctrl+C
        print("\nYou left the adventure.")


if __name__ == "__main__":
    main()
