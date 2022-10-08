card = input().split(" ")
arr={}
for i in range(len(card)):
    if card[i][0] not in arr:
        arr[card[i][0]]=1
    else:
        arr[card[i][0]]=arr[card[i][0]]+1
#print(max(arr,key=arr.get))
print(max(arr.values()))
