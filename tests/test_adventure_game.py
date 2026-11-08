"""Tests for the Text-Based Adventure Game."""

import io
import os
import sys
import unittest
from contextlib import redirect_stdout
from unittest.mock import patch

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import adventure_game as game  # noqa: E402


def run_game(inputs, health=game.STARTING_HEALTH, damage=None):
    """Run a game with scripted input and return its result and output."""
    output = io.StringIO()
    with patch("builtins.input", side_effect=inputs), redirect_stdout(output):
        score, final_health = game.play_game(health, damage)
    return score, final_health, output.getvalue()


class ProblemStatementTestCases(unittest.TestCase):
    def test_case_1_normal_input(self):
        score, health, output = run_game(["2", "3"])
        self.assertIn("You found a treasure!", output)
        self.assertIn("Score: 50 | Health: 100", output)
        self.assertEqual((score, health), (50, 100))

    def test_case_2_boundary_input(self):
        score, health, output = run_game(["1"], health=30, damage=30)
        self.assertIn("Monster attacks! Damage: 30. Health: 0", output)
        self.assertIn("Game Over! Final score: 0", output)
        self.assertNotIn("You found a key!", output)
        self.assertEqual((score, health), (0, 0))

    def test_case_3_invalid_input(self):
        score, health, output = run_game(["7", "abc", "3"])
        self.assertEqual(output.count("Invalid choice. Enter 1, 2 or 3."), 2)
        self.assertEqual((score, health), (0, 100))

    def test_case_4_mixed_choices(self):
        score, health, output = run_game(["1", "2", "3"], damage=30)
        self.assertIn("You found a key! Score: 20", output)
        self.assertIn("Score: 70 | Health: 70", output)
        self.assertEqual((score, health), (70, 70))


class EdgeCaseTests(unittest.TestCase):
    def test_random_damage_is_in_range(self):
        with patch("adventure_game.random.randint", return_value=25) as randint:
            score, health, output = run_game(["1", "3"])
        randint.assert_called_once_with(game.MIN_DAMAGE, game.MAX_DAMAGE)
        self.assertEqual((score, health), (20, 75))
        self.assertIn("Damage: 25", output)

    def test_fixed_damage_is_used(self):
        self.assertEqual(game.cave(0, 100, 30), (20, 70))

    def test_river_function_adds_treasure_points(self):
        self.assertEqual(game.river(10, 70), (60, 70))

    def test_health_never_goes_below_zero(self):
        _, health, _ = run_game(["1"], health=30, damage=40)
        self.assertEqual(health, 0)

    def test_surviving_with_one_health_gets_key(self):
        score, health, output = run_game(["1", "3"], health=31, damage=30)
        self.assertEqual((score, health), (20, 1))
        self.assertIn("You found a key!", output)

    def test_game_stops_when_health_reaches_zero(self):
        score, health, output = run_game(["1", "1", "1"], damage=40)
        self.assertEqual(health, 0)
        self.assertIn("Game Over!", output)

    def test_score_is_kept_when_player_dies(self):
        score, health, output = run_game(["2", "1", "1", "1"], damage=40)
        self.assertEqual((score, health), (90, 0))
        self.assertIn("Game Over! Final score: 90", output)

    def test_empty_and_symbol_inputs_are_invalid(self):
        _, health, output = run_game(["", " ", "0", "4", "-1", "1.5", "3"])
        self.assertEqual(output.count("Invalid choice. Enter 1, 2 or 3."), 6)
        self.assertEqual(health, 100)

    def test_spaces_around_choice_are_accepted(self):
        score, _, _ = run_game([" 2 ", "3"])
        self.assertEqual(score, 50)

    def test_quit_immediately(self):
        score, health, output = run_game(["3"])
        self.assertIn("You left the adventure.", output)
        self.assertEqual((score, health), (0, 100))

    def test_random_game_keeps_valid_state(self):
        for _ in range(100):
            moves = ["1", "2"] * 20 + ["3"]
            score, health, _ = run_game(moves)
            self.assertTrue(0 <= health <= 100)
            self.assertEqual(score % 10, 0)

    def test_custom_starting_health_is_used(self):
        _, health, _ = run_game(["3"], health=35)
        self.assertEqual(health, 35)


class FunctionResultTests(unittest.TestCase):
    def test_quit_returns_final_score_and_health(self):
        self.assertEqual(run_game(["3"])[:2], (0, 100))

    def test_river_does_not_change_health(self):
        score, health, _ = run_game(["2", "3"], health=65)
        self.assertEqual((score, health), (50, 65))

    def test_surviving_cave_adds_key_points(self):
        score, health, _ = run_game(["1", "3"], health=50, damage=10)
        self.assertEqual((score, health), (20, 40))


if __name__ == "__main__":
    unittest.main()

