from typing import List, Dict, Set
from collections import Counter
from functools import reduce


class WordleHelper:
    def __init__(self, words_list):
        self.tried_letters = set()
        self.invalid_letter_per_pos = {}
        self.possible_words = words_list

    def run(self):
        for step in range(0, 6):
            print(f"\n<--Step {step}-->")
            while 1:
                guess = input("\nWhat was your guess?\n\n")
                if is_valid_guess(guess):
                    break
                else:
                    print("Invalid guess, enter a lower case word of length 5")
            while 1:
                result = input("\nWhat was the result?\n\n")
                if is_valid_result(result):
                    break
                else:
                    print("Invalid guess, a word of length 5")

            for i, c in enumerate(result):
                if c == "_":
                    self.tried_letters.add(guess[i])

            # get all possible words
            self.possible_words = [
                w
                for w in self.possible_words
                if green_match(w, result)
                and orange_match(w, result)
                and not contains_tried_letter(w, self.tried_letters)
            ]

            if len(self.possible_words) == 0:
                raise Exception("No words left! :(")
            print(f"\nThere {len(self.possible_words)} possible word(s):\n")
            print(self.possible_words)

            # get the most popular letters in the possible words
            d = get_letter_counter(self.possible_words)
            for g in [x.lower() for x in result if x != "_"]:
                # correct for letters already in the guess
                if g in d:
                    d[g] -= len(self.possible_words)
            print(
                f"\n<--Count of Letters in Possible Words-->\n\n{sorted(d.items(), key=lambda x: x[1], reverse=True)}"
            )

            # rank the common words by frequency of the most common letters
            scores = get_word_scores_counter(self.possible_words, d)
            print(
                f"\n<--Weighted Score of Possible Words-->\n\n{sorted(scores.items(), key=lambda x: x[1], reverse=True)[:20]}"
            )
        print("Too many steps!")


def is_valid_guess(inp: str) -> bool:
    return len(inp) == 5 and all([c.islower() for c in inp])


def is_valid_result(inp: str) -> bool:
    return len(inp) == 5


# check for exact matches (Green case)
def green_match(word: str, inp: str) -> bool:
    return all([word[i] == c.lower() for i, c in enumerate(inp) if c.isupper()])


# check for right letter, wrong pos (Orange case)
def orange_match(word: str, inp: str) -> bool:
    # rem_letters equals all letters not yet picked
    rem_letters = [word[i] for i in range(0, 5) if not inp[i].isupper()]
    return all(
        [(c in rem_letters and c != word[i]) for i, c in enumerate(inp) if c.islower()]
    )


def contains_tried_letter(word: str, tried_letters: Set[str]) -> bool:
    return any([c in tried_letters for c in word])


def get_letter_counter(possible_words: List[str]) -> Dict[str, int]:
    return (
        reduce((lambda x, y: Counter(x) + Counter(y)), possible_words)
        if len(possible_words) > 1
        else Counter(possible_words[0])
    )


def get_word_scores_counter(
    possible_words: List[str], letter_counter: Dict[str, int]
) -> Dict[str, int]:
    scores = {}
    for w in possible_words:
        score, seen = 0, set()
        for c in w:
            # don't count duplicates (as these are less useful
            if c not in seen:
                score += letter_counter[c]
                seen.add(c)
        scores[w] = score
    return scores


def main():
    with open("words.txt") as f:
        words = [line.rstrip("\n") for line in f]
    words.sort()
    wh = WordleHelper(words)
    wh.run()


if __name__ == "__main__":
    main()
