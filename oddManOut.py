n=int(input())
a=[]
for i in range(0,n):
     t=input()
     s=input()
     arr=s.split(" ")
     for j in range(0,len(arr)):
          if(arr.count(arr[j])<2):
               a.append(arr[j])
               break
for i in range(0,n):
     print("Case #"+str(i+1)+": "+str(a[i]))
