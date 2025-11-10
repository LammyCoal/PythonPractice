import random

names = ['lammy', 'lukmon', 'olamiji', 'eniola']

word = random.choice(names)
chosen_word = ['_'] * len(word)

tries = 10

while tries > 0:
    print('\nCurrent word: ' + ' '.join(chosen_word))

    guess = input('Guess a letter: ').lower()

    if guess in word:
        for letters in range(len(word)):
            if word[letters] == guess:
                chosen_word[letters] = guess
        print('Great Guess!')
    else:
        tries -= 1
        print(f"Wrong Guess! Attempt left:  + {tries}")

    if "_" not in chosen_word:
        print(f"Congratulations! You guessed the word: {word}")
        break

if "_" in chosen_word and tries == 0:
    print(f"You've finished your attempt, the word was: {word}")
