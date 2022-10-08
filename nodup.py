word = input().split(" ")
flag=0
for i in range(len(word)):
    for j in range(0,len(word)):
        if(word[i]==word[j] and i!=j):
            print("no")
            flag=1
            break
    if (flag==1):
        break
if(flag==0):
    print("yes")
