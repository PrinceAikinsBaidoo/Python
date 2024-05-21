fav_fruits = []
fruits = input("Enter your three of your favorite fruits, (separate with a comma): ")
fruits.split(',')
fruits.rstrip()
fav_fruits.append(fruits)
print(fav_fruits)


requested_toppings = ["pepper", "cheese", "Mushrooms"]
for requested_topping in requested_toppings:
    if requested_topping == "cheese":
        print(f"{requested_topping} is out of stock now")
    else:
        print(f"Adding {requested_topping}")
        print("Adding",requested_topping)
print(" \nFininished making your pizza")

