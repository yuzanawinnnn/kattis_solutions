n = int(input())

first = 1
second = 2
total1 = 0
total2 = 0
for i in range(n):
    total1 = total1 + first + i
    total2 = total2 + second + i

if(total1%2 == 0 and total2%2==0):
    print("Even")
elif(total1%2 != 0 and total2%2!=0):
    print("Odd")
else:
    print("Either")


