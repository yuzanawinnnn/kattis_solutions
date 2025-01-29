s = input().split(" ")
layout = []
count = [0,0,0,0,0]

for i in range(int(s[0])):
    l = input()
    layout.append(list(l))


for i in range(int(s[0])-1):
    for j in range(int(s[1])-1):
        arr = [layout[i][j], layout[i][j+1], layout[i+1][j], layout[i+1][j+1]]
        if "#" not in arr:
            count[arr.count("X")] = count[arr.count("X")] + 1

for k in range(5):
    print(count[k])
            
            
    
