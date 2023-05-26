line = input()
s =" "
for i in range(len(line)):
    if(s[-1] == line[i]):
        continue
    else:
        s = s + line[i]
print(s[1:])
