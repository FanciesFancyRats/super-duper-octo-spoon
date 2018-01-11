# 6.00 Problem Set 3
# 
# Hangman
#


# -----------------------------------
# Helper code
# (you don't need to understand this helper code)
import random
import string

WORDLIST_FILENAME = "words.txt"

def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = string.split(line)
    print "  ", len(wordlist), "words loaded."
    return wordlist

def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# actually load the dictionary of words and point to it with 
# the wordlist variable so that it can be accessed from anywhere
# in the program
wordlist = load_words()

# your code begins here!
word = choose_word(wordlist)
word = word.lower()
alphabet = "abcdefghijklmnopqrstuvwxyz"
def hangman(word):
    lettersGuessed = 0
    print "Welcome to the game, Hangman!"
    print "I man thinking of a word that is ", len(word), "letters long."
    #creating blank spaces
    guessed = list()
    for i in range (len(word)):
            guessed.append("_")
    #creating available letters
    helper = list()
    for x in range (len(alphabet)):
        helper.append(alphabet[x])
    guesses = 8
    win = False
    while (guesses > 0) and (not win):
        correct = False
        print "----------------------------------------------------------------------------"
        #For good grammer
        if guesses > 1:
            print "You have ", guesses, "guesses left."
        else:
            print "You have ", guesses, "guess left."
        print "Avaliable letters: ",
        for j in range (len(helper)):
            print helper[j],
        print " "
        guess = raw_input('Please enter a letter: ')
        if len(guess) > 1:
            guess = guess[0]
       #check if character is in string
        for i in range (len(word)):
            if word[i] == guess[0] and guess in helper:
               correct = True
               guessed[i] = guess[0]
               lettersGuessed += 1
        #TO-DO, figure out how to get rid of specific item in list
        if guess in helper:
            helper.remove(guess)
        if lettersGuessed < len(word):
            if correct:
                print "Correct!"
                print guessed 
            if not correct:
                print "Incorrect"
                guesses -= 1
                print guessed
        else:
            print "You've won!"
            print guessed
            break
    print word

hangman(word)
