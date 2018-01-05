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
balance = 320000
air = .2

lowerBound = round(balance/12.0, 2)
upperBound = float(round((balance * (1 + (air/12))**12)/12, 2))
bisection = (lowerBound + upperBound) / 2
x = 0

while abs(bisection) > 0.2 and x < 99:
    testLower = paymentCycle(lowerBound, balance, air)
    testUpper = paymentCycle(upperBound, balance, air)
    testBisection = paymentCycle(bisection, balance, air)

    print testLower, lowerBound
    print testUpper, upperBound 
    print testBisection, bisection 
    y = raw_input('press a key')
    if abs(testBisection) < 0.2:
        break
    if abs(testLower - testBisection) < abs(testUpper - testBisection):
        upperBound = bisection
        bisection = (lowerBound + upperBound) / 2
    else:
        lowerBound = bisection
        bisection = (lowerBound + upperBound) / 2
    x += 1
print testBisection