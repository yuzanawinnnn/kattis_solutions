num=int(input())
knot1=input().split(" ")
knot2=input().split(" ")

for i in range(num):
    flag=0
    for j in range(num-1):
        if(knot2[j]==knot1[i]):
           flag=1
    if(flag==0):
        ans=knot1[i]
print(ans)
