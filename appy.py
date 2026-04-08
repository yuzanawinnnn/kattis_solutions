n = int(input())
s = []


for i in range(n):
    app = input().split(" ")
    j = 1
    while True and j<=int(app[0]):
        if(app[j] not in s):
            s.append(app[j])
            break
        else:
            j = j + 1



s = " ".join(s)
print(s)
            
    
