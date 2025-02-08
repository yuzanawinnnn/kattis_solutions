n = int(input())
name = []

for i in range(n):
    s = input()
    name.append(s)

m = int(input())

for j in range(m):
    s = input().split(" ")
    
    if(s[0] == "leave"):
        name.remove(s[1])
    else:
        name = name[: name.index(s[2])] + [s[1]] + name[name.index(s[2]) :]
    
for k in range(len(name)):
    print(name[k])
    
