n = int(input())
fri = input()
fri = fri.split(" ")
i = -1
k = 0
while k < 13:
    i = i + 1
    k = k + 1
    if(i == n):
        i = 0
print(fri[i])
