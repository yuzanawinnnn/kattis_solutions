n = input().split(" ")
n = list(map(int, n))
health = 0

while n[0] > 0:
    if(n[0] >=1 and n[1] >=1):
        health = health + 10
        n[0] = n[0] - 1
        n[1] = n[1] - 1
    elif(n[0] >=3):
        health = health + 10
        n[0] = n[0] - 3
    elif(n[0] >=2):
        health = health + 3
        n[0] = n[0] - 2
    elif(n[0] >=1):
        health = health + 1
        n[0] = n[0] - 1

print(health)
        
        
