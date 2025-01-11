s = input()
s = s.split(" ")
n = int(s[0])
a = int(s[1])
b = int(s[2])

FB = 0
F = 0
B = 0

for i in range(1, n+1):
    if(i % a == 0 and i % b == 0):
        FB = FB + 1
    elif(i % a == 0):
        F = F + 1
    elif(i % b == 0):
        B = B + 1

print(F,B,FB)
