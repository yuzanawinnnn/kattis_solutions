bottle = int(input())
A = input()
A = A.split(" ")
B = input()
B = B.split(" ")

Alice = 0
Bob = 0

for i in range(bottle):
    Alice = Alice + int(A[0]) + i * int(A[1])
    Bob = Bob + int(B[0]) + i * int(B[1])
    
if(Alice < Bob):
    print("Alice")
elif(Bob < Alice):
    print("Bob")
else:
    print("=")
