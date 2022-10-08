arr=[1,0,0]
move=input()
for i in move:
    if(i == "A"):
        temp = arr[0]
        arr[0]=arr[1]
        arr[1]=temp
    if(i == "B"):
        temp = arr[1]
        arr[1]=arr[2]
        arr[2]=temp
    if(i == "C"):
        temp = arr[0]
        arr[0]=arr[2]
        arr[2]=temp
print(arr.index(1)+1)
