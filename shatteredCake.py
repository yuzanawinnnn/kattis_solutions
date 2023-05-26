w = int(input())
n = int(input())
area = 0
for i in range(n):
    line = input()
    line = line.split(" ")
    area = area + int(line[0]) * int(line[1])
l = area / w
print(int(l))
