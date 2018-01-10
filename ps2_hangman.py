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
    print "Welcome to the game, Hangman!"
    print "I man thinking of a word that is ", len(word), "letters long."
    print word
    #creating blank spaces
    guessed = tuple()
    for i in range (len(word)):
            guessed = guessed + ("_",)
    #creating available letters
    helper = list()
    for x in range (len(alphabet)):
        helper.append(alphabet[x])
    guesses = 8
    win = False
    while (guesses > 0) and (not win):
        print "----------------------------------------------------------------------------"
        #For good grammer
        if guesses > 1:
            print "You have ", guesses, "guesses left."
        else:
            print "You have ", guesses, "guess left."
        print "Avaliable letters: ",
        for j in range (len(helper)):
            print helper[j],
        
        guesses -= 1
        print" "

hangman(word)
