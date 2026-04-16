speed = float(input())
distance = float(input())
second = float(input())

speed_ft = speed * 1.467
reach = speed_ft * second
if (distance > reach):
    print("FAILED TEST")
else:
    print("MADE IT")
