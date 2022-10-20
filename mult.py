num = int(input())
temp = int(input())
first = temp
found=0
arr=[]
for i in range(num-1):
    temp = int(input())
    if(found==1):
        first=temp
        found=0
    elif(temp%first==0):
        arr.append(temp)
        found=1
for j in range(len(arr)):
    print(arr[j])
    
