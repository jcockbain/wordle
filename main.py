def find(s, ch):
    return [i for i, ltr in enumerate(s) if ltr == ch]

def main():
    with open("words.txt") as f:
        word_dict = [line.rstrip('\n') for line in f]
    word_dict.sort()
    inp = input("What is your input?\n")
    if len(inp) != 5:
        raise Exception("Need input to be length 5!")

    possible_words = []
    blanks = find(inp, "_")
    
    for w in word_dict:
        possible = True
        
        # check for exact matches (Green case)
        for i, c in enumerate(inp):
            word_char = w[i]
            if c != "_" and c.isupper():
                if word_char != c.lower():
                    possible = False
                    break
        if not possible:
            break

        # check for letter matches (Orange case)
        for i, c in enumerate(inp):
            word_char = w[i]
            rem_letters = [w[b] for b in blanks]
            if c != "_" and c.islower():
                if not(c in rem_letters and c != word_char):
                    possible = False
                    break
        
        if possible:
            possible_words.append(w)

    print(f"There {len(possible_words)} possible word(s)")   
    print(possible_words)

if __name__ == "__main__":
    main()