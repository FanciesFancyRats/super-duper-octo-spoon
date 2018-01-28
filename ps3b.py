from ps3a import *
import time
from perm import *


#
#
# Problem #6A: Computer chooses a word
#
#
def comp_is_valid_word(word, hand, word_list):
    lettersInWord = list()
    lettersInHand = list()
    handDict = dict()

    if not word in word_list and word != ".":
        return False
    for i in range(len(word)):
        lettersInWord.append(word[i])
    for k, v in hand.items():
        lettersInHand.append(k)
    for i in range(len(word)):
        if not word[i] in lettersInHand and word != ".":
            return False
    for i in range(len(word)):
        handDict[word[i]] = handDict.get(word[i], 0) + 1

    for k in handDict:
        for l in hand:
            if k == l and word !=".":
                if handDict[k] > hand[l]:
                    return False
    if word == "." or hand_is_empty(hand):
        print bcolors.YELLOW, "finished", bcolors.ENDC
    return True

def comp_choose_word(hand, word_list):
    """
	Given a hand and a word_dict, find the word that gives the maximum value score, and return it.
   	This word should be calculated by considering all possible permutations of lengths 1 to HAND_SIZE.

    hand: dictionary (string -> int)
    word_list: list (string)
    """
    # TO DO...
    # Use get_perms to brute for an answer that will return true for a copy of is_word_valid
    stringsToTry = []
    print "line 23"
    for i in range(HAND_SIZE):
        stringsToTry = stringsToTry + get_perms(hand, i)
    wordsToTry = []
    for i in range(len(stringsToTry)):
        if comp_is_valid_word(stringsToTry[i], hand, word_list):
            wordsToTry.append(stringsToTry[i])
            print stringsToTry[i]
    print wordsToTry 
    highScore = 0
    word = ""
    for i in range(len(wordsToTry)):
        if get_word_score(wordsToTry[i], HAND_SIZE) > highScore:

           highScore = get_word_score(wordsToTry[i], HAND_SIZE)
           word = wordsToTry[i]
    if not wordsToTry:
        print "using  '.'"
        return '.'
    else:
        print "using ", word
        return word



#
# Problem #6B: Computer plays a hand
#
def comp_play_hand(hand, word_list):
    """
     Allows the computer to play the given hand, as follows:

     * The hand is displayed.

     * The computer chooses a word using comp_choose_words(hand, word_dict).

     * After every valid word: the score for that word is displayed, 
       the remaining letters in the hand are displayed, and the computer 
       chooses another word.

     * The sum of the word scores is displayed when the hand finishes.

     * The hand finishes when the computer has exhausted its possible choices (i.e. comp_play_hand returns None).

     hand: dictionary (string -> int)
     word_list: list (string)
    """
    # TO DO ...    
    score = 0
    wordAndScore = dict()
    word = ""
    while not hand_is_empty(hand) and not word == ".":

        display_hand(hand)
        valid = False
        word = comp_choose_word(hand, word_list)
        if word != ".":
            wordAndScore[word] = get_word_score(word, HAND_SIZE)
            score += get_word_score(word, HAND_SIZE)
            print bcolors.MAGENTA, word, bcolors.ENDC, "for", bcolors.GREEN, get_word_score(word, HAND_SIZE), bcolors.ENDC, "points"
            update_hand(hand, word)
    for k, v in wordAndScore.items():
        print bcolors.MAGENTA, k, bcolors.ENDC, "for ", bcolors.GREEN, v, bcolors.ENDC, "points"
        print "Total score: ", bcolors.GREEN, score, bcolors.ENDC
     
#
# Problem #6C: Playing a game
#
#
def play_game(word_list):
    """Allow the user to play an arbitrary number of hands.

    1) Asks the user to input 'n' or 'r' or 'e'.
    * If the user inputs 'n', play a new (random) hand.
    * If the user inputs 'r', play the last hand again.
    * If the user inputs 'e', exit the game.
    * If the user inputs anything else, ask them again.

    2) Ask the user to input a 'u' or a 'c'.
    * If the user inputs 'u', let the user play the game as before using play_hand.
    * If the user inputs 'c', let the computer play the game using comp_play_hand (created above).
    * If the user inputs anything else, ask them again.

    3) After the computer or user has played the hand, repeat from step 1

    word_list: list (string)
    """
    # TO DO...
    hand = deal_hand(HAND_SIZE)
    print "Welcome to 6.00 word game~"
    print "Enter n for a New hand, r to Retry the current hand, or e to Exit"
    print "Our current hand is: ", display_hand(hand)
    choice = raw_input("Please input your choice: ")
    held_hand = hand.copy()
    while choice != "e":
        if choice == "r":
            hand = held_hand.copy()
            print "Who goes first, you('u') or I('c')?"
            ##Need to finis this branching path
        
#
# Build data structures used for entire session and play game
#
#if __name__ == '__main__':
#    word_list = load_words()
#    play_game(word_list)
hand = deal_hand(HAND_SIZE)
comp_play_hand(hand, word_list)
