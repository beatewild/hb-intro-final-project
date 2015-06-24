"""

French Fries - $3.50 Hamburger - $5.50 Hotdog - $4.50 Burrito - $6.25 Chicken Salad - $9.50

Soda - $1.75 Coffee - $2.50 Milk Shake - $4.25 Beer - $4.50 Wine - $6.50

The tipp options are: 15%, 20%, 25%

"""

#Making a list of the items plus price
#What and how much had the customer ordered?
#Create a function to calculate the sum
#Calculate tax
#Calculate tip
#Add tax and tip


food = {"French Fries":3.50, "Hamburger":5.50, "Hotdog":4.50, "Chicken Salad":9.50}
drinks = {"Soda":1.75, "Coffee":2.50, "Milk Shake":4.25, "Beer":4.50, "Wine":6.50}
tip = {"15":1.15,"20":1.20,"25":1.25}

#tax = 8.75% #1.0875
#tip = 15%, 20%, 25%

'''
name = raw_input ("What is your name: ")
food_choice = raw_input ("Which food did you eat? ")
drink_choice = raw_input ("What did you drink? ")
tip_choice = raw_input("15 or 20 or 25: Choose the tip in percent: ")
'''



food_choice = raw_input("Which food did you eat? ") 
drink_choice = raw_input ("What did you drink? ")
tip_choice = raw_input("15 or 20 or 25: Choose tip in percent: ")


total = ((food[food_choice] + drinks[drink_choice]) * 1.0875) * tip[tip_choice]

print "You have to pay", total, "Dollar - included", tip_choice, "%","tip."





