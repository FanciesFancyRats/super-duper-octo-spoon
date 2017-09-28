"""
Copyright [yyyy] [name of copyright owner]

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

 http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""
"""
Copyright [yyyy] [name of copyright owner]

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

 http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
    limitations under the License.
"""
balance = raw_input('Please input balance:')
air = raw_input('Please input annual intrest rate: ')
balance = float(balance)
air = float(air)
lowerBound = balance/12.0
upperBound = (balance * (1 + (air/12))**12)/12
upperBound = round(upperBound, 2)
bisection = (lowerBound+upperBound)/2
monthyPayment = bisection
x = 1
n = 0
balanceCheck = balance
#print(lowerBound)
#print(upperBound)
#print(bisection)
#*****************
def yearIntrest(monthlyPayment):
 x = 1
 monthlyPayment = float(monthlyPayment)
 balanceCheck = balance
 while ((x < 12) & (balanceCheck > 0)):
  intrestPaid = round(((air/12.0)*balanceCheck),2)
  #print(intrestPaid)
  principalPaid = round((monthlyPayment - intrestPaid), 2)
  #print(principalPaid)
  balanceCheck = round((balanceCheck - principalPaid),2)
  #print(remainingBalance)
  x = x + 1
 return balanceCheck;
 

 
while((abs(balanceCheck) > 0.2) and (n < 999)):
 n = n+1
 balanceCheck = balance
 testLowerBound = yearIntrest((lowerBound + bisection)/2)
 testUpperBound = yearIntrest((upperBound + bisection)/2)
 if(abs(testUpperBound) <= abs(testLowerBound)):
  lowerBound = bisection
  print("We went up")
  print(testUpperBound)
  #upperBound = upperBound
 if(abs(testUpperBound) > abs(testLowerBound)):
 	 upperBound = bisection
 	 #lowerBoud = lowerBound
 	 print("We went down")
 	 print(testLowerBound)
 bisection = (lowerBound + upperBound)/2
 #print(bisection)
 monthlyPayment = bisection
 x = 1
 #print(upperBound)
 while ((x < 12) & (balanceCheck > 0)):
  intrestPaid = round(((air/12.0)*balanceCheck),2)
  #print(intrestPaid)
  principalPaid = round((monthlyPayment - intrestPaid), 2)
      #print(principalPaid)
  balanceCheck = round((balanceCheck - principalPaid),2)
  #print(remainingBalance)
  x = x + 1
  
#print(balanceCheck)
monthlyPayment = round((monthlyPayment), 2)
if (n >= 999):
 print('We could not find a solution')
if (n < 999):
 print('RESULTS')
 print(monthlyPayment)
 print(x)
 print(balanceCheck)