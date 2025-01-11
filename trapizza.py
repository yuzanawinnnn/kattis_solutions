import math
d = int(input())
a = int(input())
b = int(input())
h = int(input())

r = d/2
mahjong = math.pi * r * r
trapizza = 0.5 * (a + b) * h

if(mahjong > trapizza):
    print("Mahjong!")
elif(mahjong < trapizza):
    print("Trapizza!")
else:
    print("Jafn storar!")
