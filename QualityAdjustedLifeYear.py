N=int(input(" "))

arr=[]
sum=0

for i in range(N):
   temp=input(" ")
   arr.append(temp)

for j in range(N):
   TEMP=arr[j]
   TEMP=TEMP.split(" ")
   sum+=float(TEMP[0])*float(TEMP[1])
   
  
print(round(sum, 3))
