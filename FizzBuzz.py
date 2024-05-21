# Write your code
for i in range(101):
  if i == 0:
    continue
  if i % 3 == 0 and i % 5 == 0:
    print("FizzBuzz")
  elif i % 5 == 0:
    print("Buzz")
  elif i % 3 == 0:
    print("Fizz")
  else:
    print(i)