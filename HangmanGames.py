import random

gameWords = ["apple", "school", "garden", "python", "window"]
secretWord = random.choice(gameWords)
lettersUsed = []
life = 6
print("== Hangman Game ==")

while life != 0:

    showWord = ""
    allFound = True

    for ch in secretWord:
        if ch in lettersUsed:
            showWord = showWord + ch + " "
        else:
            showWord = showWord + "_ "
            allFound = False

    print("\nCurrent Word:", showWord)

    if allFound:
        print("\nYou guessed the word.")
        break

    userLetter = input("Type one letter: ").lower()

    if len(userLetter) > 1:
        print("Only one letter at a time.")
        continue

    if userLetter in lettersUsed:
        print("Already entered.")
        continue

    lettersUsed.append(userLetter)

    if userLetter in secretWord:
        print("Good Guess")
    else:
        print("Not in the word.")
        life = life - 1
        print("Lives Left:", life)

if life == 0:
    print("\nYou Lost")
    print("Correct Word was:", secretWord)