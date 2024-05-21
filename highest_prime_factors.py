#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    t = int(input().strip())
    ls_factors = list()
    fac_of_factor = 0
    prime_factor = []

    for t_itr in range(t):
        n = int(input().strip())
        
        for i in range(1,n+1):
            if n % i == 0:
                ls_factors.append(i)
        break

        if len(ls_factors) == 2:
            print(n)
        else:
            for factor in ls_factors:
                for num_in_factor in range(1, factor + 1):
                    if factor % num_in_factor == 0:
                        fac_of_factor = fac_of_factor + 1
                if fac_of_factor == 2:
                    prime_factor.append(factor)
            prime_factor.sort(reverse=True)
            print(prime_factor)
            





