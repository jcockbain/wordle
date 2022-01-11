from typing import List, Dict

# TODO: take as input
tried_letters = set()

# check for exact matches (Green case)
def green_match(word: str, inp: str) -> bool:
    for i, c in enumerate(inp):
        word_char = word[i]
        if c != "_" and c.isupper():
            if word_char != c.lower():
                return False
    return True

# check for right letter, wrong pos (Orange case)
def orange_match(word: str, inp: str) -> bool:
    blanks = [i for i, ltr in enumerate(inp) if ltr == '_']
    rem_letters = [word[b] for b in blanks]
    for i, c in enumerate(inp):
        word_char = word[i]
        if c != "_" and c.islower():
            if not(c in rem_letters and c != word_char):
                return False
    return True


def contains_tried_letter(word: str) -> bool:
    return any([c in tried_letters for c in word])


def get_letter_counter(possible_words: List[str])-> Dict[str, int]:
    d = {}
    for p in possible_words:
        for c in p:
            if c not in d:
                d[c] = 1
            else:
                d[c] += 1
    return d

def get_word_scores_counter(possible_words: List[str], letter_counter: Dict[str, int]) -> Dict[str, int]:
    scores = {}
    for w in possible_words:
        score, seen = 0, set()
        for c in w:
            # don't count duplicates
            if c not in seen:
                score += letter_counter[c]
                seen.add(c)
        scores[w] = score
    return scores


def main():
    with open("words.txt") as f:
        words = [line.rstrip('\n') for line in f]
    words.sort()
    inp = input("What is your input?\n\n")
    if len(inp) != 5:
        raise Exception("Need input to be length 5!")

    possible_words = []
    for w in words:
        if green_match(w, inp) and orange_match(w, inp) and not contains_tried_letter(w):
            possible_words.append(w)

    print(f"\nThere {len(possible_words)} possible word(s)\n")
    print(possible_words)

    d = get_letter_counter(possible_words)
    for g in [x.lower() for x in inp if x != "_"]:
        # correct for letters already in the guess
        if g in d:
            d[g] -= len(possible_words)

    print("\n<--Count of Letters in Possible Words-->\n")
    print(sorted(d.items(), key=lambda x: x[1], reverse=True))

    scores = get_word_scores_counter(possible_words, d)
    print("\n<--Weighted Score of Possible Words-->\n")
    print(sorted(scores.items(), key=lambda x: x[1], reverse=True)[:20])


if __name__ == "__main__":
    main()
