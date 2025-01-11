n = int(input())
s = input()
s = s.split(" ")
abb = ""

for i in range(n):
    if(s[i][0].isupper()):
        abb = abb + s[i][0]
        
print(abb)
