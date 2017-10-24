def printX ():
    print "+ - - - - +" , "- - - - +" , "- - - - +" , "- - - - +"
def printY(y):
    print "|         |" , "        |" * y
def doFour(f, y):
    f(y)
    f(y)
    f(y)
    f(y)
def printSquare():
    printX()
    doFour(printY(), 3)
    printX()
    doFour(printY(), 3)
    printX()
    doFour(printY(), 3)
    printX()
    doFour(printY(), 3)
    printX()
printSquare()
