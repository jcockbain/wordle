import unittest

from main import WordleHelper, green_match, orange_match


class TestMain(unittest.TestCase):
    def test_run_step(self):
        
        words = ["label", "cable", "table"]
        guess = "fable"
        result = "_ABle"
        wh = WordleHelper(words)
        wh.run_step(guess, result)
        self.assertEqual(["label"], wh.possible_words)

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


if __name__ == "__main__":
    unittest.main()
