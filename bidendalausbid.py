prev = input().split(":")
prev = list(map(int, prev))
now = input().split(":")
now = list(map(int, now))
total = 0

if(now[1] >= prev[1]):
    total = total + now[1] - prev[1]
else:
    total = total + now[1] + 60 - prev[1]
    now[0] = now[0] - 1

if(now[0] >= prev[0]):
    total = total + ( now[0] - prev[0] ) * 60
else:
    total = total + ( now[0] + 24 - prev[0] ) * 60
    
print(total)
