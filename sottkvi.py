n = input()
n = n.split(" ")
bd = int(n[1]) + int(n[2])
count = 0

for i in range(int(n[0])):
    day = int(input())
    if(day + 13 < bd):
        count = count + 1

print(count)
