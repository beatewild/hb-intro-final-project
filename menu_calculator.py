#tax = 8.75% #1.0875
#tip = 15%, 20%, 25%

#name = raw_input ("What is your name: ")
#food_choice = raw_input ("Which food did you eat? ")
#drink_choice = raw_input ("What did you drink? ")
#tip_choice = raw_input("15 or 20 or 25: Choose the tip in percent: ")
#total = ((food[food_choice] + drinks[drink_choice]) * 1.0875) * tip[tip_choice]
#print "You have to pay", total, "Dollar - included", tip_choice, "%","tip."


food = {"fries":3.50, "hamburger":5.50, "hotdog":4.50, "burrito":6.75, "salad":9.50, "pizza":14.00, "tiramisu":6.25, "icecream":4.75}
drink = {"soda":1.75, "tea":2.25, "coffee":2.75, "milkshake":4.25, "beer":4.50, "wine":6.50, "gin":5.75}
tip = {"15":1.15,"20":1.20,"25":1.25}


food_choice_list = []
food_number_list = []
items = []
while(True):
	food_choice = raw_input("Which food did you eat? ").lower() 
	food_choice = food_choice.replace(" ","")
	if (food_choice not in food):
		food_choice = raw_input ("This is no food from our menu. We have fries, hamburger, hotdog, burrito, salad, pizza, tiramisu, icecream. What did you eat? ").lower()
		food_choice = food_choice.replace(" ","")
	food_number = raw_input("How many? ").lower()
	food_number = food_number.replace(" ","")
	item = raw_input("Did you eat more food? yes or no: ").lower()
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

#print "The total of food is", sum(total_food), "dollars."


drink_choice_list = []
drink_number_list = []
items = []
while(True):
	drink_choice = raw_input("What did you drink? ").lower()
	drink_choice = drink_choice.replace(" ","")
	if (drink_choice not in drink):
		drink_choice = raw_input ("This is no drink from our menu. We have soda, tea, coffee, milkshake, beer, wine, gin. What did you drink? ").lower()
		drink_choice = drink_choice.replace(" ","")
	drink_number = raw_input("How many? ").lower()
	drink_number = drink_number.replace(" ","")
	item = raw_input("Did you have more drinks? yes or no: ").lower()
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

#print "The total of drinks is", sum(total_drink), "dollars."

total_net = sum(total_food+total_drink)

tip_choice = raw_input("Choose the tip: 15 or 20 or 25 percent: ")
tip_choice = tip_choice.replace(" ","")
if (tip_choice not in tip):
	tip_choice = raw_input ("This is not a tip option. Please choose 15 or 20 or 25: ")
	tip_choice = tip_choice.replace(" ","")

#print "The total of your check is", total_net, "dollars."

total_tax = total_net * 1.0875


#print "The total is", total_net, "plus 8.75 percent tax is", total_tax, "Dollars."

total_tax_tip = total_tax * tip[tip_choice]

print "You have to pay", "%.2f" % total_tax_tip, "Dollars. 8.75","%","tax and", tip_choice, "%","tip included. Thanks for your visit."



