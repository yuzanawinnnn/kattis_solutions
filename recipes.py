import math
n = int(input())
for i in range(n):
    s = input().split(" ")
    ing = int(s[0])
    no_port = int(s[1])
    desired = int(s[2])
    
    scl_fctr = desired / no_port
    
    ing_dict = {}
    for j in range(ing):
        inp = input().split(" ")
        
        if(inp[2] == "100.0"):
            main_wgt = float(inp[1]) * scl_fctr
            ing_dict[inp[0]] = main_wgt
            temp = inp[0]
        else:
            ing_dict[inp[0]] = float(inp[2])
    
    print("Recipe #", i + 1)
    for key, val in ing_dict.items():
        if(key != temp):
            print(key, val * main_wgt /100)
        else:
            print(key, val)
    print("----------------------------------------")
            
    
    
