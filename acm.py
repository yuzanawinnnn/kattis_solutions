ans = {}
time = 0
count = 0
while True:
    s = input()
    if(s == "-1"):
        break
    s = s.split(" ")
    if(s[2] == "right"):
        count = count + 1
        if(s[1] in ans.keys()):
            time = time + int(s[0]) + ans[s[1]] * 20
        else:
            time = time + int(s[0])
    elif(s[1] in ans.keys()):
        ans[s[1]] = ans[s[1]] + 1
    else:
        ans[s[1]] = 1
print(count, time)
    
