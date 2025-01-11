n = int(input())
count = 0

for i in range(n):
    candidate = int(input())
    if(candidate % 2 != 0):
        count = count + 1

print(count)
