F = input()
H = input()
H = list(H)

j = 0
for i in range(len(F)):
    
    while True and j<len(H):
        if(F[i] == H[j]):
            j = j + 1
            break
        else:
            H[j] = ""
            j = j + 1

res = ''.join(H)

if(res == F):
    print("Ja")
else:
    print("Nej")
        
