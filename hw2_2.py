# balance - the outstanding balance on the credit card
# annualInterestRate - annual interest rate as a decimal


# Lowest Payment: 180 

#Monthly interest rate = (Annual interest rate) / 12.0
#Monthly unpaid balance = (Previous balance) - (Minimum fixed monthly payment)
#Updated balance each month = (Monthly unpaid balance) + (Monthly interest rate x Monthly unpaid balance)

#def Paying_Debt_Off(balance, annualInterestRate):
#balance = 320000000
#annualInterestRate = 0.2
#import time
#start = time.clock()
payment = balance/12
payment = payment - (payment%10) +10
mon_interest_rate = annualInterestRate/12
    
while (True):
    updated_balance = balance

    for i in range(12):
        mon_unpaid_balance = updated_balance - payment
        updated_balance = mon_unpaid_balance + mon_unpaid_balance*mon_interest_rate

    if updated_balance < 0:
        break
    else:
        payment += 10
     
#return payment
#payment = Paying_Debt_Off(4773, 0.2)
print ("Lowest Payment: %d" % payment)

#end = time.clock()
#time = end - start
#print time
