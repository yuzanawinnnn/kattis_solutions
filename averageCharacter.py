import math
s = input()
total = 0
for i in range(len(s)):
    total = total + ord(s[i])
letter = math.floor(total/len(s))
print(chr(letter))
