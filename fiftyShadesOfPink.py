n = int(input())
count = 0
for i in range(n):
    name = input().lower()
    if("pink" in name or "rose" in name):
        count = count +1
if(count == 0):
    print("I must watch Star Wars with my daughter")
else:
    print(count)
