num = input().split(" ")
num = list(map(int, num))
num.sort()
order=input()
ans=[]
for i in range(len(order)):
    if(order[i]=="A"):
        ans.append(num[0])
    elif(order[i]=="B"):
        ans.append(num[1])
    elif(order[i]=="C"):
        ans.append(num[2])
print(ans[0],ans[1],ans[2])
