num_of_fib = int(input("Enter the number of fibonacci numbers you want: "))
fib = [0, 1]
num1 = 0
num2 = 1
print("Fibonacci sequence:")
while len(fib) <= num_of_fib:
    num2 = num1 + num2
    num1 = num2 - num1
    fib.append(num2)
for i in fib:
    print(i)