arr=[]
for i in range(10):
    num = int(input())
    temp = num%42
    if(temp not in arr):
        arr.append(temp)
print(len(arr))
