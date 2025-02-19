s = input()
s = list(s)

T = 0
H = 0
for i in range(len(s)):
    if s[i] == "T":
        T = T + 1
    else:
        H = H + 1
        
    if(T>= 11 or H>=11):
        if(T-H >= 2 or H-T>=2):
            T = 0
            H = 0

print(str(T)+"-"+str(H))
