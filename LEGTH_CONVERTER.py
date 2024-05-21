LIF = float(input("EMTER LENGTH IN FEET: "))
LCIM = 30 * LIF
print(f"LENGTH IN CENTIMETERS IS {LCIM}")

mark = int(input("Enter your mark: "))
if mark >= 70:
    grade = "A"
elif mark >= 60:
    grade = "B"
elif mark >= 50:
    grade = "C"
elif mark >= 40:
    grade = "D"
else:
    grade = "F"
print(f"Your grade is {grade}")

average = 0
sum = 0
ls = [10, 20, 30, 40, 50]
for i in range(len(ls)):
    print(f"ls[{i}] = {ls[i]}")
sum = sum + i
average = sum/len(ls)
print(f"The sum is {sum}")
print(f"The average is {average}")