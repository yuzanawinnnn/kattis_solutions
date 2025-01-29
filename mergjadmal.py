s = input()
s = list(s)
flag = False

for i in range(len(s)):
    if(i < len(s) - 2):
        if(s[i] == "4" and s[i+1] == "2" and s[i+2] == "0"):
            print("Mergjad!")
            flag = True
            break
    if(i < len(s) - 1):
        if(s[i] == "6" and s[i+1] == "9"):
            print("Mergjad!")
            flag = True
            break

if(not flag):
    print("Leim!")
