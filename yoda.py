n = input()
m = input()

if(len(n) < len(m)):
    n = (len(m) - len(n)) * "0" + n
elif(len(m) < len(n)):
    m = (len(n) - len(m)) * "0" + m

n = list(n)
m = list(m)

for i in range(len(n)):
    if(int(m[i]) < int(n[i])):
        m[i] = ""
    elif(int(n[i]) < int(m[i])):
        n[i] = ""

m = ''.join(m)
n = ''.join(n)

if(len(n) == 0):
    print("YODA")
else:
    print(int(n))
    
if(len(m) == 0):
    print("YODA")
else:
    print(int(m))
