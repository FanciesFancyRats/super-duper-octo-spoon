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
solved == False

print lowerBound
print upperBound


while(solved == False):
    #we are here trying to build the loop that test the monthly payment
    payment = (lowerBound + upperBound) / 2
    i = 0
    testBalance = balance
        while(i < 12) and (testBalance > 0):

