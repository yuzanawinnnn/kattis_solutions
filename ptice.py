Adrian = ['A', 'B', 'C']
Bruno = ['B', 'A', 'B', 'C']
Goran = ['C', 'C', 'A', 'A', 'B', 'B' ]
a= b = g = 0
n = int(input())
line = input()
flag = False
f1 = f2 = f3 = False
i = 1
while flag == False:
    if(f1 == False):
        temp1 = Adrian * i
    if(f2 == False):
        temp2 = Bruno * i
    if(f3 ==False):
        temp3 = Goran * i
    if(f1 == True and f2 == True and f3== True):
        flag = True
    if(len(temp1)>=n):
        f1 = True
    if(len(temp2)>=n):
        f2 = True
    if(len(temp3)>=n):
        f3 = True
    i =i + 1
for j in range(n):
    if(line[j] == temp1[j]):
        a = a + 1
    if(line[j] == temp2[j]):
        b = b + 1
    if(line[j] == temp3[j]):
        g = g + 1
print(max(a,b,g))
if(a == max(a,b,g)):
    print("Adrian")
if(b == max(a,b,g)):
    print("Bruno")
if(g == max(a,b,g)):
    print("Goran")

