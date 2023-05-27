count, T = map(int,input().split(" "))
line = list(map(int,input().split(" ")))
total = 0
i = 0
ans = 0
c = 0
flag = False
while flag == False and i < count:
    total = total + line[i]
    if(total > T):
        flag = True
    else:
        c = c + 1
    i = i + 1
print(c)
