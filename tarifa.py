X=int(input(""))
N=int(input(""))

arr=[]
sum=0

for i in range (N):
    MM=int(input(""))
    arr.append(MM)

for j in range (N):
    temp=X-arr[j]
    sum+=temp
       

print(sum+X)
