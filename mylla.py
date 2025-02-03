n = int(input())
s = input()
win = {"A":0 , "H":0}
victory = {"A":0 , "H":0}
flag = False
for i in range(len(s)):
    
    win[s[i]] = win[s[i]] + 1
    if win[s[i]] == 3:
        victory[s[i]] = victory[s[i]] + 1
        win = {"A":0 , "H":0}
        for key,val in victory.items():
            if (val == n):
                if(key == "A"):
                    print("Hannes")
                    flag = True
                else:
                    print("Arnar")
                    flag = True
    if(flag == True):
        break
                
    
        
