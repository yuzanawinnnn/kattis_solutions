import math
string=input("")
a=string.split(" ")
print(math.ceil(int(a[0])/math.sin(math.radians(int(a[1])))))
