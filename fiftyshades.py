num = int(input())
count=0
for i in range(num):
    temp= input().lower()
    if("pink" in temp or "rose" in temp):
        count+=1
if (count!=0):
    print(count)
else:
    print("I must watch Star Wars with my daughter")
