forb = input()
s = input()
s = s.split(" ")
res = ""
for j in range(len(s)):
    for i in forb:
        if(i in s[j]):
            s[j] = "*" * len(s[j])
            break
    res = res + s[j] + " "
print(res)
        
    
