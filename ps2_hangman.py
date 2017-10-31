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
word = (choose_word(wordlist))
length = len(word)
letters = []
guessList = []
win = 0
attemptNumber = 0
print word
for i in range(length):
    letters.append(word[i])
for i in range(length):
    guessList.append("_")
while((attemptNumber < 6) and (win == 0)):
    print(guessList)
    guess = raw_input("Please input a word: ")
    if (guess == word):
        win = 1
        print("Correct, you win")
    if (guess != word):
        attemptNumber = attemptNumber + 1
        if(len(guess) >= len(word)):
            for i in range(length):
                if guess[i] == letters[i]:
                    guessList[i] = letters[i]
        if(len(word)>len(guess)):
            print(len(word)) ,
            print">" ,
            print(len(guess))
            for i in range(len(guess)):
                print i
                if guess[i] == letters[i]:
                    guessList[i] = letters[i]
        print("Try again: ")
