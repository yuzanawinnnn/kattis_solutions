import math
n = int(input())
time = [0]
distance = [0]
speed = 0
s = input()
for i in range(1,n):
    s = input()
    s = s.split(" ")
    time.append(int(s[0]))
    distance.append(int(s[1]))
    
    if((distance[i]-distance[i-1]) / (time[i]-time[i-1]) > speed):
        speed = math.floor((distance[i]-distance[i-1]) / (time[i]-time[i-1]) )

print(speed)
