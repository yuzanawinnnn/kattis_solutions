G = input().split(" ")
E = input().split(" ")

G = sum(list(map(int, G)))
E = sum(list(map(int, E)))

if(G > E):
    print("Gunnar")
elif(E > G):
    print("Emma")
else:
    print("Tie")
