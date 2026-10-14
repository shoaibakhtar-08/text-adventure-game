"""
Automated tests for the Text-Based Adventure Game (PS No. 39).

Test Cases 1-4 mirror the four cases given in the problem statement.
The remaining tests check extra edge cases.

Run from the project root:
    python -m unittest discover -s tests -v
"""

import io
import os
import sys
import unittest
from contextlib import redirect_stdout
from unittest.mock import patch

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import adventure_game as game  # noqa: E402


def run_game(inputs, health=game.DEFAULT_HEALTH, damage=None):
    """Play a game with scripted inputs; return (score, health, output_text)."""
    buffer = io.StringIO()
    with patch("builtins.input", side_effect=inputs), redirect_stdout(buffer):
        score, final_health = game.play(health, damage)
    return score, final_health, buffer.getvalue()


class ProblemStatementTestCases(unittest.TestCase):

    def test_case_1_normal_input(self):
        """Choice 2 (River) -> treasure, Score 50, Health 100."""
        score, health, out = run_game(["2", "3"])
        self.assertIn("You found a treasure!", out)
        self.assertIn("Score: 50 | Health: 100", out)
        self.assertEqual((score, health), (50, 100))

    def test_case_2_boundary_minimum_input(self):
        """Health 30, Cave, damage 30 -> Health 0, Game Over, score 0."""
        score, health, out = run_game(["1"], health=30, damage=30)
        self.assertIn("Monster attacks! Damage: 30. Health: 0", out)
        self.assertIn("Game Over! Final score: 0", out)
        self.assertNotIn("You found a key!", out)
        self.assertEqual((score, health), (0, 0))

    def test_case_3_invalid_input(self):
        """Choices '7' and 'abc' -> invalid messages, no health lost."""
        score, health, out = run_game(["7", "abc", "3"])
        self.assertEqual(out.count("Invalid choice. Enter 1, 2 or 3."), 2)
        self.assertEqual((score, health), (0, 100))

    def test_case_4_different_valid_scenario(self):
        """Cave, River, Quit with damage 30 -> final score 70, health 70."""
        score, health, out = run_game(["1", "2", "3"], damage=30)
        self.assertIn("Monster attacks! Damage: 30. Health: 70", out)
        self.assertIn("You found a key! Score: 20", out)
        self.assertIn("You found a treasure!", out)
        self.assertIn("Score: 70 | Health: 70", out)
        self.assertIn("You left the adventure. Final score: 70 | Health: 70", out)
        self.assertEqual((score, health), (70, 70))


class EdgeCaseTests(unittest.TestCase):

    def test_random_damage_always_in_range(self):
        for _ in range(1000):
            self.assertTrue(game.MIN_DAMAGE <= game.get_damage() <= game.MAX_DAMAGE)

    def test_fixed_damage_is_used(self):
        self.assertEqual(game.get_damage(30), 30)

    def test_health_never_negative(self):
        _, health, _ = run_game(["1"], health=30, damage=40)
        self.assertEqual(health, 0)

    def test_survive_exact_boundary(self):
        """Health 31 and damage 30 leaves Health 1, so the key is still found."""
        score, health, out = run_game(["1", "3"], health=31, damage=30)
        self.assertEqual((score, health), (20, 1))
        self.assertIn("You found a key!", out)

    def test_game_ends_when_health_reaches_zero_without_quit(self):
        """Loop must stop on Health 0; no further input is requested."""
        score, health, out = run_game(["1", "1", "1", "1"], damage=30)
        self.assertEqual(health, 0)
        self.assertIn("Game Over!", out)

    def test_score_kept_when_player_dies(self):
        score, health, out = run_game(["2", "1", "1", "1", "1"], damage=40)
        self.assertEqual(health, 0)
        self.assertEqual(score, 50 + 2 * 20)   # River, then 2 survived caves
        self.assertIn("Game Over! Final score: 90", out)

    def test_empty_and_symbol_input_are_invalid(self):
        _, health, out = run_game(["", " ", "0", "4", "-1", "1.5", "3"])
        self.assertEqual(out.count("Invalid choice. Enter 1, 2 or 3."), 6)
        self.assertEqual(health, 100)

    def test_input_with_spaces_is_accepted(self):
        score, _, _ = run_game([" 2 ", "3"])
        self.assertEqual(score, 50)

    def test_end_of_input_quits_cleanly(self):
        score, health, out = run_game([EOFError()])
        self.assertIn("You left the adventure.", out)
        self.assertEqual((score, health), (0, 100))

    def test_quit_immediately(self):
        score, health, out = run_game(["3"])
        self.assertIn("You left the adventure. Final score: 0 | Health: 100", out)

    def test_random_game_is_always_consistent(self):
        """Many random games: health stays within 0-100, score is a multiple of 10."""
        for _ in range(200):
            moves = ["1", "2"] * 20 + ["3"]
            score, health, _ = run_game(moves)
            self.assertTrue(0 <= health <= 100)
            self.assertEqual(score % 10, 0)


class CommandLineTests(unittest.TestCase):

    def test_defaults(self):
        args = game.parse_args([])
        self.assertEqual(args.health, 100)
        self.assertIsNone(args.damage)

    def test_testing_options(self):
        args = game.parse_args(["--health", "30", "--damage", "30"])
        self.assertEqual((args.health, args.damage), (30, 30))

    def test_invalid_health_rejected(self):
        with redirect_stdout(io.StringIO()), patch("sys.stderr", io.StringIO()):
            with self.assertRaises(SystemExit):
                game.parse_args(["--health", "0"])


if __name__ == "__main__":
    unittest.main()
