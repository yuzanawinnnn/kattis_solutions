N = int(input())
german = input()
german = german.split(" ")
dictionary = dict()
translation = ""

M = int(input())
for i in range(M):
    s = input()
    s = s.split(" ")
    dictionary[s[0]] = s[1]

for i in range(N):
    translation = translation + dictionary[german[i]] + " "
    
print(translation[:len(translation)-1])
