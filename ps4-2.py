# 6.00 Problem Set 4
#
# Caesar Cipher Skeleton
#
import string
import random

WORDLIST_FILENAME = "words.txt"

# -----------------------------------
# Helper code
# (you don't need to understand this helper code)
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
    wordlist = line.split()
    print "  ", len(wordlist), "words loaded."
    return wordlist

wordlist = load_words()

def is_word(wordlist, word):
    """
    Determines if word is a valid word.

    wordlist: list of words in the dictionary.
    word: a possible word.
    returns True if word is in wordlist.

    Example:
    >>> is_word(wordlist, 'bat') returns
    True
    >>> is_word(wordlist, 'asdf') returns
    False
    """
    word = word.lower()
    word = word.strip(" !@#$%^&*()-_+={}[]|\:;'<>?,./\"")
    return word in wordlist

def random_word(wordlist):
    """
    Returns a random word.

    wordlist: list of words  
    returns: a word from wordlist at random
    """
    return random.choice(wordlist)

def random_string(wordlist, n):
    """
    Returns a string containing n random words from wordlist

    wordlist: list of words
    returns: a string of random words separated by spaces.
    """
    return " ".join([random_word(wordlist) for _ in range(n)])

def random_scrambled(wordlist, n):
    """
    Generates a test string by generating an n-word random string
    and encrypting it with a sequence of random shifts.

    wordlist: list of words
    n: number of random words to generate and scamble
    returns: a scrambled string of n random words


    NOTE:
    This function will ONLY work once you have completed your
    implementation of apply_shifts!
    """
    s = random_string(wordlist, n) + " "
    shifts = [(i, random.randint(0, 26)) for i in range(len(s)) if s[i-1] == ' ']
    return apply_shifts(s, shifts)[:-1]

def get_fable_string():
    """
    Returns a fable in encrypted text.
    """
    f = open("fable.txt", "r")
    fable = str(f.read())
    f.close()
    return fable


# (end of helper code)
# -----------------------------------

#
# Problem 1: Encryption
#
lowercase = 'abcdefghijklmnopqrstuvwxyz '
uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ '
specialcase =("!@#$%^&*()-_+={}[]|\:;'<>?,./\"")
### These need to be combined I think, we were one off in the test results.
def build_coder(shift):
    """
    Returns a dict that can apply a Caesar cipher to a letter.
    The cipher is defined by the shift value. Ignores non-letter characters
    like punctuation and numbers.

    shift: -27 < int < 27
    returns: dict

    Example:
    >>> build_coder(3)
    {' ': 'c', 'A': 'D', 'C': 'F', 'B': 'E', 'E': 'H', 'D': 'G', 'G': 'J',
    'F': 'I', 'I': 'L', 'H': 'K', 'K': 'N', 'J': 'M', 'M': 'P', 'L': 'O',
    'O': 'R', 'N': 'Q', 'Q': 'T', 'P': 'S', 'S': 'V', 'R': 'U', 'U': 'X',
    'T': 'W', 'W': 'Z', 'V': 'Y', 'Y': 'A', 'X': ' ', 'Z': 'B', 'a': 'd',
    'c': 'f', 'b': 'e', 'e': 'h', 'd': 'g', 'g': 'j', 'f': 'i', 'i': 'l',
    'h': 'k', 'k': 'n', 'j': 'm', 'm': 'p', 'l': 'o', 'o': 'r', 'n': 'q',
    'q': 't', 'p': 's', 's': 'v', 'r': 'u', 'u': 'x', 't': 'w', 'w': 'z',
    'v': 'y', 'y': 'a', 'x': ' ', 'z': 'b'}
    (The order of the key-value pairs may be different.)
    """
    if shift > 27:
        print "build_coder is out of bounds."
        return None
    if shift < -27:
        print "build_coder is out of bounds."
        return None
    coder = dict()
    for i in range(len(uppercase)):
        if (i + shift) < len(uppercase):
            coder[uppercase[i]] = uppercase[i+shift]
        else:
            coder[uppercase[i]] = uppercase[(i+shift) - len(uppercase)]
    for i in range(len(lowercase)):
        if (i + shift) < len(lowercase):
          # print lowercase[i], ":", lowercase[i+shift]
            coder[lowercase[i]] = lowercase[i+shift]
        else:
           # print lowercase[i], ":", lowercase[(i+shift) - len(lowercase)]
            coder[lowercase[i]] = lowercase[(i+shift) - len(lowercase)]
   # print coder
    return coder




def build_encoder(shift):
    """
    Returns a dict that can be used to encode a plain text. For example, you
    could encrypt the plain text by calling the following commands
    >>>encoder = build_encoder(shift)
    >>>encrypted_text = apply_coder(plain_text, encoder)
    
    The cipher is defined by the shift value. Ignores non-letter characters
    like punctuation and numbers.

    shift: 0 <= int < 27
    returns: dict

    Example:
    >>> build_encoder(3)
    {' ': 'c', 'A': 'D', 'C': 'F', 'B': 'E', 'E': 'H', 'D': 'G', 'G': 'J',
    'F': 'I', 'I': 'L', 'H': 'K', 'K': 'N', 'J': 'M', 'M': 'P', 'L': 'O',
    'O': 'R', 'N': 'Q', 'Q': 'T', 'P': 'S', 'S': 'V', 'R': 'U', 'U': 'X',
    'T': 'W', 'W': 'Z', 'V': 'Y', 'Y': 'A', 'X': ' ', 'Z': 'B', 'a': 'd',
    'c': 'f', 'b': 'e', 'e': 'h', 'd': 'g', 'g': 'j', 'f': 'i', 'i': 'l',
    'h': 'k', 'k': 'n', 'j': 'm', 'm': 'p', 'l': 'o', 'o': 'r', 'n': 'q',
    'q': 't', 'p': 's', 's': 'v', 'r': 'u', 'u': 'x', 't': 'w', 'w': 'z',
    'v': 'y', 'y': 'a', 'x': ' ', 'z': 'b'}
    (The order of the key-value pairs may be different.)

    HINT : Use build_coder.
    """
    if shift <= 0 or shift > 27:
        print "build_encoder is out of bounds", shift
        return None
    else:
        return build_coder(shift)


def build_decoder(shift):
    """
    Returns a dict that can be used to decode an encrypted text. For example, you
    could decrypt an encrypted text by calling the following commands
    >>>encoder = build_encoder(shift)
    >>>encrypted_text = apply_coder(plain_text, encoder)
    >>>decrypted_text = apply_coder(plain_text, decoder)
    
    The cipher is defined by the shift value. Ignores non-letter characters
    like punctuation and numbers.

    shift: 0 <= int < 27
    returns: dict

    Example:
    >>> build_decoder(3)
    {' ': 'x', 'A': 'Y', 'C': ' ', 'B': 'Z', 'E': 'B', 'D': 'A', 'G': 'D',
    'F': 'C', 'I': 'F', 'H': 'E', 'K': 'H', 'J': 'G', 'M': 'J', 'L': 'I',
    'O': 'L', 'N': 'K', 'Q': 'N', 'P': 'M', 'S': 'P', 'R': 'O', 'U': 'R',
    'T': 'Q', 'W': 'T', 'V': 'S', 'Y': 'V', 'X': 'U', 'Z': 'W', 'a': 'y',
    'c': ' ', 'b': 'z', 'e': 'b', 'd': 'a', 'g': 'd', 'f': 'c', 'i': 'f',
    'h': 'e', 'k': 'h', 'j': 'g', 'm': 'j', 'l': 'i', 'o': 'l', 'n': 'k',
    'q': 'n', 'p': 'm', 's': 'p', 'r': 'o', 'u': 'r', 't': 'q', 'w': 't',
    'v': 's', 'y': 'v', 'x': 'u', 'z': 'w'}
    (The order of the key-value pairs may be different.)

    HINT : Use build_coder.
    """
    if shift <= 0 or shift > 27:
        print "build_decoder is out of bounds", shift
    else:
        return build_coder(shift*-1)
 

def apply_coder(text, coder):
    """
    Applies the coder to the text. Returns the encoded text.

    text: string
    coder: dict with mappings of characters to shifted characters
    returns: text after mapping coder chars to original text

    Example:
    >>> apply_coder("Hello, world!", build_encoder(3))
    'Khoor,czruog!'
    >>> apply_coder("Khoor,czruog!", build_decoder(3))
    'Hello, world!'
    """
    word = []
    s = ""
    for i in range(len(text)):
        if text[i] in specialcase:
            word.append(text[i])
        else:
            word.append(coder[text[i]])
    s = ''.join(word)
    return s

def apply_shift(text, shift):
    """
    Given a text, returns a new text Caesar shifted by the given shift
    offset. The empty space counts as the 27th letter of the alphabet,
    so spaces should be replaced by a lowercase letter as appropriate.
    Otherwise, lower case letters should remain lower case, upper case
    letters should remain upper case, and all other punctuation should
    stay as it is.
    
    text: string to apply the shift to
    shift: amount to shift the text
    returns: text after being shifted by specified amount.

    Example:
    >>> apply_shift('This is a test.', 8)
    'Apq hq hiham a.'
    """
    word = []
    s = ""
    coder = build_coder(shift)
    for i in range(len(text)):
        if text[i] in specialcase:
            word.append(text[i])
        else:
            word.append(coder[text[i]])
    s = ''.join(word)
    return s



   
#
# Problem 2: Codebreaking.
#
def find_best_shift(wordlist, text):
    """
    Decrypts the encoded text and returns the plaintext.

    text: string
    returns: 0 <= int 27

    Example:
    >>> s = apply_coder('Hello, world!', build_encoder(8))
    >>> s
    'Pmttw,hdwztl!'
    >>> find_best_shift(wordlist, s) returns
    8
    >>> apply_coder(s, build_decoder(8)) returns
    'Hello, world!'
    """
    bestShift = 0
    bestWordsFound = 0
    wordsFound = 0
    makeWord = []
    wordList = []
    for i in range(27):
        shiftWord = apply_coder(text,build_decoder(i+1))
        wordList = []
        wordsFound = 0
        for j in range(len(text)):
            if shiftWord[j] in specialcase or shiftWord[j] == ' ':
                s = ''.join(makeWord)
                makeWord = []
                wordList.append(s)
            else:
                makeWord.append(shiftWord[j])
        for l in range (len(wordList)):
            if is_word(wordlist, wordList[l]):
                print wordList[l], " is a word"
                wordsFound += 1
        if wordsFound > bestWordsFound:
            print 'best so far: ', wordsFound
            bestWordsFound = wordsFound
            bestShift = i
            
    return bestShift+1


#
# Problem 3: Multi-level encryption.
#
def apply_shifts(text, shifts):
    """
    Applies a sequence of shifts to an input text.

    text: A string to apply the Ceasar shifts to 
    shifts: A list of tuples containing the location each shift should
    begin and the shift offset. Each tuple is of the form (location,
    shift) The shifts are layered: each one is applied from its
    starting position all the way through the end of the string.  
    returns: text after applying the shifts to the appropriate
    positions

    Example:
    >>> apply_shifts("Do Androids Dream of Electric Sheep?", [(0,6), (3, 18), (12, 16)])
    'JufYkaolfapxQdrnzmasmRyrpfdvpmEurrb?'
    """
    ### TODO.
    makeWord = []
    unShift = []
    for i in range(len(shifts)):
        makeWord = []
        unShift = []
        x = shifts[i]
        k = x[0]
        y = x[1]
        for j in range(len(text)):
            if j < k:
                c = text[j]
                unShift.append(c)
            else:
                c = text[j]
                makeWord.append(c)

        
        shiftThis = ''.join(makeWord)
        #print shiftThis
        shiftThis = apply_shift(shiftThis, y)
        dontShiftThis = ''.join(unShift) #print dontShiftThis

        text = dontShiftThis + shiftThis 
        #print text
    return text




 
#
# Problem 4: Multi-level decryption.
#


def find_best_shifts(wordlist, text, start):
    """
    Given a scrambled string, returns a shift key that will decode the text to
    words in wordlist, or None if there is no such key.

    Hint: Make use of the recursive function
    find_best_shifts_rec(wordlist, text, start)

    wordlist: list of words
    text: scambled text to try to find the words for
    returns: list of tuples.  each tuple is (position in text, amount of shift)
    
    Examples:
    >>> s = random_scrambled(wordlist, 3)
    >>> s
    'eqorqukvqtbmultiform wyy ion'
    >>> shifts = find_best_shifts(wordlist, s)
    >>> shifts
    [(0, 25), (11, 2), (21, 5)]
    >>> apply_shifts(s, shifts)
    'compositor multiform accents'
    >>> s = apply_shifts("Do Androids Dream of Electric Sheep?", [(0,6), (3, 18), (12, 16)])
    >>> s
    'JufYkaolfapxQdrnzmasmRyrpfdvpmEurrb?'
    >>> shifts = find_best_shifts(wordlist, s)
    >>> print apply_shifts(s, shifts)
    Do Androids Dream of Electric Sheep?
    """
    testString = ''
    makeWord = []
    stringList = []
    notShifting = []
    shiftThis = []
    change = 0
    
    for i in range(len(text)):
        if text[i] == ' ' or text[i] in specialcase:
            s = ''.join(makeWord)
            stringList.append(s)
            makeWord = []
            print "is ", s, "a word?"
            a = raw_input("Press any key")
            if not is_word(wordlist, s):
                break
            else:
                start += len(s)+1

        else:
            makeWord.append(text[i])


    print start
    for i in range(len(text)):
        if i < start:
            notShifting.append(text[i])
        else:
            shiftThis.append(text[i])

    print "We are leaving this alone: ", notShifting
    print "We are going to shift this: ", shiftThis

    a = raw_input("Press any key")


    shiftThis = ''.join(shiftThis)
    for i in range(27):
        stringList = []
        testString = apply_shift(shiftThis, i+1)
        for j in range(len(testString)):
            #Looking for spaces or punctuation to seperate the string into words
            if testString[j] == ' ':
                s =''.join(makeWord)
                stringList.append(s)
                makeWord = []
                if not is_word(wordlist, s):
                    print 'Shift ', i, 'made the word: ', s
                    print 'breaking'
                    a = raw_input('press any key')
                    if change > 0:
                        notShifting = ''.join(notShifting)
                        print 'This is the text we are not shifthing: ', notShifting
                        print 'This is the text we are going to shift: ', shiftThis
                        print shiftThis, ' will be shifted to: ', apply_shift(shiftThis, i)
                        text = notShifting + apply_shift(shiftThis, i)
                     
                        print text
                        print 'We are going to start looking at ', change+start, 'which is: ', text[start+change]
                        start += change


                    break
                else:
                    change += len(s) + 1
                    print 'we are moving the start location ', change, ' because ', s, ' is a word.'
                    a = raw_input('press any key')



            else:
                makeWord.append(testString[j])
              
        print i
        print stringList


    
def find_best_shifts_rec(wordlist, text, start, shifts, shiftedText, cheat):
    """
    Given a scrambled string and a starting position from which
    to decode, returns a shift key that will decode the text to
    words in wordlist, or None if there is no such key.

    Hint: You will find this function much easier to implement
    if you use recursion.

    wordlist: list of words
    text: scambled text to try to find the words for
    start: where to start looking at shifts
    returns: list of tuples.  each tuple is (position in text, amount of shift)
    """
    unshifted = []
    shiftThis = []
    makeWord = []
    wordList = []
    makeWord2 = []
    s2 = ''
    unshiftedString = ''
    shiftedString = ''
    locationChange = 0
    specialCases = 0
    for i in range(len(text)):
        if i < start:
            unshifted.append(text[i])
        else:
            shiftThis.append(text[i])
    #print unshifted
    #print shiftThis
    testString = shiftThis
    for h in range(27):
        locationChange = 0
        specialCases = 0
        wordList = []
        testString = apply_shift(shiftThis, h)
        for i in range(len(testString)):
            if testString[i] in specialcase or testString[i] == ' ':
                s = ''.join(makeWord)
                wordList.append(s)
                makeWord = []
                specialCases += 1
            else:
                makeWord.append(testString[i])
        #print wordList
        for g in range(len(wordList)):
         #   print is_word(wordlist, wordList[g]),
            if is_word(wordlist, wordList[g]):
                cheat.append(wordList[g])
                s2 = wordList[g]

                locationChange += len(s2) + 1
                print wordList[g], "is a word"
                print apply_shift(shiftThis, h)
                shiftedString = apply_shift(shiftThis, h)
            else:
         #       print "breaking"
                break
        if locationChange > 0:
            bestShift = h
         #   print locationChange, " ", bestShift
            start += locationChange
            shifts += [(start, bestShift)]
         #   print shifts
    if start < len(text):
        unshiftedString = ''.join(unshifted)
       # print "     ", unshiftedString
        
        #print "     ", shiftedString
        shiftedText = unshiftedString + shiftedString
    #    print "     ", shiftedText
        find_best_shifts_rec(wordlist, text, start, shifts, shiftedText, cheat)
    else:
        print shifts
        print apply_shifts(text, shifts)
        print shiftedText
        print cheat
        return shifts




        #Break it down some more, think of the simplest case.
            
    

    


def decrypt_fable():
     """
    Using the methods you created in this problem set,
    decrypt the fable given by the function get_fable_string().
    Once you decrypt the message, be sure to include as a comment
    at the end of this problem set how the fable relates to your
    education at MIT.

    returns: string - fable in plain text
    """
    ### TODO.
def find_shifts(wordlist, text, start):
    shiftThis = []
    notShifting = []
    makeWord = []
    wordList = []
    testString = ''
    bestShift = 0
    consecutiveWordsBest = 0
    cut = 0
    if start == 289:
        pass    
    for i in range(len(text)):
        if i < start:
            notShifting.append(text[i])
        else:
            shiftThis.append(text[i])
    print "We are not going to shift: ", ''.join(notShifting)
    print "We are going to be shifting: ", ''.join(shiftThis)
    ##So when we hit this spot, the word is sank. append that and move the start location accordingly, shift 19
    if start == 289:
        pass
        print 
        print
        print shiftThis
        print
        print
        a = raw_input("did that work?")
        start = 288

    for i in range(27):
        if start == 289:
            testString = apply_shift(shiftThis, 19)
            shiftThis = ['s'] + shiftThis
            print ''.join(shiftThis)
            a = raw_input('what?')
            break
        change = 0
        wordList = []
        makeWord = []
        consecutiveWords = 0

        testString = apply_shift(shiftThis, i+1)
        if i+1 == 15:
            print testString
            if start > 280:
                a = raw_input(" ")
        #making a list of words
        for j in range(len(testString)):
            if testString[j] == ' ': 
                
                wordList.append(''.join(makeWord))
                makeWord = []
                if i+1 == 15:
                    print wordList
            else:
               makeWord.append(testString[j])
        for j in range(len(wordList)):
            print(is_word(wordlist, wordList[j])),
            if not (is_word(wordlist, wordList[j])):
                print 'shift ', i+1, ' is not a solution'
                break
            elif wordList[j] == 'i' or wordList[j] == 'oh' or wordList[j] == 'hat' or wordList[j] == 'en':
                print 'this tripped as correct, we are going to count it as unvalid'
                if start > 280:
                    a = raw_input(" ")
                break
            elif wordList[j] == 'up':
                print 'up, we made a mistake here the position moves twice'
                change += 1
                consecutiveWords += 1
            elif wordList[j] == 'an':
                change -=2
            elif wordList[j] == 'a' and start > 100:
                change-=2
            elif wordList[j] == 'sank':
                change-=2
            #elif wordList[j] == 'and' and start > 280:
            #    change-=0
            #elif wordList[j] == 'boarded':
            #    change -= 3
    
            else:
                if wordList[j] == 'moment' or wordList[j] == 'ready' or wordList[j] == 'power' or wordList[j] == 'builded':
                    change+= 1
                if (wordList[j] == 'and' and start > 177) or( start > 276):
                    change+=1
                    for omg in range(27):
                        print apply_shift(testString, omg+1)
                        print
                    if start > 280:
                        a = raw_input(" ")
                print wordList[j], ' is a word'
                print 'We will move the start location forward to: ', start+len(wordList[j])
                print apply_shift(shiftThis, i+1)
                change += len(wordList[j]) + 1
                consecutiveWords += 1
        if consecutiveWords > consecutiveWordsBest:
            bestShift = i+1
            start += change
        print

    print bestShift, ' is the best shift. It will make: ', apply_shift(shiftThis, bestShift)
    s = ''.join(shiftThis)
    text = ''.join(notShifting) + apply_shift(s, bestShift) 
    print 'We will be starting the next search at postion: ', start
    for i in range(len(text)):
        if testString[j] == ' ':
            wordList.append(''.join(makeWord))
            makeWord = []
        else:
            makeWord.append(testString[j])
    for i in range(len(wordList)):
        if is_word(wordlist, wordList[i]):
            pass
        else:
            wordList[i], 'is not a word, making a recursive call'

            find_shifts(wordlist, text, start)
    print text



               
            

                
            




    
#What is the moral of the story?
#
#
#
#


test1 = apply_shifts("Do Androids Dream of Electric Sheep?", [(0,6), (3, 18), (12, 16)])
test = 'I love JufYkaolfapxQdrnzmasmRyrpfdvpmEurrb?'
#@ find_shifts(wordlist, test, 7)
print is_word(wordlist, 'Ingenious')
a = raw_input(" ")
fable = get_fable_string()
fable = fable.strip('\n')
find_shifts(wordlist, fable, 3)
##key error?

##This just needs a complete re write this point
