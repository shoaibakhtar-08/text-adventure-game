# Text-Based Adventure Game

**PS No. 39** | Semester 1 Project  
Rungta International Skills University, School of Computer Science and Engineering  
B.Tech Computer Science and Engineering in association with **IBM**

A console adventure game written in Python. The player starts in a forest and chooses to enter a cave, visit a river, or quit. The game uses health, score, random monster damage, and a menu that checks for valid input.

## Problem Statement

Create a text-based adventure game where the player explores a forest, cave, and river through menu choices. The cave has a monster attack, the river has treasure, and the game ends when the player quits or health reaches zero.

## Game Rules

| Choice | Place | Result |
|:---:|---|---|
| 1 | Cave | Monster damage is randomly selected from 10 to 40. If the player survives, they find a key worth 20 points. |
| 2 | River | Find treasure worth 50 points. Health does not change. |
| 3 | Quit | End the game and show the final score and health. |

The player starts with 100 health and 0 score. Invalid choices are rejected without changing health or score. Health never drops below zero.

## Requirements and How to Run

- Python 3.8 or newer
- No third-party packages; the game uses Python's built-in `random` module

```bash
python adventure_game.py
```

On some systems, use `python3` instead of `python`.

For a predictable test scenario, call the game function with a starting health and fixed damage value:

```python
from adventure_game import play_game

play_game(starting_health=30, fixed_damage=30)
```

## Project Structure

```text
text-adventure-game/
├── adventure_game.py
├── tests/
│   └── test_adventure_game.py
├── docs/
│   ├── Project_Report.docx
│   ├── Project_Synopsis.pdf
│   ├── Text_Adventure_Game_Project_Presentation.pptx
│   ├── flowchart.dot
│   ├── flowchart.png
│   └── sample_runs.md
├── .github/workflows/tests.yml
├── .gitignore
├── LICENSE
└── README.md
```

## Program Design

The game is divided into four functions:

| Function | Purpose |
|---|---|
| `show_menu()` | Displays the choices, checks the input, and returns a valid choice. |
| `cave(score, health, fixed_damage=None)` | Applies random monster damage (or fixed damage in examples), awards key points if the player survives, and returns the updated score and health. |
| `river(score, health)` | Awards treasure points and returns the updated score and health. |
| `play_game(starting_health=100, fixed_damage=None)` | Runs the main loop, updates score and health, and returns the final values. |

The program begins at the `if __name__ == "__main__"` section. When the file is run directly, it calls `play_game()` with the default settings.

### Flowchart

The program starts with health 100 and score 0. While health is above zero, it shows the forest menu, validates the choice, applies the Cave or River outcome, and repeats. Choosing Quit or reaching zero health ends the game.

## Testing

The test file uses Python's `unittest` library. It covers the four main cases and additional checks for random damage, location functions, health boundaries, score, input validation, and return values.

Run the tests from the project folder:

```bash
python -m unittest discover -s tests -v
```

GitHub Actions is configured to run the test suite for Python 3.9 through 3.12 on pushes and pull requests.

### Main Test Cases

| # | Scenario | Expected result |
|---:|---|---|
| 1 | Choose River, then Quit | Score 50; health 100. |
| 2 | Start with 30 health; enter Cave with fixed damage 30 | Health 0; Game Over; no key reward. |
| 3 | Enter 7 and abc, then Quit | Each invalid choice is rejected; health and score stay the same. |
| 4 | Enter Cave with fixed damage 30, then River, then Quit | Final score 70; health 70. |

## Sample Runs

See [docs/sample_runs.md](docs/sample_runs.md) for the console output for these cases.

## Concepts Demonstrated

- Variables and constants
- Functions
- `if` / `elif` / `else` conditions
- `while` loops
- Input validation
- Random numbers with the standard-library `random` module
- Basic unit testing with `unittest`

## Possible Improvements

- Add an inventory and healing items
- Add difficulty levels
- Save a high-score table
- Add colored output or a graphical interface

## Author

**Shoaib Akhtar**  
B.Tech CSE (AI/ML), Rungta International Skills University

Licensed under the [MIT License](LICENSE).

