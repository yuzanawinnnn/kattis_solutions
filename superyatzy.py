num = []
count = []

s = input().split(" ")
for i in range(int(s[0])):
    n = int(input())
    if n not in num:
        num.append(n)
        count.append(1)
    else:
        count[num.index(n)] = count[num.index(n)] + 1

count.remove(max(count))
if(int(s[1]) >= sum(count)):
    print("Ja")
else:
    print("Nej")
    
