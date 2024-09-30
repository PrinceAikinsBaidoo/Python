print("What do you have?\n1. I have my average already but it is per 100.\n2. I have individual subject scores.")
i = int(input("Enter an option:\t"))
try:
    if i == 1:
        print("Great. This is gonna be peazy easy.")
        score = float(input("Enter your per 100 score without the percentage:\t"))
        gpa_4 = (score/100) * 4.0
    else:
        print("Aight. You have to enter your scores without the percentages.")
        subject_scores = list(map(int, input("Enter your scores, separated by comma only: ").split(",")))
        j = 0
        total_score = 0
        for i in subject_scores:
            j = j + 1
            total_score += i
        gpa_4 = (total_score/(j * 100)) * 4.0
    print(f"Your per 4.0 gpa is {gpa_4:.2f}")
except:
    print("Invalid input, try again.")
