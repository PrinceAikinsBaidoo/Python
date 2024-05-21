n = int(input())
arr = map(int, input().split())

maxm = max(arr)
for i in arr:
    if i == maxm:
        del arr[0]
print(maxm)

'''
for i in ls:
    if i == maxm:
        ls.remove(i)
nl =len(ls)
print(ls)
'''
'''
ls_lenght = len([arr]) + 1
for i in range(ls_lenght) :
    if ls[i-1] > ls[i]:
        largest = {ls[i]}

for i in ls :
    if ls[i] == largest:
         ls.pop(i)

'''