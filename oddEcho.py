n = int(input())
arr=[]
for i in range(n):
    word=input()
    if((i+1)%2 !=0):
        arr.append(word)
for i in range(len(arr)):
    print(arr[i])
