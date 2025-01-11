n = int(input())
s = input()
coffee = 0
awake = 0

for i in range(n):
    if(s[i] == "1"):
        coffee = 3
    if(coffee > 0):
        awake = awake + 1
        coffee = coffee - 1
    
print(awake)
