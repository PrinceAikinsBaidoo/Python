# Enter your code here. Read input from STDIN. Print output to STDOUT
T = int(input())
let_pos = 0
let_odd = ""
let_even = ""
ls = list()
for i in range(T):
    S = input().split(' ')
    for word in S:
        n = len(word)
        for i in range(2,n+2):  
            if i % 2 == 1:
                let_even = word[i]
            else:
                let_odd = word[i]
            #let_pos += 1
        print(f"{let_even} {let_odd}")
    '''
        while let_pos < n:
            let_even = let_even, word[e]
            let_odd = let_odd, word[o]
            e += 2
            o += 2
            let_pos += 1

    print(let_even, let_odd)
'''
