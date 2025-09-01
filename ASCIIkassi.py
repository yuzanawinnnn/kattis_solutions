n = int(input())
horizon = "+"
for i in range(n):
    horizon += "-"
horizon += "+"
print(horizon)
vertical = horizon
vertical = vertical.replace("+", "|")
vertical = vertical.replace("-", " ")
for j in range(n):
    print(vertical)
print(horizon)
    
