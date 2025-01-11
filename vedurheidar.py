v = int(input())
n = int(input())
road = []

for i in range(n):
    r = input()
    road.append(r)
    
for j in range(n):
    s = road[j].split(" ")
    if(int(s[1]) >= v):
        print(s[0], "opin")
    else:
        print(s[0], "lokud")
