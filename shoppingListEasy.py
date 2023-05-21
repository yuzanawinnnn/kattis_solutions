line = input()
line = line.split(" ")
shop = {}
total = 0
arr =[]
for i in range(int(line[0])):
    s = input()
    s = s.split(" ")
    for j in range(int(line[1])):
        if(s[j] not in shop):
            shop[s[j]] = 1
        else:
            shop[s[j]] = shop[s[j]] +1
for name, count in shop.items():  
    if count == int(line[0]):
        total = total +1
        arr.append(name)
print(total)  
arr.sort()
for k in arr:
    print(k)
