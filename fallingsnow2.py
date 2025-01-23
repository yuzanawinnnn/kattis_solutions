n = input()
n = n.split(" ")
snow = []

for i in range(int(n[0])):
    s = input()
    s = list(s)
    snow.append(s)


for j in range(int(n[0])-1,-1,-1):
    for k in range(int(n[1])):
        if(snow[j][k] == '.'):
            for l in range(j-1, -1, -1):
                if(snow[l][k] == 'S'):
                    snow[j][k] = 'S'
                    snow[l][k] = '.'
                    break
for m in range(len(snow)):
    print(''.join(snow[m]))
