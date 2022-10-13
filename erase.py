num = int(input())
s1=list(input())
s2=input()
for i in range(num):
    s3=""
    for j in range(len(s1)):
        if(s1[j]=="0"):
            s1[j]="1"
            s3+="1"
        else:
            s1[j]="0"
            s3+="0"
if(s3==s2):
    print("Deletion succeeded")
else:
    print("Deletion failed")
    
