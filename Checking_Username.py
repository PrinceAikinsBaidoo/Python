current_users = ["Pab", "Tessa", "Mike", "Ashitey", "Twig"]
lc_users = []
for c_user in current_users:
    c_user = c_user.lower()
    lc_users.append(c_user)
new_users = ["Pab", "Tessa", "Panther", "Jvo_James", "Peter"]
for n_user in new_users:
    if n_user.lower() in lc_users:
        print(f"{n_user} is already in use. \n You need to enter a new username.")
    else:
        print(f"{n_user} is available.")



current_users = ["Pab", "Tessa", "Mike", "Ashitey", "Twig"]
lc_users = []
for c_user in current_users:
    c_user = c_user.lower()
    lc_users.append(c_user)
print(f"Current Users: {lc_users}")
new_users = ["Pab", "Tessa", "Panther", "Jvo_James", "Peter"]
for n_user in new_users:
    if n_user.lower() in lc_users:
        print(f"{n_user} is already in use. \n You need to enter a new username.")
    else:
        print(f"{n_user} is available.")