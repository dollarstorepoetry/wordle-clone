from words import EnglishWords


def wordle(word):
    guess = ""
    num_guesses = 7
    # print initial setup
    for _ in enumerate(word):
        print("_", end=" ")
    print()
    while num_guesses > 0 and guess != word:
        guess = input(f"Num guesses: {num_guesses}\nEnter word: \n").lower()
        if len(guess) == len(word):
            print(hint(guess, word))
        else:
            print("no " + f"(There are ({num_guesses}) letters)")
            continue
        num_guesses -= 1
    print(f"WORD: {word}")


def hint(guess, word):
    o = ''
    used_letters = []  # so it doesn't show repeats mistakenly
    for i, l in enumerate(guess):
        if guess[i] == word[i]:
            o += guess[i].upper()
            used_letters.append(guess[i])

        elif guess[i] in word and guess[i] not in used_letters:
            # if in the word but not at the right spot
            o += "*"
            used_letters.append(guess[i])

        else:
            o += "_"
    return o


def main():
    d = EnglishWords()
    wl = -1
    while not 3 < wl < 30:
        wl = int(input("How many letters would u like"))
        if not 3 < wl < 30:
            print("yo word too long fool")
    wordle(d.get_random_word(word_length=wl))
    _ = input('input anything to terminate')


if __name__ == '__main__':
    main()
