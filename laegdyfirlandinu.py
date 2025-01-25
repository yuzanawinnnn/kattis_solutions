n = input().split(" ")
temp = []
 
for i in range(int(n[0])):
     s = input().split(" ")
     temp.append(list(map(int, s)))


flag = False

for j in range(1,int(n[0])-1):
    for k in range(1,(int(n[1]))-1):
        if(temp[j][k]< temp[j-1][k] and temp[j][k]< temp[j+1][k] and temp[j][k]< temp[j][k-1] and temp[j][k]< temp[j][k+1]):
            flag = True
            break

if(flag == True):
    print("Jebb")
else:
    print("Neibb")
    
