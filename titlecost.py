s = input().split(" ")
cap = False

for i in range(1, len(s[0])):
    if(s[0][i].isupper()):
        cap = True
        print("{:.14f}".format(float(s[1])))
        break

if(cap == False):
    print(len(s[0]))
        
