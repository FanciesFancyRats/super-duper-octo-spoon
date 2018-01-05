def paymentCycle(payment, balance, air):
    for i in range (12):
        intrestPaid = float(round((air/12) * balance, 2))
        principalPaid = float(round(payment - intrestPaid, 2))
        balance -= float(round(principalPaid, 2))
        if balance < 0:
            break
    return(balance)
#balance = float(round(raw_input('Please enter the balance: '), 2))
#air = float(round(raw_input('Please enter annual intrest rate: '), 2))
balance = 999999
air = .18

lowerBound = round(balance/12.0, 2)
upperBound = float(round((balance * (1 + (air/12))**12)/12, 2))
bisection = float(round((lowerBound + upperBound)/2, 2)) 
x = 0

while x < 99:
    testLower = round(paymentCycle(lowerBound, balance, air), 2)
    testUpper = round(paymentCycle(upperBound, balance, air), 2)
    testBisection = round(paymentCycle(bisection, balance, air), 2)

    print 'upperbound returns: ', testUpper,'payment: ', upperBound 
    print 'bisection returns: ', testBisection,'payment: ', bisection 
    print 'lowerbound returns: ', testLower,'payment: ', lowerBound
    y = raw_input('press a key')
    if abs(testBisection) < 0.2:
        break
    if abs(testLower) - abs(testBisection) < abs(testUpper) - abs(testBisection):
        print 'line 31'
        upperBound = round(bisection, 2)
        bisection = round((lowerBound + upperBound) / 2, 2)
    else:
        print 'line 34'
        lowerBound = round(bisection, 2)
        bisection = round((lowerBound + upperBound) / 2, 2)
    x += 1
print 'payment: ', bisection
print 'balance: ', testBisection
#We are having some sort of rounding error, my results are off by about 0.02 from the test cases.
#Not sure where this is happening, might ask around or come back later. Would definetly like to move on though.
