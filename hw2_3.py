# balance - the outstanding balance on the credit card
# annualInterestRate - annual interest rate as a decimal


# Lowest Payment: 180 

#Monthly interest rate = (Annual interest rate) / 12.0
#Monthly unpaid balance = (Previous balance) - (Minimum fixed monthly payment)
#Updated balance each month = (Monthly unpaid balance) + (Monthly interest rate x Monthly unpaid balance)

#def Paying_Debt_Off(balance, annualInterestRate):
#payment = balance/12
#payment = payment - (payment%10) +10

#balance = 999999
#annualInterestRate = 0.18
mon_interest_rate = annualInterestRate/12

high = (balance*(1+mon_interest_rate)**12)/12
low = balance/12

payment = (low+high)/2
epsilon = 0.01
updated_balance = balance

while (abs(updated_balance) > epsilon):
    updated_balance = balance
    payment = (low+high)/2
    
    for i in range(12):
        mon_unpaid_balance = updated_balance - payment
        updated_balance = mon_unpaid_balance*(1+ mon_interest_rate)

    #print payment
    #print updated_balance
  
    if updated_balance < 0:
        high = payment
        
    else: 
        low = payment
     
print ("Lowest Payment: %.2f" % payment)


