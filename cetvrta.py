p1=input().split(" ")
p2=input().split(" ")
p3=input().split(" ")

if(int(p1[0])==int(p2[0])):
    ans1 = int(p3[0])
elif(int(p1[0])==int(p3[0])):
    ans1 = int(p2[0])
elif(int(p2[0])==int(p3[0])):
    ans1 = int(p1[0])
 
if(int(p1[1])==int(p2[1])):
    ans2 = int(p3[1])
elif(int(p1[1])==int(p3[1])):
    ans2 = int(p2[1])
elif(int(p2[1])==int(p3[1])):
    ans2 = int(p1[1])

print(ans1,ans2)
