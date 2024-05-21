name = input("Enter your name: " )
dicti = {}
# Maths = input("Enter the subject name:" )
subjects = ["Circuit Theory", "Information Technology", "Com. Skills", "Structured Programming","Discrete Mathematics", "Pure Mathematics" ]
for subject in subjects:
    sc = input(f"Enter score for {subject}: ")
    score = int(sc)
    dicti[subject] = score
print(f" \n Displaying scores of {name} in the various subjetcs \n")
print(dicti)