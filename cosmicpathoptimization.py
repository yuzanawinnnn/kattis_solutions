import math
n = int(input())
temp = input()
temp = temp.split(" ")

mean = 0
for i in range(n):
    mean = mean + int(temp[i])

print(math.floor(mean/n))
