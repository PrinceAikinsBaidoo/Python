def tickets():
    age = int(input("Enter your age: "))
    if age < 3:
        print("Ticket is free")
    elif age <= 12:
        print("Ticket is $10")
    else:
        print("Ticket is $15")

    prompt = "Do you want to check for a different age:\n1. Yes\n2. No\n>> "
    ans = input(prompt)

    while ans == "Yes" or ans == "yes" or ans == "YES" or int(ans) == 1 :
        tickets()
    else:
        pass
tickets()



