s = input()
i = len(s)-1
ans = ""
while True:
    if(s[i]) == '.':
        break
    ans = s[i] + ans
    i = i - 1
print("."+ans)
