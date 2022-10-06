n=int(input())
arr=[]
for i in range(n):
    temp = input().split(" ")
    if(int(temp[1])-int(temp[2])>int(temp[0])):
        arr.append("advertise")
    elif(int(temp[1])-int(temp[2]) == int(temp[0])):
        arr.append("does not matter")
    else:
        arr.append("do not advertise")
for j in range(n):
    print(arr[j])
