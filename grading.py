grade = input().split(" ")
A = int(grade[0])
B = int(grade[1])
C = int(grade[2])
D = int(grade[3])
E = int(grade[4])
per = int(input())
if(per>=A):
    print("A")
elif(per>=B):
    print("B")
elif(per>=C):
    print("C")
elif(per>=D):
    print("D")
elif(per>=E):
    print("E")
else:
    print("F")
