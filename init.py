x = int(input())
y = int(input())
z = int(input())
n = int(input())
sl = []

for i in range(x + 1):
    pass
    for j in range(y + 1):
        for k in range(z + 1):
            if k + j + i != n and len(sl) <= 3:
                sl.append([i,j,k])
print(sl)

s = 'hello' + 'world\n'
s = s * 4
print(s)

