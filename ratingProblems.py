line = input()
n, r= line.split()
maxi = (int(n)-int(r))*3
mini = (int(n)- int(r))*(-3)
total = 0
for i in range(int(r)):
    rate = int(input())
    total = total + rate
print((mini+total)/int(n), (maxi+total)/int(n))
