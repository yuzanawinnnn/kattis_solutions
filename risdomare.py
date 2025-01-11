N = int(input())
s = input()

arr = [] #portion or size
summ = []
prefer = ["antal","storlek"]

for i in range(N):
    p = input()
    p = p.split(" ")
    arr.append(int(p[prefer.index(s)]))
    summ.append(int(p[0]) + int(p[1]))

if(summ.count(max(summ)) == 1):
    print(summ.index(max(summ)) + 1)
else:
    maxi = -1
    for j in range(N):
        if(summ[j] == max(summ) and arr[j] > maxi):
            maxi = arr[j]
            index = j
    print(index + 1)
