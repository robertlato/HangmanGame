# Hangman game

import random

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    Be sure to have words.txt file in the same folder as this file.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

# Load the list of words into the variable wordlist
wordlist = loadWords()

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a random word from wordlist
    """
    return random.choice(wordlist)


def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    x = True
    for i in secretWord:
        if i not in lettersGuessed:
            x = False
    return(x)



def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    y = ''
    for i in secretWord:
        if i in lettersGuessed:
            y += i
        else:
            y += '_ '
    return(y)



def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    import string
    AvailableLetters = ''
    for letter in string.ascii_lowercase:
        if letter not in lettersGuessed:
            AvailableLetters += letter
    return(AvailableLetters)
    

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.
    Starts up an interactive game of Hangman.

    '''
    guessLeft = 8
#    secretWord = chooseWord(wordlist)
    lettersGuessed = []
    print('Welcome to the game, Hangman! To exit type "exit game"')
    print('I am thinking of a word that is', len(secretWord), 'letters long')
    while guessLeft >= 1 and '_' in getGuessedWord(secretWord, lettersGuessed):
        print('-------------')
        print('You have', guessLeft, 'guesses left.')
        print('Available Letters: ', getAvailableLetters(lettersGuessed))
        guess = input('Please guess a letter: ')
        lowerguess = guess.lower()
        if lowerguess == 'exit game':
            break
        if lowerguess in lettersGuessed:
            print("Oops! You've already guessed that letter: ", getGuessedWord(secretWord, lettersGuessed))
        elif lowerguess in secretWord:
            lettersGuessed += lowerguess
            print('Good guess: ', getGuessedWord(secretWord, lettersGuessed))
        else: 
            lettersGuessed += lowerguess
            print('Oops! That letter is not in my word: ', getGuessedWord(secretWord, lettersGuessed))
            guessLeft -= 1
    if guessLeft == 0:
        print('-------------')
        print('Sorry, you ran out of guesses. The word was:', secretWord)
    elif lowerguess == 'exit game':
        print('Exiting the game..')
    else: 
        print('-------------')
        print('Congratulations, you won!')
        

#initializing the hangman hame with random choosen word
secretWord = chooseWord(wordlist).lower()
hangman(secretWord)
