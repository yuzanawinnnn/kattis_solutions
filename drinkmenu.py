s = input().split(" ")
menu = []
name = {}

for i in range(int(s[0])):
    m = input()
    menu.append(m)
    
for j in range(int(s[1])):
    n = input()
    if(n not in name.keys()):
        name[n] = 1
    else:
        name[n] = name[n] + 1
    
    print(menu[name[n] - 1])
