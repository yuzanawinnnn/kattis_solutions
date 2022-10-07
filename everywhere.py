test=int(input())
for i in range(test):
    arr=[]
    num=int(input())
    for j in range(num):
        temp=input()
        if temp not in arr:
           arr.append(temp)
    print(len(arr))
