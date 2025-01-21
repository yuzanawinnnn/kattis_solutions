N = int(input())
s = input()
s = s.split(" ")
s = list(map(int, s))
count = 0

for i in range(1,7):
    for j in range(1,7):
        if(i + j in s):
            count = count + 1

ans = count / 36
print("{:.17f}".format(ans))
