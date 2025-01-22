s = input()
s = s.split(" ")
mine = []
count = 0
for i in range(int(s[0])):
    m = input()
    m = list(m)
    mine.append(m)
    count = count + m.count("*")
    
print(count)
for j in range(int(s[0])):
    for k in range(int(s[1])):
        if(mine[j][k] == "*"):
            print(j + 1, k + 1)

    
    
