def isPal(x):
    assert type(x) == list
    temp = x
    temp.reverse()
    print 'x: ', x
    print 'temp: ', temp
    if temp == x:
        return True
    else:
        return False

def silly(n):
    assert type(n) == int and n > 0
    result = []
    for i in range (n):
        elem = raw_input('Enter something: ')
        result.extend(elem)
        print "result: ", result
    if isPal(result):
        print 'Is a palindrome'
    else:
        print 'Is not a palindrome'

def isPalTest():
    L = [1, 2]
    result = isPal(L)
    print "shoud be false: ", result
    L = [1,2,1]
    result = isPal(L)
    print "should be true: ", result
isPalTest()
