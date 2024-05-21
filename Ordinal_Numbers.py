numbers = []
for i in range(1,10):
    numbers.append(i)
    if i == 1:
        numbers[0] = "1st"
        print(numbers[0])
    elif i == 2:
        numbers[1] = "2nd"
        print(numbers[1])
    elif i == 3:
        numbers[2] = "3rd"
        print(numbers[2])
    else:
        numbers[i-1] = f"{i}th"
        print(numbers[i-1])