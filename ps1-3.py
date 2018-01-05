#monthly payment lower bound = balance / 12.0
#monthly payment upper bound = balance * (1 + mir) ** 12.0) / 12.0

balance = round(float(raw_input('Please enter the balance: ')),2)
air = round(float(raw_input('Please enter the air: ')),2)
mir = air/12
#Minimum monthly payment - This is the target variable
#Intrest paid = mir * balance
#Principal paid = minimum monthly payment - Intrest paid
#Balance = Balance - Principal paid

lowerBound = round(balance/12.0, 2)
upperBound = round((balance * (1 + mir) ** 12.0)/12, 2)
bisection = (lowerBound+upperBound)/2
solved = False
balanceCheck = balance

def paymentCycle(payment):
    for i in range (12):
        balanceCheck = round(balance)
        intrestPaid = round(mir * balanceCheck)
        principalPaid = round(payment - intrestPaid)
        balanceCheck = round(balanceCheck - principalPaid)
    return round(balanceCheck)
print lowerBound
print upperBound

x = 0
print(abs(balanceCheck) > .2) and (x < 9)
while(abs(balanceCheck) > .2) and (x < 9):
    balanceCheck = balance
    testLowerBound = paymentCycle((lowerBound + bisection)/2)
   # print ' testLowerBound: ' , testLowerBound
    testUpperBound = paymentCycle((upperBound + bisection)/2)
   # print ' testUpperBound: ' , testUpperBound
    if(abs(testUpperBound) <= abs(testLowerBound)):
        lowerBound = bisection
       # print 'bisection' , bisection
       # print 'We went up' , testUpperBound
    if(abs(testUpperBound) > abs(testLowerBound)):
        upperBound = bisection
   #     print 'We went down' , testLowerBound
    bisection = (lowerBound + upperBound)/2
    payment = bisection
    balanceCheck = paymentCycle(payment)
    print 'Current balance: ' , balanceCheck
    x += 1
#y = paymentCycle(bisection)
#print y 
