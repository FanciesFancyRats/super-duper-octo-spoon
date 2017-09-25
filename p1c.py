balance = raw_input('Please input your balance: ')
air = raw_input('Please input your annual intrest rate: ')
balance = float(balance)
air = float(air)
#print(type(balance))
monthlyPayment = 0
intrestPaid = ((air/12)*balance)
principalPaid = 0.0
x = 0
x = int(x)
balanceCheck = balance
#find upper bound
upperBound = (balance*(1+(air/12))**12.0)/12.0
#find lower bound
lowerBound = balance/12
#bisection = ((upperBound+lowerBound)/2)
#monthlyPayment = bisection
while ((balanceCheck > 0.2) or (balanceCheck < 0.2)):
 #print('**Start**')
 bisection = ((upperBound + lowerBound)/2)
 bisection = round(bisection, 2)
 #print(upperBound)
 #print(lowerBound)
	#adjust bounds
	#monthlyPayment = monthlyPayment + .01
 balanceCheck = balance
 x = 0
 while ((balanceCheck != 0) and (x < 12)):
	 #test bounds
	 #print(bisection)
	 intrestPaid = ((air/12)*balanceCheck)
	 intrestPaid = round(intrestPaid, 2)
	 principalPaid = bisection - intrestPaid
	 balanceCheck = balanceCheck - principalPaid
	 x = x + 1
	 #print(balanceCheck)
	 #print(principalPaid)
	 #print(x)
	 #print(upperBound)
	 #print(lowerBound)
	 #print('*****')
	 #print(upperBound - bisection)
	 #print('*******')
	 #print(bisection - lowerBound)
 if((upperBound - bisection) >= (bisection - lowerBound)):
	 lowerBound = bisection
	 print('line 43')
 if((upperBound - bisection) < (bisection - lowerBound)):
	 upperBound = bisection
	 print('line 46')
print ('Number of months: ')
print (x)
print ('Balance: ')
balanceCheck = round(balanceCheck, 2)
print (balanceCheck)
print ('Monthly payment: ')
print (bisection)