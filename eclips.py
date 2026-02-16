a = input().split(" ")
b = ""
for i in a:
    if "e" in i:
        b = b + i + " "
if(b == ""):
    print("oh noes")
else:
    print(b)
        
