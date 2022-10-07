arr=[1,1,2,2,2,8]
num=input().split(" ")

for i in range(6):
    arr[i]=arr[i]-int(num[i])

print(arr[0],arr[1],arr[2],arr[3],arr[4],arr[5])
