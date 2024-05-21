from statistics import median
from statistics import mean


NoOfNum = int(input("Enter the numebr of numbers: "))
first_Num = int(input("Enter the first number: "))
numbers = []
numbers.append(first_Num)

for i in range(NoOfNum - 1):
    next_num = int(input("Enter the next number: "))
    numbers.append(next_num)
print(numbers)

Med = median(numbers)
meaner = mean(numbers)
print("The median is ",Med )
print("The mean is ", meaner)