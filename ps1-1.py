balance = raw_input('Please input the outstanding balance: ')
balance = float(balance)
anualIntrestRate = raw_input('Please input the anual intrest rate: ')
anualIntrestRate = float(anualIntrestRate)
minimumRate = raw_input('Please input the minimum monthly payment rate: ')
minimumRate = float(minimumRate)
print balance, anualIntrestRate, minimumRate
#Minimum monthly payment = minimumRate * balance
#(minimum monthly payment gets split into intrest paid and principal paid)
#intrest paid = anualIntestRate / 12 months * balance
#pricipal paid = Minimum monthly payment - intrest paid
#remaing balance = balance - principal paid


#print 'minimumPayment', minimumPayment


#month n
#minimum monthly payment
#principal paid
#remaining balance
for i in range (12):
    minimumPayment = round(minimumRate * balance, 2)
    
    print 'Month: ', (i+1)
    intrestPaid = round((anualIntrestRate/12) * balance, 2)
    print 'Minimum monthly payment: $', minimumPayment
    principalPaid = round(minimumPayment - intrestPaid, 2)
    print 'Principal paid: $', principalPaid
    balance = round(balance - principalPaid, 2)
    print 'Remaning balance: $', balance



