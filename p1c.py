balance = raw_input('Please enter the balance: ')
balance = float(balance)
air = raw_input('Please enter the annual intrest rate: ')
air = float(air)
tol = 10
monthlyPayment = 0
x = 1
balanceCheck = balance
lowerBound = balance/12
lowerBound = round(lowerBound, 2)
upperBound = (balance * (1 + (air/12.0))**12.0)/12.0
upperBound = round(upperBound, 2)
bisection = (upperBound + lowerBound)/2
bisection = round(bisection)
print(lowerBound)
print(upperBound)
print(bisection)
print('********')

while (abs(balanceCheck) > tol):

#while (balanceCheck > 0):
    monthlyPayment = monthlyPayment + tol
    monthlyPayment = round(monthlyPayment, 2)
    balanceCheck = balance
    x = 0
    while ((x < 12) and (balanceCheck > 0)):
        intrestPaid = (air/12)*balanceCheck
        intrestPaid = round(intrestPaid, 2)
        principalPaid = monthlyPayment - intrestPaid
        principalPaid = round(principalPaid, 2)
        balanceCheck = balanceCheck - principalPaid
        balanceCheck = round(balanceCheck,2)
        x = x + 1
print(monthlyPayment)
print(x)
print(balanceCheck)