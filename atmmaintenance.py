nk = input().split(" ")
n = input().split(" ")
s = ""
nk = int(nk[1])

for i in range(len(n)):
    if(nk >= int(n[i])):
        s = s + "1"
        nk = nk - int(n[i])
    else:
        s = s + "0"
print(s)
        
