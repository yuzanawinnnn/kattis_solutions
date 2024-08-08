n = int(input())
name = []
gift = []
for i in range(n):
    s = input()
    s = s.split(" ")
    name.append(s[0])
    gift.append(int(s[1]))
print(name[gift.index(max(gift))])
