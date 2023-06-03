L=int(input(""))
D=int(input(""))
X=int(input(""))

arr=[]
sum=0

for i in range(L,D+1):
    temp=str(i)
    for j in str(temp):
       sum+=int(j)
    if(sum==X):
        arr.append(i)
    sum=0
   
       
arr.sort()

print(arr[0])
print(arr[-1])
