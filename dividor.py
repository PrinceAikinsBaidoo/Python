a = int(input("Enter the dividend: "))
b = int(input("Enter the divisor: "))
c = 0
f = (a % b)
d = a - f
e = 0
while  c != d:
    e = e + 1
    c = c + b
print(f"\nThe quotient is {e}")
print(f"The remainder is: {f}")
'''
z = d + 1
for i in range(1, z):
    if d % i == 0:
        lag = i
print(lag)
'''