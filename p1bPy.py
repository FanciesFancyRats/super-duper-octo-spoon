minimumPayment = 0.0
intrestPaid = 0.0
principalPaid = 0.0
balance = 0.0
air = 0.0
minimumRate = 0.0
x = 0
amountPaid = 0.0
balanceCheck = 10
remainingBalance = 0.0


    #print'Enter the outstanding balance on your credit card: '
balance = raw_input('Enter the outstanding balance on your credit card: ')
float(balance)
air = raw_input('Enter the annual credit card intrest rate as a decimal: ')
float(air)
    #minimumRate = raw_input('Enter the minimum monthly payment rate as a decimal: ')
    #minimumRate = float(minimumRate)
    #minimumPayment = float(round(minimumPayment, 2))

intrestPaid = float(intrestPaid)
principalPaid = float(principalPaid)
balance = float(balance)
air = float(air)
print('loop 0')
print (balanceCheck)
while balanceCheck > 0:
    print('loop 1')
    print(balanceCheck)
    print(minimumPayment)
    minimumPayment = minimumPayment + 0.01;
    remainingBalance = balance
    x = 0
    while ((x < 12) & (balanceCheck > 0)):

        intrestPaid = round(((air/12.0)*remainingBalance),2)
        print(intrestPaid)
        principalPaid = round((minimumPayment - intrestPaid), 2)
        print(principalPaid)
        remainingBalance = round((remainingBalance - principalPaid),2)
        print(remainingBalance)
        balanceCheck = remainingBalance
        x = x + 1
        print(x)
#print(minimumPayment)
#print(remainingBalance)
#print(x)

    #for x in range(12):
    #        print("Month: %s" % (x + 1))
    #        minimumPayment = round((minimumRate * balance), 2)
    #        print("Minimum monthly payment: %s" % (minimumPayment))
            #print (minimumPayment)
    #        intrestPaid = round(((air/12.0)*balance),2)
    #        principalPaid = round((minimumPayment - intrestPaid),2)
    #        amountPaid = amountPaid + intrestPaid + principalPaid
    #        print("Principle paid: %s" % (principalPaid))
    #        balance = round((balance - principalPaid),2)
    #        print("Remaining balance: %s" % (balance))

print("RESULT")
print ('Monthly payment to pay off debt in 1 year: $%s' % (minimumPayment))
print ('Number of months needed: $%s' % (x))
print ('Remaining balance : $%s') % (balanceCheck)
