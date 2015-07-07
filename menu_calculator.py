food = {"fries":[3.50, 110], "hamburger":[5.50, 550], "hotdog":[4.50, 315], "burrito":[6.75, 410], "salad":[9.50, 150], "pizza":[9.75, 1680], "tiramisu":[6.25, 590], "icecream":[4.75, 70]}
drink = {"soda":[1.75, 180], "tea":[2.25,35], "coffee":[2.75,60], "milkshake":[4.25,490], "beer":[4.00,150], "wine":[5.25,120], "gin":[5.75,90]}
tip = {"15":1.15,"20":1.20,"25":1.25}



print " 				"
print "Welcome to the Menu Calculator! Today we offer:"
print "Fries 			3.50 $"
print "Hamburger 		5.50 $" 
print "Hotdog 			4.50 $"
print "Burrito 		6.75 $" 
print "Salad 			8.50 $" 
print "Pizza 			9.75 $" 
print "Tiramisu 		6.25 $" 
print "Icecream 		4.75 $"

food_choice_list = []
food_number_list = []
items = []
while(True):
	food_choice = raw_input("Which food do you want to eat? ").lower() 
	food_choice = food_choice.replace(" ","")
	if (food_choice not in food):
		food_choice = raw_input ("This is not an item from our menu. We have fries, hamburger, hotdog, burrito, salad, pizza, tiramisu, icecream. What do you choose? ").lower()
		food_choice = food_choice.replace(" ","")
	food_number = raw_input("How many? ").lower()
	food_number = food_number.replace(" ","")
	item = raw_input("Do you want more food? 'yes' or 'no': ").lower()
	item = item.replace(" ","")
	food_choice_list.append(food_choice)
	food_number_list.append(food_number)
	if (item == "no"):
		break
	elif (item == "yes"):
		items.append(item)
	else:
		item = raw_input ("What was that? Please give me a 'yes' or a 'no': ").lower()
		item = item.replace(" ","")
		if (item == "no"):
			break
		elif (item == "yes"):
			items.append(item)

for i in range(len(food_choice_list)):
	food_choice_list[i]=food[food_choice_list[i]]


price_list_food = list(food_choice_list)
calorie_list_food = list(food_choice_list)


price_number_food = list(food_number_list)
calorie_number_food = list(food_number_list)


for i in range(len(price_list_food)):
	price_list_food[i]=price_list_food[i][0]


for e in range(len(calorie_list_food)):
	calorie_list_food[e]=calorie_list_food[e][1]


total_food = [float(price_list_food) * float(price_number_food) for price_list_food,price_number_food in zip(price_list_food,price_number_food)]

calorie_food_total = [int(calorie_list_food) * int(calorie_number_food) for calorie_list_food,calorie_number_food in zip(calorie_list_food,calorie_number_food)]
sum_calorie_food = sum(calorie_food_total)


print " 				"
print "These are our drinks:"
print "Soda 			1.75 $"
print "Tea 			2.25 $" 
print "Coffee 			2.75 $" 
print "Milkshake 		4.25 $" 
print "Beer 			4.00 $" 
print "Wine 			5.25 $" 
print "Gin 			5.75 $"


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
		item = raw_input ("What was that? Please give me a 'yes' or a 'no': ").lower()
		item = item.replace(" ","")
		if (item == "no"):
			break
		elif (item == "yes"):
			items.append(item)


for i in range(len(drink_choice_list)):
	drink_choice_list[i]=drink[drink_choice_list[i]]


price_list_drink = list(drink_choice_list)
calorie_list_drink = list(drink_choice_list)


price_number_drink = list(drink_number_list)
calorie_number_drink = list(drink_number_list)


for i in range(len(price_list_drink)):
	price_list_drink[i]=price_list_drink[i][0]


for e in range(len(calorie_list_drink)):
	calorie_list_drink[e]=calorie_list_drink[e][1]


total_drink = [float(price_list_drink) * float(price_number_drink) for price_list_drink,price_number_drink in zip(price_list_drink,price_number_drink)]


calorie_drink_total = [int(calorie_list_drink) * int(calorie_number_drink) for calorie_list_drink,calorie_number_drink in zip(calorie_list_drink,calorie_number_drink)]
sum_calorie_drink = sum(calorie_drink_total)


total_net = sum(total_food+total_drink)

print " 				"
tip_choice = raw_input("Choose the tip: 15 or 20 or 25 percent: ")
tip_choice = tip_choice.replace(" ","")
if (tip_choice not in tip):
	tip_choice = raw_input ("This is not a tip option. Please choose 15 or 20 or 25: ")
	tip_choice = tip_choice.replace(" ","")


total_tax = total_net * 1.0875
tax_only = total_tax - total_net

total_tax_tip = total_tax * tip[tip_choice]
tip_only = total_tax_tip - total_tax


print "													"
print "													"
print "----           		RECEIPT			----"
print "													"
print "----         		MEAL 	- $", "%.2f" % total_net,"	----"
print "----		8.75","%"," TAX 	- $", "%.2f" % tax_only,"	----"
print "----		", tip_choice, "%", "	TIP 	- $", "%.2f" % tip_only,"	----"
print "----        		TOTAL 	- $", "%.2f" % total_tax_tip,"	----"
print "													"
print "----		You have to pay", "%.2f" % total_tax_tip, "Dollars. 	----"
print "													"
sum_calorie_all = sum_calorie_food+sum_calorie_drink
print "***		This meal has", sum_calorie_all, "calories."
print "***		Calories in food: 	", sum_calorie_food
print "***		Calories in drinks: 	", sum_calorie_drink
print "					"
print "$$$ 		Anyway - enjoy your meal! Thanks for your purchase! 	$$$"
print "					"
print "					"



