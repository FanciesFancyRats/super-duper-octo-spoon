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
hit = 0
numberCorrect = 0
alphabet = "abcdefghijklmnopqrstuvwxyz"
helper = []
for i in range(len(alphabet)):
    helper.append(alphabet[i])
print(len(helper))
print word
for i in range(length):
    letters.append(word[i])
for i in range(length):
    guessList.append("_")
while((attemptNumber < 6) and (win == 0)):
    hit = 0
    numberCorrect = 0
    print("Here are your remaining letter: ")
    print(helper)
    print(guessList)
    guess = raw_input("Please input a letter: ")
    for i in range(length):
        if guess == letters[i]:
            hit = 1
            guessList[i] = guess
    for i in range(len(helper)):
        if guess == helper[i]:
            remove = i
    del helper[remove]
    for i in range(length):
        if guessList[i] == letters[i]:
            numberCorrect = numberCorrect + 1
    if hit == 1:
        print("Correct ") ,
        print(guess) ,
        print("is in the word")
    if hit == 0:
        print("Incorrect ") ,
        print(guess) ,
        print("is not in the word")
        attemptNumber = attemptNumber + 1
    if (numberCorrect == length):
        win = 1
        print("You've won")
print(word)




# your code begins here!
