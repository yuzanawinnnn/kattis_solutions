n = int(input())
total = 0
for i in range(n):
    press = int(input())
    if(i%2 == 0):
        press = press
    else:
        press = (-1) * press
    
    total = total + press

if(n %2 != 0):
    print("still running")
else:
    print(abs(total))
