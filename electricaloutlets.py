num = int(input())
for i in range(num):
    temp = input().split(" ")
    total=0
    for j in range(1,len(temp)):
        total+=int(temp[j])
    print(total-len(temp)+2)
