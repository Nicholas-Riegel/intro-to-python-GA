import os
import random

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

def gameLoop():

    outputList = []
    wordToGuess = random.choice(wordList)

    for x in wordToGuess:
        outputList.append('_')

    triesLeft = 6
    wrongAnswerMessage = "Wrong answers:"
    exit = False

    while '_' in outputList and triesLeft > 0:

        os.system('clear')
        print('Guess the letters in this word!')
        print("You can type \"exit\" to exit the game at any time.")
        print("Tries left: " + str(triesLeft))
        print(*outputList)
        print(wrongAnswerMessage)

        chosenLetter = input('Please enter a letter: ')
        chosenLetter = chosenLetter.lower()
        
        if chosenLetter == "exit": 
            exit = True
            break
        if chosenLetter in wordToGuess:
            for i in range(len(wordToGuess)):
                if wordToGuess[i] == chosenLetter:
                    outputList[i] = chosenLetter
        else:
            triesLeft -= 1
            wrongAnswerMessage += " " + chosenLetter
    
    os.system('clear')
    
    if exit == False:
        print('Guess the letters in this word!')
        print("Tries left: " + str(triesLeft))
        print(*outputList)
        if triesLeft == 0 and "_" in outputList:
            print("Sorry. You're out of turns. You lose!")
        else:
            print('You win!')
        playAgain = input('Would you like to play again? Enter "yes" or "no". ')
        if playAgain == "yes":
            gameLoop()
        else:
            print("Have a nice day!")
    else:
        print("Goodbye!")

# run game
gameLoop()
