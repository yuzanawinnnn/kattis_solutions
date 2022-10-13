cards=list(input())
T=C=G=0
for i in range(len(cards)):
    if(cards[i]=="T"):
        T+=1
    elif(cards[i]=="C"):
        C+=1
    else:
        G+=1

total=T*T+C*C+G*G
while(T>0 and G>0 and C>0):
    total+=7
    T-=1
    C-=1
    G-=1
print(total)

    
        
