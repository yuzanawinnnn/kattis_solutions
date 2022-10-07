num=input().split(";")
count=0
for i in range(len(num)):
    if "-" in num[i]:
        temp=num[i].split("-")
        count+=int(temp[1])-int(temp[0])+1
    else:
        count+=1
print(count)
