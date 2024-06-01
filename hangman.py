import os

wordList = [
    'dolphin',
    'mystery',
    'galaxy',
    'puzzle',
    'jungle',
    'whisper',
    'knight',
    'harmony',
    'voyage',
    'lantern',
]

outputList = []

wordToGuess = wordList[1]

for x in wordToGuess:
    outputList.append('_')

while '_' in outputList:
    os.system('clear')
    print('Guess the letters in this word!')
    print("You can type \"exit\" to exit the game at any time.")
    print(*outputList)
    chosenLetter = input('Please enter a letter: ')
    chosenLetter = chosenLetter.lower()
    if chosenLetter == "exit": break
    if chosenLetter in wordToGuess:
        for i in range(len(wordToGuess)):
            if wordToGuess[i] == chosenLetter:
                outputList[i] = chosenLetter
    else:
        print('letter is not in word')

os.system('clear')
print(*outputList)
print('You win!')