N = int(input())
chores = []
for i in range(N):
    s = input()
    if(s not in chores):
        chores.append(s)
    
for j in range(len(chores)):
    print(chores[j])
