toppings = []
topping = input("Enter a topping to be added to your pizza: ")
print(f"Adding {topping} to your pizza. \n ")

prompt = "Enter the next topping Or enter quit to end: "
next_top = input(prompt)
print(".....\n.........")
print(f"Adding {next_top} to your pizza.")
while next_top != "quit":
    next_top = input(prompt)
    if next_top == "quit" or next_top == "Quit":
        break
    print(".....\n.........")
    print(f"Adding {next_top} to your pizza.\n" )