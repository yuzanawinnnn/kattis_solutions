n = int(input())
flight = []

for i in range(n):
    f = input()
    f = f.split(" ")
    
    for j in range(n):
        if(f[j] != "-1"):
            flight.append(str(i+1)+" "+ str(j+1)+" "+f[j])
print(len(flight))        
for k in range(len(flight)):
    print(flight[k])
