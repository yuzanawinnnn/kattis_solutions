n = int (input())
arr=set()
for i in range(n):
    temp = input().split(" ")
    for j in range(int(temp[0]),int(temp[1])+1):
        arr.add(j)
print(len(arr))
    
