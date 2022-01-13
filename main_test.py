import unittest
from unittest.case import TestCase

from main import contains_tried_letter, green_match, orange_match


class TestMain(unittest.TestCase):
    def test_green_match(self):

        true_cases = {
            ("green", "GR__N"),
        }
        for t in true_cases:
            word, inp = t
            self.assertTrue(green_match(word, inp))

        false_cases = {("green", "GR__P")}
        for t in false_cases:
            word, inp = t
            self.assertFalse(green_match(word, inp))

    def test_orange_match(self):

        true_cases = {
            ("green", "r___e"),
            ("green", "r_E_e"),
        }
        for t in true_cases:
            word, inp = t
            self.assertTrue(orange_match(word, inp))

        false_cases = {("green", "t___e"), ("green", "g___e")}
        for t in false_cases:
            word, inp = t
            self.assertFalse(orange_match(word, inp))

    def test_contains_tried_letters(self):
        invalid_letters = set(["s"])
        true_cases = ["aides"]
        for t in true_cases:
            self.assertTrue(contains_tried_letter(t, invalid_letters))

        false_cases = ["anted"]
        for t in false_cases:
            self.assertFalse(contains_tried_letter(t, invalid_letters))


if __name__ == "__main__":
    unittest.main()
