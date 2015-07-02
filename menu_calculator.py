#tax = 8.75% #1.0875
#tip = 15%, 20%, 25%

food = {"fries":3.50, "hamburger":5.50, "hotdog":4.50, "burrito":6.75, "salad":9.50, "pizza":14.00, "tiramisu":6.25, "icecream":4.75}
drink = {"soda":1.75, "tea":2.25, "coffee":2.75, "milkshake":4.25, "beer":4.50, "wine":6.50, "gin":5.75}
tip = {"15":1.15,"20":1.20,"25":1.25}


name = raw_input ("Welcome to the Menu Calculator! What is your name? ")

food_choice_list = []
food_number_list = []
items = []
while(True):
	food_choice = raw_input("Which food do you want to eat? ").lower() 
	food_choice = food_choice.replace(" ","")
	if (food_choice not in food):
		food_choice = raw_input ("This is not a food from our menu. We have fries, hamburger, hotdog, burrito, salad, pizza, tiramisu, icecream. What do you choose? ").lower()
		food_choice = food_choice.replace(" ","")
	food_number = raw_input("How many? ").lower()
	food_number = food_number.replace(" ","")
	item = raw_input("Did you want more food? 'yes' or 'no': ").lower()
	item = item.replace(" ","")
	food_choice_list.append(food_choice)
	food_number_list.append(food_number)
	if (item == "no"):
		break
	elif (item == "yes"):
		items.append(item)
	else:
		item = raw_input ("What was that? Give me a 'yes' or a 'no': ").lower()
		item = item.replace(" ","")
		if (item == "no"):
			break
		elif (item == "yes"):
			items.append(item)
		
		

for i in range(len(food_choice_list)):
	food_choice_list[i]=food[food_choice_list[i]]


total_food = [float(food_choice_list) * float(food_number_list) for food_choice_list,food_number_list in zip(food_choice_list,food_number_list)]


drink_choice_list = []
drink_number_list = []
items = []
while(True):
	drink_choice = raw_input("What do you want to drink? ").lower()
	drink_choice = drink_choice.replace(" ","")
	if (drink_choice not in drink):
		drink_choice = raw_input ("This is not a drink from our menu. We have soda, tea, coffee, milkshake, beer, wine, gin. What do you want? ").lower()
		drink_choice = drink_choice.replace(" ","")
	drink_number = raw_input("How many? ").lower()
	drink_number = drink_number.replace(" ","")
	item = raw_input("More drinks for you? 'yes' or 'no': ").lower()
	item = item.replace(" ","")
	drink_choice_list.append(drink_choice)
	drink_number_list.append(drink_number)
	if (item == "no"):
		break
	elif (item == "yes"):
		items.append(item)
	else:
		item = raw_input ("What was that? Give me a 'yes' or a 'no': ").lower()
		item = item.replace(" ","")
		if (item == "no"):
			break
		elif (item == "yes"):
			items.append(item)

for i in range(len(drink_choice_list)):
	drink_choice_list[i]=drink[drink_choice_list[i]]


total_drink = [float(drink_choice_list) * float(drink_number_list) for drink_choice_list,drink_number_list in zip(drink_choice_list,drink_number_list)]


total_net = sum(total_food+total_drink)

tip_choice = raw_input("Choose the tip: 15 or 20 or 25 percent: ")
tip_choice = tip_choice.replace(" ","")
if (tip_choice not in tip):
	tip_choice = raw_input ("This is not a tip option. Please choose 15 or 20 or 25: ")
	tip_choice = tip_choice.replace(" ","")


total_tax = total_net * 1.0875
tax_only = total_tax - total_net


total_tax_tip = total_tax * tip[tip_choice]
tip_only = total_tax_tip - total_tax


'''
print name+ ", you have to pay", "%.2f" % total_tax_tip, "Dollars, including 8.75","%","tax and", tip_choice, "%","tip. Thanks for your visit."
'''

print "													"
print "----           		RECEIPT			----"
print "													"
print "----         		MEAL 	- $", "%.2f" % total_net,"	----"
print "----		8.75","%"," TAX 	- $", "%.2f" % tax_only,"	----"
print "----		", tip_choice, "%", "	TIP 	- $", "%.2f" % tip_only,"	----"
print "----        		TOTAL 	- $", "%.2f" % total_tax_tip,"	----"
print "													"
print "Thanks for your visit,", name
print "													"


