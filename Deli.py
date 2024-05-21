sandwich_orders = []
order1 = input("Enter an order for your sandwich: ")
sandwich_orders.append(order1)

def orders(input):

    next_order = input("Enter the next order Or Enter quit to end.\n >> ")
    while next_order != "quit":
        sandwich_orders.append(next_order)

orders(input)

finished_sandwiches = []
for sandwich in sandwich_orders:
    print(f"I made your {sandwich} sandwich")
    finished_sandwiches.append(sandwich)
print("\n.....Below are all sandwiches that have been made......")
for finished_sandwich in finished_sandwiches:
    print(finished_sandwich)