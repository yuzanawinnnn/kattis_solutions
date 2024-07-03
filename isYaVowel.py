s = input()
v = 0
y = 0
vowel = ['a', 'e', 'i', 'o', 'u']
for i in range(len(s)):
    if s[i] in vowel:
        v = v + 1
    elif s[i] == 'y':
        y = y + 1
print(v, v+y)
