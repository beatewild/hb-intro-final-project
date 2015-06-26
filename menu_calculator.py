#tax = 8.75% #1.0875
#tip = 15%, 20%, 25%

'''
name = raw_input ("What is your name: ")
food_choice = raw_input ("Which food did you eat? ")
drink_choice = raw_input ("What did you drink? ")
tip_choice = raw_input("15 or 20 or 25: Choose the tip in percent: ")

total = ((food[food_choice] + drinks[drink_choice]) * 1.0875) * tip[tip_choice]

print "You have to pay", total, "Dollar - included", tip_choice, "%","tip."
'''

food = {"French Fries":3.50, "Hamburger":5.50, "Hotdog":4.50, "Chicken Salad":9.50, "Pizza":14.00}
drink = {"Soda":1.75, "Coffee":2.50, "Milk Shake":4.25, "Beer":4.50, "Wine":6.50}
tip = {"15":1.15,"20":1.20,"25":1.25}


food_choice_list = []
food_number_list = []
items = []
while(True):
	food_choice = raw_input("Which food did you eat? ") 
	food_number = raw_input("How many? ")
	item = raw_input("Did you eat more food? ")
	food_choice_list.append(food_choice)
	food_number_list.append(food_number)
	if (item == "no"):
		break	
	else:
		items.append(item)

for i in range(len(food_choice_list)):
	food_choice_list[i]=food[food_choice_list[i]]
	print i,"is i"
	print food_choice_list[i],"is food_choice_list[i]"

total_food=0
for e in range(len(food_number_list)):
	print e, "is e"
	print food_number_list[e], "is food_number_list[e]"	


total_food = [float(food_choice_list) * float(food_number_list) for food_choice_list,food_number_list in zip(food_choice_list,food_number_list)]

print "The total of food is ", sum(total_food), "dollars."


drink_choice_list = []
drink_number_list = []
items = []
while(True):
	drink_choice = raw_input("What did you drink? ") 
	drink_number = raw_input("How many? ")
	item = raw_input("Did you have more drinks? ")
	drink_choice_list.append(drink_choice)
	drink_number_list.append(drink_number)
	if (item == "no"):
		break	
	else:
		items.append(item)

for i in range(len(drink_choice_list)):
	drink_choice_list[i]=drink[drink_choice_list[i]]
	print i,"is i"
	print drink_choice_list[i],"is drink_choice_list[i]"

total_drink=0
for e in range(len(drink_number_list)):
	print e, "is e"
	print drink_number_list[e], "is drink_number_list[e]"	


total_drink = [float(drink_choice_list) * float(drink_number_list) for drink_choice_list,drink_number_list in zip(drink_choice_list,drink_number_list)]

print "The total of drinks is ", sum(total_drink), "dollars."

print "The total of your check is", sum(total_food+total_drink), "dollars."



'''


items = []
while(True):
	drink_choice = raw_input("What did you drink? ")
	drink_number = raw_input("How many? ")
	item = raw_input("Did you have more drinks? ")
	if (item == "no"):
		break	
	else:
		items.append(item)

'''





