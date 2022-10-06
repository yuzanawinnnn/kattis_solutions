temp=input()
flag=1
for i in range(len(temp)):
    for j in range(len(temp)):
        if (temp[i] == temp [j] and i!=j):
            flag=0
if (flag==1):
    print(1)
else:
    print(0)
