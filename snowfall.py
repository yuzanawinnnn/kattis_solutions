n = int(input())
snow = 0
for i in range(n):
    w = input()
    weather = w.split(" ")
    if(weather[0] == "0"):
        snow = snow + int(weather[1])
    else:
        if(snow <= int(weather[1]) or snow == 0):
            snow = 0
        else:
            snow = snow - int(weather[1])
print(snow)
