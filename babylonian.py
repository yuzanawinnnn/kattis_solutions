import math
n = int(input())

for i in range(n):
    num = input()
    total = 0
    c = num.count(",")
    if(c == 0):
        print(int(num))
    else:
        num = num.split(",")
        k = 0
        for j in range(c,-1,-1):
            if(num[k] == ''):
                num[k] = 0
            total = total + int(num[k])* int(math.pow(60,j))
            k = k + 1
        print(total)

