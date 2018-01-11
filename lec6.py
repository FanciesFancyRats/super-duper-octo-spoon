#EtoF = {'bread' : 'du pain', 'wine' : 'du vin',\
#        'eats' : 'mange', 'drinks' : 'bois',\
#        'likes' : 'aime', 1: 'un',\
#        '6.00':'6.00'}
#def translateWord(word, dictionary):
#    if word in dictionary:
#        return dictionary[word]
#    else:
#        return word
#def translate(sentence):
#    translation = ''
#    word = ''
#    for c in sentence:
#        if c != ' ':
#            word = word + c
#            print word
#        else:
#            translation = translation + ' ' + translateWord(word, EtoF)
#            word = ''
#            print translation
#    return translation[1:] + ' ' + translateWord(word, EtoF)
#print translate('John eats bread')
#print translate('Eric drinks wine')
#print translate('Everyone likes 6.00')
# at 21:00
#def simpleExp(b, n):
#    if n == 0:
#        return 1
#    else:
#        return b * simpleExp(b, n-1)
#print simpleExp(3, 2)
#def Hanoi(n, f, t, s):
#    if n == 1:
#        print "move from " + f + ' to ' + t
#    else:
#        Hanoi(n-1, f, s, t)
#        Hanoi(1, f, t, s)
#        Hanoi(n-1, s, t, f)
#Hanoi(3, 'f', 's', 't')
#def toChars(s):
#    import string
#    s = string.lower(s)
#    ans = ''
#    for c in s:
#        if c in string.lowercase:
#            ans = ans + c
#    return ans
#def isPal(s):
#    if len(s) <= 1:
#        return True
#    else:
#        return s[0] == s[-1] and isPal(s[1:-1])
#
#def isPalimdrone(s):
#    return isPal(toChars(s))
#print isPalimdrone('Guttag')
#print isPalimdrone('Guttug')
#print isPalimdrone('Are we not drawn onward, we few, drawn onward to new era?')
#f(n) = f(n-2) + f(n-1)
def fib(n):
    if n == 0
