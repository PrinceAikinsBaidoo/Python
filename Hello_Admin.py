usernames = ["admin", "Pab", "Tessa", "Mike", "Code"]
for username in usernames:
    if username == 'admin':
        print(f"Hello {username}, would you like to see a status report? ")
    else:
        print(f"Hello {username}, thank you for logging in again.")

usernames.clear()
if usernames == []:
    print("We need to find some users")
