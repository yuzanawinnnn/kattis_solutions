n=int(input())
arr=[]
for i in range(n):
    temp = int(input())
    arr.append(temp)
    
for j in range(n):
    if (arr[j]%2 ==0):
        print(arr[j]," is even")
    else:
        print(arr[j]," is odd")
