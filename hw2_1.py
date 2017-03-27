#balance - the outstanding balance on the credit card
#annualInterestRate - annual interest rate as a decimal
#monthlyPaymentRate - minimum monthly payment rate as a decimal

#Month: 1
#Minimum monthly payment: 96.0
#Remaining balance: 4784.0

#Monthly interest rate= (Annual interest rate) / 12.0
#Minimum monthly payment = (Minimum monthly payment rate) x (Previous balance)
#Monthly unpaid balance = (Previous balance) - (Minimum monthly payment)
#Updated balance each month = (Monthly unpaid balance) + (Monthly interest rate x Monthly unpaid balance)

#Test Case 1:
#	      balance = 4213
#	      annualInterestRate = 0.2
#	      monthlyPaymentRate = 0.04
#	      
#	      Result Your Code Should Generate:
#	      -------------------
#	      Month: 1
#	      Minimum monthly payment: 168.52
#	      Remaining balance: 4111.89
#	      Month: 2
#	      Minimum monthly payment: 164.48
#	      Remaining balance: 4013.2
#	      Month: 3
#	      Minimum monthly payment: 160.53
#	      Remaining balance: 3916.89

#balance = 4213
total_paid = 0
#annualInterestRate = 0.2
#monthlyPaymentRate = 0.04
mon_rate = annualInterestRate/12.0

for i in range(1,13):
    min_mon_pay = round(monthlyPaymentRate * balance,2)
    unpaid_balance = balance - min_mon_pay
    balance = round(unpaid_balance + mon_rate*unpaid_balance, 2)
    total_paid += min_mon_pay
    #print ("Month: " + str(i))
    #print ("Minimum monthly payment: " + str(min_mon_pay))
    #print ("Remaining balance: " + str(balance))

#print ("Total paid: " + str(total_paid))
print ("Remaining balance: " + str(balance))
