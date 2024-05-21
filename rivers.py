river = {"Nile": "Egypt", "Ankobra": "Ghana", "Niger": "Niger"}
for river_name,country in river.items():
    print( river_name )
    print( country)
    print(f"The {river_name} runs through {river[river_name]}")



poll = {
    "PAB": "Python", 
    "MIKE": "C++", 
    "CODE": "TypeScript",
    "INNOCENT ZERO": "VBScript",
    "PANTHER": "", 
    "TESLA": "",
    }
for name, language in poll.items():
    if  language:
        print(f"{name}, thank you for responding")
    else:
        print(f"{name}, you are invited to take the poll")

ls = [
  "07895462130",
  "919875641230",
  "9195969878"
  ]
ls.sort()

'''
for i in range(N+1):
nums = int(input())
ls.append(nums)
ls = ls.sort()
'''

for z in ls:
    if z[:2] == "91" and len(z) == 10:
        print(f"+91 {z[:5]} {z[5:10]}" )
    elif z[:3] == "+91":
        print(f"{z[:2]} {z[3:8]} {z[8:13]} ")
    elif z[:1] == "0":
        z.removeprefix("0")
        print(f"+91 {z[1:6]} {z[6:11]} ")
    elif z[:2] == "91":
        print(f"+{z[:2]} {z[2:7]} {z[7:12]} ")
        
