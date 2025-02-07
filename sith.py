name = input()
a = int(input())
b = int(input())
ans = int(input())
diff = a - b

if(diff >= 0):
    print("VEIT EKKI")
else:
    if(ans == diff):
        print("JEDI")
    else:
        print("SITH")
    
