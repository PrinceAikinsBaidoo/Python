from decimal import Decimal, getcontext 
  
getcontext().prec = 6

arr = [1,1,0,-1,-1]
lenght = len(arr)
pos = 0.000000
neg = 0.000000
zero = 0.000000
for i in arr:
    if i < 0:
        neg = neg + 1.000000
    elif i == 0:
        zero = zero + 1.000000
    else:
        pos = pos + 1.000000
neg_rat = float(neg/lenght)
pos_rat = float(pos/lenght)
ze_rat = zero/lenght
res = Decimal()

'''
print(str(neg_rat) + "00000")
print(str(pos_rat) + "00000")
print(str(ze_rat)+ "00000")
'''

