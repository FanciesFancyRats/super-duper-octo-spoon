balance = round(float(raw_input('balance: ')), 2)
air = round(float(raw_input('air: ')), 2)

#monthly intrest rate:
mir = air / 12
#balance = balance  * (1+mir) - minimumpayment
payment = 0.0

#minimum monthly payment - this is the target variable
#intrest paid = mir * balance
#principal paid =  minimum monthly  - intrest paid
#check balance
solved = False
while(solved == False):
    testBalance = balance
    payment += 10.0
    i = 0
    while(i < 12) and (testBalance > 0):
        intrestPaid =round(mir * testBalance, 2)
        principalPaid = round(payment - intrestPaid, 2)
        testBalance = round(testBalance - principalPaid, 2)
        #print '$' , testBalance
        i += 1
    if testBalance < 0:
        solved = True
        
print "RESULT"
print 'Monthly payment to pay off debt in 1 year: ', payment
print 'Number of months needed: ', i
print 'Balance: ', testBalance
