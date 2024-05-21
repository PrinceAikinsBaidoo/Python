# Enter your code here. Read input from STDIN. Print output to STDOUTa 
a = int(input("Number of queries: "))
diction = dict()
names = list()
for i in range(a):
    NN = list(input("Name & Number: ").split(' '))
    diction.update({NN[0]: NN[1]})

for i in range(a):
    nam = (input("Name to find: "))
    names.append(nam)


for i in range(len(names)):
    for key, value in diction.items():
        if names[i] not in diction.keys():
            print(f"{names[i]}=Not found")
            break
        elif names[i] == key:
            print(f"{key}={value}")
        