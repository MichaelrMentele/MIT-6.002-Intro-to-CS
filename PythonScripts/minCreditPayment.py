#Initialize Variables
#Inputs
balance = 4213
annualInterestRate = 0.2
monthlyPaymentRate = 0.04

#Initialized
month = 1
payment = 0
total = 0

#Calculated
monthlyInterest = annualInterestRate/12

while month <= 12:
    print 'Month: ' + str(month)
    month += 1
    
    min_month_pay = monthlyPaymentRate * balance
    total += min_month_pay
    print 'Minimum monthly payment: ' + str(round(min_month_pay, 2))
    
    payment = monthlyPaymentRate * balance
    balance = balance - payment    
    balance = balance + monthlyInterest * balance
    print 'Remaining balance: ' + str(round(balance, 2))
    
print 'Total paid: ' + str(round(total, 2))
print 'Remaining balance: ' + str(round(balance, 2))