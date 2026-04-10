n = input().split(" ")
days = int(n[0]) // int(n[1]) 
if (int(n[0]) % int(n[1]) != 0):
    days = days + 1
if(int(n[1]) >= int(n[0])):
    print(1)
else:
    print(days)
