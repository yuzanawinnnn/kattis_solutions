s = input()
i = 0
count = 0
while i< len(s):
    if(s[i] == 'c' and i+9 <= len(s)):
        if(s[i:i+9] == 'certainly'):
            count = count + 1
            i = i + 9
        else:
            i = i + 1
    else:
        i = i + 1
print(count)
        
