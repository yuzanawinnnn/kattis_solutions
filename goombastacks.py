n = int(input())
goomba = 0
flag = True
for i in range(n):
    s = input().split(" ")
    goomba = goomba + int(s[0])
    if goomba < int(s[1]):
        flag = False
        break

if(not flag):
    print("impossible")
else:
    print("possible")
