N=int(input(""))
temp=input("")

temp=temp.split(" ")

arr=[]
sum=0
for i in range(N):
    if(temp[i]!="-1"):
      arr.append(int(temp[i]))

for j in range(len(arr)):
    sum+=arr[j]
    
ans=sum/len(arr)
print(ans)
