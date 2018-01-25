WORDLIST_FILENAME = "words.txt"

def load_words():
    print "Loading word list from file..."
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    wordlist = []
    for line in inFile:
        wordlist.append(line.strip().lower())
    print "  ", len(wordlist), "words loaded."
    return wordlist
word_list = load_words()

def is_letter_valid(letters, word_list):

    #takes in the list of letters so far and determins validity
    word = ''.join(letters)
    print word_list.find(word)
    print word in word_list
letters = ['p', 'e', 'a', 'f']

is_letter_valid(letters, word_list)
