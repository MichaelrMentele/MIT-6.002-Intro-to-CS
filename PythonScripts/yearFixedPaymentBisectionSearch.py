#Inputs
ibalance = 320000
annualInterestRate = 0.20

#Initialized
month = 0
epsilon = 0.01

#Dependents
monthlyRate = annualInterestRate/12
balance = ibalance
lwrBound = balance/12
uprBound = (balance * (1+ monthlyRate)**12)/12
payment = (uprBound + lwrBound)/2

while  True:
    print 'Month: ' + str(month)
    month += 1
    
    print balance
    payment = (uprBound + lwrBound)/2
    balance = balance - payment    
    balance = balance + monthlyRate * balance
    
    if month == 12 and balance > 0 + epsilon:
        lwrBound = payment
        print payment
    
        balance = ibalance
        month = 0
        
    elif month == 12 and balance < 0 - epsilon:
        uprBound = payment
        print payment
        
        balance = ibalance
        month = 0
        
    elif month == 12 and abs(balance) <= epsilon:
        break
    


print 'Lowest Payment: ' + str(round(payment, 2))
