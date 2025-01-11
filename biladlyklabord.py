s = input()
s = list(s)

for i in range(len(s)-1):
    if(s[i] == s[i+1]):
        s[i] = ""

s = ''.join(s)
print(s)
