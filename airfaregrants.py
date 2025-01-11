n = int(input())
price = []

for i in range(n):
    p = int(input())
    price.append(p)
    
reimburse = int(max(price)/2)

if min(price) <= reimburse:
    print(0)
else:
    print(min(price) - reimburse)
