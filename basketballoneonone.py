line = input()
i = 0
A = 0
B = 0
flag = False
while i<len(line)-1:
    s = line[i:i+2]

    if(s[0] == "A"):
        A = A+int(s[1])
        if(flag and abs(A-B) >= 2):
            print("A")
            break
        elif(not flag and A >= 11):
            print("A")
            break
    elif(s[0] == "B"):
        B = B +int(s[1])
        if(flag and abs(B-A) >= 2):
            print("B")
            break
        elif(not flag and B >=11):
            print("B")
            break
    if( A == B and A == 10):
        flag = True
    i = i + 2
