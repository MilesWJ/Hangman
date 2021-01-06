import random

with open("wordlist.txt", "r") as file:
    words = file.readlines()

word = random.choice(words)[:-1]

allowed_errors = 7
guesses = []
done = False

while not done:
    for everyLetter in word:
        if everyLetter.lower() in guesses:
            print(everyLetter, end=" ")
        else:
            print("_", end=" ")
    print("")

    guess = input(f"Allowed Errors Left: {allowed_errors}, Next Guess:")
    guesses.append(guess.lower())
    if guess.lower() not in word.lower():
        allowed_errors -=1
        if allowed_errors == 0:
            break
    
    done = True
    for letter in word:
        if letter.lower() not in guesses:
            done = False

if done:
    print(f"You found the word! It was {word}.")
else:
    print(f"Game over! The word was {word}.")
