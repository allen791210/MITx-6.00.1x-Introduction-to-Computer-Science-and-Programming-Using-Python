def item_order(order):
    numSalad = 0
    numHamburger = 0
    numWater = 0
    s= order.split()

    for i in s:
        if i == 'salad':
            numSalad += 1

        elif i == 'hamburger':
            numHamburger += 1

        elif i == 'water':
            numWater += 1
            
    result = "salad:"+ str(numSalad) + " hamburger:"+ str(numHamburger)+ " water:"+ str(numWater)
    return result

#order = "salad water hamburger salad hamburger"
#s = item_order(order)
#print s
