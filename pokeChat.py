line = input()
num = input()
s = ""
i = 0
while i<len(num):
    s = s + line[int(num[i:i+3])-1]
    i = i + 3
print(s)
