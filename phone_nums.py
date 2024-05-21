def wrapper(f):
    def fun(l):
        # complete the function
        ls = []
        count  = 0
        while count != N :
            nums = str(input("Enter number: "))
            ls.append(nums)
            ls.sort()
            count = count + 1
        for z in ls:
                if z[:2] == "91" and len(z) == 10:
                    print(f"+91 {z[:5]} {z[5:10]}" )
                elif z[:3] == "+91":
                    print(f"{z[:2]} {z[3:8]} {z[8:13]}")
                elif z[:1] == "0":
                    z.removeprefix("0")
                    print(f"+91 {z[1:6]} {z[6:11]}")
                elif z[:2] == "91":
                    print(f"+{z[:2]} {z[2:7]} {z[7:12]}")
    return fun

N = int(input("Enter number of numbers: "))
@wrapper
def sort_phone(l):
    print(*sorted(l), sep='\n')

if __name__ == '__main__':
    l = [input() for _ in range(int(input()))]
    sort_phone(l) 