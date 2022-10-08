arr=[]
for i in range(5):
    temp=input().split(" ")
    sum=0
    for j in range(4):
        sum+= int(temp[j])
    arr.append(sum)
maxi=max(arr)
print(arr.index(maxi)+1,maxi)

