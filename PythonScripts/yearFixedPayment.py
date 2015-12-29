#Inputs
ibalance = 4773
annualInterestRate = 0.20

#Initialized
month = 0
payment = 10
total = 0

#Dependents
monthlyRate = annualInterestRate/12
balance = ibalance

while  balance >= 0:
    #print 'Month: ' + str(month)
    month += 1
    
    print balance
    balance = balance - payment    
    balance = balance + monthlyRate * balance
    
    if month >= 12 and balance > 0:
        payment +=10
        print payment
        balance = ibalance
        month = 0


print 'Lowest Payment: ' + str(payment)
