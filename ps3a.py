# 6.00 Problem Set 3A Solutions
#
# The 6.00 Word Game
# Created by: Kevin Luu <luuk> and Jenna Wiens <jwiens>
#
#
class bcolors:
    BLUE = '\033[34m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    ENDC = '\033[0m'
import random
import string

VOWELS = 'aeiou'
CONSONANTS = 'bcdfghjklmnpqrstvwxyz'
HAND_SIZE = 5

SCRABBLE_LETTER_VALUES = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
}

# -----------------------------------
# Helper code
# (you don't need to understand this helper code)
# test

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
    # wordlist: list of strings
    wordlist = []
    for line in inFile:
        wordlist.append(line.strip().lower())
    print "  ", len(wordlist), "words loaded."
    return wordlist

def get_frequency_dict(sequence):
    """
    Returns a dictionary where the keys are elements of the sequence
    and the values are integer counts, for the number of times that
    an element is repeated in the sequence.

    sequence: string or list
    return: dictionary
    """
    # freqs: dictionary (element_type -> int)
    freq = {}
    for x in sequence:
        freq[x] = freq.get(x,0) + 1
    return freq
	

# (end of helper code)
# -----------------------------------

#
# Problem #1: Scoring a word
#
def get_word_score(word, n):
    """
    Returns the score for a word. Assumes the word is a
    valid word.

	The score for a word is the sum of the points for letters
	in the word multiplied by the length of the word, plus 50
	points if all n letters are used on the first go.

	Letters are scored as in Scrabble; A is worth 1, B is
	worth 3, C is worth 3, D is worth 2, E is worth 1, and so on.

    word: string (lowercase letters)
    returns: int >= 0
    """
    
    score = 0
    for i in range(len(word)):
        #print SCRABBLE_LETTER_VALUES[word[i]], word[i]
        score += SCRABBLE_LETTER_VALUES[word[i]]
        #print score
    score = score*len(word)
    if n == len(word):
        score += 50
    return score
# Make sure you understand how this function works and what it does!
#
def display_hand(hand):
    """
    Displays the letters currently in the hand.

    For example:
       display_hand({'a':1, 'x':2, 'l':3, 'e':1})
    Should print out something like:
       a x x l l l e
    The order of the letters is unimportant.

    hand: dictionary (string -> int)
    """
    for letter in hand.keys():
        for j in range(hand[letter]):
             print bcolors.BLUE ,  letter,              # print all on the same line
    print bcolors.ENDC                               # print an empty line

#
# Make sure you understand how this function works and what it does!
#
def deal_hand(n):
    """
    Returns a random hand containing n lowercase letters.
    At least n/3 the letters in the hand should be VOWELS.

    Hands are represented as dictionaries. The keys are
    letters and the values are the number of times the
    particular letter is repeated in that hand.

    n: int >= 0
    returns: dictionary (string -> int)
    """
    hand={}
    num_vowels = n / 3
    
    for i in range(num_vowels):
        x = VOWELS[random.randrange(0,len(VOWELS))]
        hand[x] = hand.get(x, 0) + 1
        
    for i in range(num_vowels, n):    
        x = CONSONANTS[random.randrange(0,len(CONSONANTS))]
        hand[x] = hand.get(x, 0) + 1
        
    return hand

#
# Problem #2: Update a hand by removing letters
#
def update_hand(hand, word):
    """
    Assumes that 'hand' has all the letters in word.
	In other words, this assumes that however many times
	a letter appears in 'word', 'hand' has at least as
	many of that letter in it. 

    Updates the hand: uses up the letters in the given word
    and returns the new hand, without those letters in it.

    Has no side effects: does not modify hand.

    word: string
    hand: dictionary (string -> int)    
    returns: dictionary (string -> int)
    """
    for i in range(len(word)):
        hand[word[i]] = hand[word[i]] - 1
        #print hand[word[i]]
    return(hand)

#
# Problem #3: Test word validity
#
def is_valid_word(word, hand, word_list):
    """
    Returns True if word is in the word_list and is entirely
    composed of letters in the hand. Otherwise, returns False.
    Does not mutate hand or word_list.
    
    word: string
    hand: dictionary (string -> int)
    word_list: list of lowercase strings
    """
    lettersInWord = list()
    lettersInHand = list()
    handDict = dict()
    #testing if the entered word is in word_list
    if not word in word_list and word != ".":
        print bcolors.RED, "word is invalid", bcolors.ENDC
        return False
    #creating list of letters in hand and in entered word
    #to compare and return false if letters not in hand
    for i in range(len(word)):
        lettersInWord.append(word[i])
    for k, v in hand.items():
        lettersInHand.append(k)
    for i in range(len(word)):
        if not word[i] in lettersInHand and word != ".":
            print bcolors.RED,  word[i], " not in hand", bcolors.ENDC
            return False

    for i in range(len(word)):
        handDict[word[i]] = handDict.get(word[i], 0) + 1 
    #trying to compare the word and hand to see if the hand has enough of a letter
    for k in handDict:
        for l in hand:
            if k == l and word != ".":
                if handDict[k] > hand[l]:
                    print bcolors.RED,  "not enough ", l, bcolors.ENDC
                    return False
    if word == "." or hand_is_empty(hand):
        print bcolors.YELLOW, "finished", bcolors.ENDC
    return True
    
def calculate_handlen(hand):
    handlen = 0
    for v in hand.values():
        handlen += v
    return handlen

#
# Problem #4: Playing a hand
#
def play_hand(hand, word_list):

    """
    Allows the user to play the given hand, as follows:

    * The hand is displayed.
    
    * The user may input a word.

    * An invalid word is rejected, and a message is displayed asking
      the user to choose another word.

    * When a valid word is entered, it uses up letters from the hand.

    * After every valid word: the score for that word is displayed,
      the remaining letters in the hand are displayed, and the user
      is asked to input another word.

    * The sum of the word scores is displayed when the hand finishes.

    * The hand finishes when there are no more unused letters.
      The user can also finish playing the hand by inputing a single
      period (the string '.') instead of a word.

      hand: dictionary (string -> int)
      word_list: list of lowercase strings
      
    """
    # TO DO ...
    score = 0
    wordAndScore = dict()
    word = ""
    while not hand_is_empty(hand) and not word == ".":

    
        display_hand(hand)
        valid = False
        word = raw_input('Please enter a word: ')
        while (not is_valid_word(word, hand, word_list)):
            word = raw_input('Please enter a word: ')
            if not is_valid_word(word, hand, word_list ):
                pass
        if word != ".":
            wordAndScore[word] = get_word_score(word, HAND_SIZE)
            score += get_word_score(word, HAND_SIZE)
            print bcolors.MAGENTA, word, bcolors.ENDC, "for", bcolors.GREEN, get_word_score(word, HAND_SIZE), bcolors.ENDC, "points"
            update_hand(hand, word)
    for k, v in wordAndScore.items():
        print bcolors.MAGENTA, k, bcolors.ENDC, "for ", bcolors.GREEN,  v, bcolors.ENDC, "points"
    print "Total score: ", bcolors.GREEN, score, bcolors.ENDC
def hand_is_empty(hand):
    #Returns state of hand in boolean
    inHand = 0
    for k, v in hand.items():
        inHand += v
    if inHand > 0:
        return False
    else:
        return True
        

#
# Problem #5: Playing a game
# Make sure you understand how this code works!
# 
def play_game(word_list):
    """
    Allow the user to play an arbitrary number of hands.

    * Asks the user to input 'n' or 'r' or 'e'.

    * If the user inputs 'n', let the user play a new (random) hand.
      When done playing the hand, ask the 'n' or 'e' question again.

    * If the user inputs 'r', let the user play the last hand again.

    * If the user inputs 'e', exit the game.

    * If the user inputs anything else, ask them again.
    """
    hand = deal_hand(HAND_SIZE)
    print "Welcome to 6.00 word game."
    print "Enter n for a New hand, r to Retry the current hand, or e to Exit"
    print "Your current hand is: ", display_hand(hand)
    choice = raw_input("Please input your choice: ")
    held_hand = hand
    while choice != "e":
        if choice == "r":
            print choice
            hand = held_hand.copy()
            play_hand(hand, word_list)
            print "Welcome to 6.00 word game."
            print "Enter n for a New hand, r to Retry the current hand, or e to Exit"
            print "Your current hand is: ", display_hand(held_hand)
            choice = raw_input("Please input your choice: ")
            if choice == "e":
                break
        elif choice == "n":
            print choice
            hand = deal_hand(HAND_SIZE) 
            held_hand = hand.copy()
            play_hand(hand, word_list)
            print "Welcome to 6.00 word game."
            print "Enter n for a New hand, r to Retry the current hand, or e to Exit"
            print "Your current hand is: ", display_hand(held_hand)
            choice = raw_input("Please input your choice: ")
            if choice == "e":
                break
        elif choice == "e":
            print choice
            break
        else:
            print choice
            print "I'm sorry I don't understand ", choice
            choice = raw_input("Please input your choice: ")
            if choice == "e":
                break


            


#
# Build data structures used for entire session and play game
#
word_list = load_words()
#play_game(word_list)
