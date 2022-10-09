string = input()
count=0
for i in range(len(string)):
    ch = string[i]
    if(ch=='A' or ch=='a' or ch=='E' or ch =='e' or ch=='I'
 or ch=='i' or ch=='O' or ch=='o' or ch=='U' or ch=='u'):
     count+=1
print (count)
