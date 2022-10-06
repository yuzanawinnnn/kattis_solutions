num=int(input())
arr=[]
sum=0
for i in range(num):
    temp=input()
    sum+=int(temp[:len(temp)-1])**int(temp[len(temp)-1])
print(sum)
