def find(s, ch):
    return [i for i, ltr in enumerate(s) if ltr == ch]

# TODO: take as input
tried = set(["a","e","s"])

# check for exact matches (Green case)
def green_match(word, inp):
    for i, c in enumerate(inp):
        word_char = word[i]
        if c != "_" and c.isupper():
            if word_char != c.lower():
                return False
    return True

# check for right letter, wrong pos (Orange case)
def orange_match(word, inp):
    blanks = find(inp, "_")
    rem_letters = [word[b] for b in blanks]
    for i, c in enumerate(inp):
        word_char = word[i]
        if c != "_" and c.islower():
            if not(c in rem_letters and c != word_char):
                return False
    return True

def contains_tried_letter(word):
    return any([c in tried for c in word])

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
        
    print(f"There {len(possible_words)} possible word(s)\n")   
    print(possible_words)

    guessed = [x.lower() for x in inp if x != "_"]
    d = {}
    for p in possible_words:
        for c in p:
            if c not in d:
                d[c] = 1
            else:
                d[c] += 1

    for g in guessed:
        # correct for letters already in the guess
        if g in d:
            d[g] -= len(possible_words)
 
    print("\n<--Count of Letters in Possible Words-->\n")
    sort_orders = sorted(d.items(), key=lambda x: x[1], reverse=True)
    print(sort_orders)

    scores = {}
    for w in possible_words:
        score = 0
        seen = set()
        for c in w:
            # don't count duplicates
            if c not in seen:
                score += d[c]
                seen.add(c)
        scores[w] = score
    
    print("\n<--Weighted Score of Possible Words-->\n")
    sort_scores = sorted(scores.items(), key=lambda x: x[1], reverse=True)
    print(sort_scores[:20])


if __name__ == "__main__":
    main()