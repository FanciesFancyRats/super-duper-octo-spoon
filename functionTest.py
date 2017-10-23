def printTwice(s):
    print(s)
    print(s)
def doTwice(f, v):
    f(v)
    f(v)
def doFour(f, v):
    doTwice(f, v)
    doTwice(f, v)
word = "spam"
doFour(printTwice, word)
