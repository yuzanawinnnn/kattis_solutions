n = int(input())
loc = {}
for i in range(n):
    name = input()
    s = input()
    
    if(s in loc.keys()):
        loc[s] = loc[s] + 1
    else:
        loc[s] = 1

for keys,values in loc.items():
    print(keys, values)

