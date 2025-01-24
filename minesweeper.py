n = input()
n = n.split(" ")
mine = [['.']* int(n[1])]


for j in range(int(n[0])):
    line = []
    for k in range(int(n[1])):
        line.append('.')
    mine.append(line)

for i in range(int(n[2])):
    s = input()
    s = s.split(" ")
    mine[int(s[0])-1][int(s[1])-1] = '*'

for m in range(int(n[0])):
    print(''.join(mine[m]))
    
    
    
