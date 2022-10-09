word = input()
arr=[]
string=""
for j in range(len(word)):
    arr.append(word[j])
for i in range(len(arr)):
    ch = arr[i]
    if(ch=='a'or ch =='e' or ch=='i' or ch=='o' or ch=='u'):
        string+=ch
        arr[i+1]=""
        arr[i+2]=""

    elif(ch!='a'or ch !='e'or ch!='i' or ch!='o' or ch!='u'):
        string+=ch
print(string)
        
