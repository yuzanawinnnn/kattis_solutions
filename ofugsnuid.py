num=int(input())
arr=[]
for i in range (num):
    temp = input()
    arr.append(temp)
for j in range(num-1,-1,-1):
    print(arr[j])
    
