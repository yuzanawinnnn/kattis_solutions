n = int(input())
component = [0,0,0]

for i in range(n):
    s = input()
    s = s.split(" ")
    for j in range(3):
        if(s[j] == "J"):
            component[j] = component[j] + 1
            
print(min(component))
