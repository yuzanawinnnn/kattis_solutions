arr=""
for i in range(5):
    s=input()
    if "FBI" in s:
        arr+=str(i+1)+" "
if(len(arr)==0):
    print("HE GOT AWAY!")
else:
    print(arr)
