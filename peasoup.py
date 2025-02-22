n = int(input())
flag = False

for i in range(n):
    count = int(input())
    menu = []
    restaurant = input()
    for j in range(count):
        m = input()
        menu.append(m)
    if(flag == False and "pea soup" in menu and "pancakes" in menu):
        name = restaurant
        flag = True
        
if(flag == False):
    print("Anywhere is fine I guess")
else:
    print(name)
        
    
