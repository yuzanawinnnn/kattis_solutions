s = input()
s = s.split(" ")
total = 0
for i in range(int(s[0])):
    total += int(input())

if(total<= int(s[1])):
    print("Jebb")
else:
    print("Neibb")
