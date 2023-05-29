temp=input(" ")

temp=temp.split("-")

arr=[]
for i in range(len(temp)):
    tt=temp[i]
    arr.append(tt[0])

TEMP=""
for j in range(len(arr)):
 TEMP+=arr[j]

print(TEMP)
