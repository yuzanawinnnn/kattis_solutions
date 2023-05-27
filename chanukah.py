n = int(input())
for i in range(n):
    a, b = map(int,input().split(" "))
    total = b * (b + 1) / 2
    print(a,int(total)+b)
