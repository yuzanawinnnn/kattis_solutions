n = int(input())
line = input()
arr=[]
total = 0
arr = line.split(" ")
for i in range(n):
    if(int(arr[i])<0):
        total = total + abs(int(arr[i]))
print(total)
