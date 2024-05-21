ls_factors = []
prime_factor = []
factors =[]
a = int(input("Enter numbers separated by spaces: "))
v = int(input("Enter numbers separated by spaces: "))
ls_factors.append([a,v])
for b in ls_factors:
    for c in range(1,b):
        if b % c == 0:
            factors.append(c)
    print(c)
    
    '''
for factor in ls_factors:
    for num_in_factor in range(1, factor + 1):
        if factor % num_in_factor == 0:
            fac_of_factor = fac_of_factor + 1
    if fac_of_factor == 2:
        prime_factor.append(factor)
    #prime_factor.sort(reverse=True)
print(prime_factor)
'''